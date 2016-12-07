import numpy as np
import re
import json
import math

def transform_json(data):
  data = data['places']
  result = {}

  for i in data:
    time = str(i['time'][0]['open']) + "-" + str(i['time'][0]['close'])
    result[i['name']] = {'time':time, 'resto':i['eatery_nearby']}

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

  range_time = str_start + " - " + close_time
  time.append(range_time)

  return time

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


def delete_some_pattern(array, char_hash):
  result = array
  for key in char_hash:
    tmp = []
    for i in result:
      pat = key+"[^"+key+"]"+key
      pattern = re.compile(pat)
      if not pattern.match(i):
        tmp.append(i)

    result = tmp

  return result
  

def variansi(word):
  w_unique = list(set(list(word)))
  w_size = []

  for i in w_unique:
    w_size.append(word.count(i))

  sums = 0
  for i in range(0, len(w_size)):
    for j in range(i+1, len(w_size)):
      sums = sums + abs(w_size[i]-w_size[j])

  return sums


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
      if (variansi(x) < variansi(y)):
        return -1
      else:
        return 1

def generate_itinerary(open_time, close_time, data_json, data):
  #buat range waktu
  time = create_time(open_time, close_time)

  #ubah bentuk json 
  data_json = transform_json(data_json)

  #cut data jika > 24 tempat, asumsi 1 hari 24 jam (1 tempat minimal 1 jam)
  data = np.array(data)
  data = data[:24]

  #bikin lokasi jadi char
  tempat_char = {}
  char_array_time = {}
  for idx,i in enumerate(data):
    tempat_char[i] = chr(idx+97)
    char_array_time[tempat_char[i]] = create_time_slot(data_json[i]['time'], time)

  #bikin semua kemungkinan
  result = create_all_possibilities(char_array_time, time)

  #buang yang pola regexnya (a[^a]*a)
  result = delete_some_pattern(result, char_array_time)

  #sort, ambil yang terbaik
  sortedDict = sorted(result, cmp=comparator)
  print sortedDict

  
  return sortedDict[0]


with open('static/json/places.json') as data_file:
  data = json.load(data_file)

generate_itinerary("10.20", "14.30", data, ["Soekarno Bridge", "Christ Blessing"])
