import numpy as np
import re
import json
import math
import settings
import random

settings.init_build()

#method utk transform bentuk json, bisar jadi hash
def transform_json(data):
  data = data['places']
  result = {}

  for i in data:
    time = str(i['time'][0]['open']) + "-" + str(i['time'][0]['close'])
    address = i['location'][0]['address']+" "+i['location'][0]['city']+" "+i['location'][0]['province']+" "+i['location'][0]['island']
    result[i['name']] = {'time':time, 'resto':i['eatery_nearby'], 'address': address, 'city': i['location'][0]['city']}

  return result

#method untuk create range waktu jalan-jalan
def create_time(open_time, close_time):
  str_start = open_time
  start = float(open_time)
  end = int(math.floor(start) + 1)
  str_end = str(end)+".00"

  time = []

  while end < float(close_time):    
    range_time = str_start + "-" + str_end
    time.append(range_time)

    start = end
    str_start = str_end
    end = start+1
    str_end = str(end)+".00"

  range_time = str_start + "-" + close_time
  time.append(range_time)

  return time

#bikin time slot dari jam mulai jalan-jalan sampai selesai jalan-jalan
def create_time_slot(range_time, slot):
  result = []

  times = range_time.split('-')
  time_1 = float(times[0])
  time_2 = float(times[1])

  for idx,i in enumerate(slot):
    slot_i = i.split('-')
    slot_time_1 = float(slot_i[0])
    slot_time_2 = float(slot_i[1])

    if (slot_time_1 >= time_1 and slot_time_2 <= time_2):
      result.append(idx)

  return result

#bikin semua kemungkinan susunan jalan-jalan
def create_all_possibilities(cat, time):
  result = ['']
  for idx,i in enumerate(time):
    tmp_result = []
    for a in cat:
      if idx in cat[a]:
        for j in result:
          tmp_result.append(j+a)

    if (tmp_result == []):
      for j in result:
        tmp_result.append(j+'-')

    result = tmp_result

  return result

#buang pattern yang jalan2 ke tempat sama tapi 2 kali atau lebih
def delete_some_pattern(array, char_hash):
  tmp = []
  for key in char_hash:
    for i in array:
      pat = "(.*)"+key+"[^"+key+"]+"+key+"(.*)"
      pattern = re.compile(pat)
      if pattern.match(i):
        tmp.append(i)

  return [x for x in array if x not in tmp]
  
#variasi perjalanan, keseimbangan jalan2nya
def variasi(word):
  w_unique = list(set(list(word)))
  w_size = []

  for i in w_unique:
    w_size.append(word.count(i))

  sums = 0
  for i in range(0, len(w_size)):
    for j in range(i+1, len(w_size)):
      sums = sums + abs(w_size[i]-w_size[j])

  return sums

#untuk sort dari semua kemungkinan susunan itin
def comparator(x,y):
  x = x.replace('-','')
  y = y.replace('-','')
  x_size = len(list(set(list(x))))
  y_size = len(list(set(list(y))))
  if (x_size > y_size):
    return -1
  elif (x_size < y_size):
    return 1
  else:
    if (len(x) > len(y)):
      return -1
    elif (len(x) < len(y)):
      return 1
    else:
      if (variasi(x) < variasi(y)):
        return -1
      else:
        return 1

#transform string to json
def string_to_json(string, char_loc, data_json, time_slot):
  result = []
  for idx,i in enumerate(list(string)):
    if not (i=='-'):
      new_hash = {"type": "normal", "name": char_loc[i], "address": data_json[char_loc[i]]['address'], "time": time_slot[idx] }
      result.append(new_hash)

  return result

#ambil restoran terdekat
def get_nearby_resto(data_json, place, eat_time):
  restos = []
  restos_no_add = []
  resto_array = data_json[place]['resto']
  city = data_json[place]['city']

  resto_hash = settings.name_ids
  place_hash = settings.places

  for i in resto_array:
    try:
      name_ids = settings.name_ids[i]
      for j in name_ids:
        #validasi kota
        if j['location']['city'] == city:
          #validasi waktu makan
          resto_open_time = place_hash[j[index]]['time'][0]['open']
          resto_close_time = place_hash[j[index]]['time'][0]['close']
          time = eat_time.split('-')
          eat_time_start = float(time[0])
          eat_time_end = float(time[1])
          if (resto_open_time <= eat_time_start and resto_close_time >= eat_time_end):
            restos.append(j['index'])
    except:
      restos_no_add.append(i)
    

  if not (restos == []):
    rand_resto = random.choice(restos)
    i = place_hash[rand_resto]
    j = i['location'][0]
    resto_json = { 'name' : i['name'], 'address' : (j['address']+" "+j['city']+" "+j['province']+" "+j['island']+", near "+place)}
    return resto_json

  elif not (restos_no_add == []):
    rand_resto = random.choice(restos_no_add)
    return {'name': rand_resto, 'address': ('near '+ place)}

  else:
    return []


#mengganti json itinerary dengan yang sudah ada rekomendasi restorannya
def resto_recommendation(data_json, itin, time, idx, eat_time):
  if not (itin == []) and (idx >= 0) and (idx <len(itin))  :
    i = get_nearby_resto(data_json, itin[idx]['name'], eat_time)
    if not (i == []):
      itin[idx]['type'] = 'recommendation'
      itin[idx]['name'] = i['name']
      itin[idx]['address'] = i['address']
  return itin



#cari index waktu di itinerary yang pas buat makan pagi, siang, malam
def index_for_resto(sortedDict, time):
  jam_pagi = "8.00-9.00"
  jam_siang = "12.00-13.00"
  jam_malam = "18.00-19.00"
  pagi = siang = malam = -1
  t_pagi = t_siang = t_malam = ""

  def find_place(SD, idx):
    result = ""
    result_2 = idx

    if (SD[idx] != "-"):
      if ((idx-1)>=0 and SD[idx-1]!= "-"):
        result = SD[idx-1]
      elif ((idx+1)<len(SD) and SD[idx+1]!= "-"):
        result = SD[idx+1]
      else:
        result_2 = -1
    else:
      if (SD.count(SD[idx]) > 1):
        result = SD[idx]
    return (result, result_2)


  if jam_pagi in time:
    pagi = time.index(jam_pagi)
    (t_pagi, pagi)= find_place(sortedDict, pagi)
  
  if jam_siang in time:
    siang = time.index(jam_siang)
    (t_siang, siang)= find_place(sortedDict, siang)

  if jam_malam in time:
    malam = time.index(jam_malam)
    (t_malam, malam)= find_place(sortedDict, malam)


  #cek di slot ime ada apa ngk
  #cari indexnya

  return ([pagi, t_pagi], [siang, t_siang], [malam, t_malam])

#reduksi table
def table_reduction(data_json):
  data_json_baru = []
  prev = {}
  for idx,i in enumerate(data_json):
    if idx > 0:
      if i['name'] == prev['name']:
        time_next = i['time'].split('-')
        time_prev = prev['time'].split('-')
        prev['time'] = time_prev[0]+'-'+time_next[1]
      else:
        data_json_baru.append(prev)
        prev = i
    else:
      prev = i
  if not (prev == {}):
    data_json_baru.append(prev)

  return data_json_baru


#main
def generate_itinerary(open_time, close_time, data_json, data):
  #buat range waktu
  time = create_time(open_time, close_time)

  #ubah bentuk json 
  data_json = transform_json(data_json)

  #cut data jika > n jam, asumsi 1 tempat minimal 1 jam
  data = np.array(data)
  data = data[:len(time)]

  #bikin lokasi jadi char
  char_loc = {}
  char_array_time = {}
  #print data_json
  for idx,i in enumerate(data):
    char_loc[chr(idx+97)] = i
    char_array_time[chr(idx+97)] = create_time_slot(data_json[i]['time'], time)

  #bikin semua kemungkinan
  result = create_all_possibilities(char_array_time, time)

  #buang yang pola regexnya (a[^a]*a)
  result = delete_some_pattern(result, char_array_time)

  #sort, ambil yang terbaik
  sortedDict = sorted(result, cmp=comparator)

  #olah rekomendasi resto
  (pagi, siang, malam) = index_for_resto(sortedDict[0], time)
  s = list(sortedDict[0])
  if (pagi[0] != -1):
    s[pagi[0]] = pagi[1]
  if (siang[0] != -1):
    s[siang[0]] = siang[1]
  if (malam[0] != -1):
    s[malam[0]] = malam[1]
  sortedDict[0] = "".join(s)

  #buang yang kosong di awal
  x = 0
  count = 0
  while sortedDict[0][x] == "-":
    count += 1
    x +=1 


  result_json = string_to_json(sortedDict[0], char_loc, data_json, time)

  #rekomendasi pagi
  result_json = resto_recommendation(data_json, result_json, time, pagi[0]-count, "8.00-9.00")
  #rekomendasi siang
  result_json = resto_recommendation(data_json, result_json, time, siang[0]-count, "12.00-13.00")
  #rekomendai malam
  result_json = resto_recommendation(data_json, result_json, time, malam[0]-count, "18.00-19.00")

  #reduksi hasil
  result_json = table_reduction(result_json)

  return result_json



