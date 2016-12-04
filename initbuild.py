# made
# This class is used to read file json at the beginning
# Also to build index based on category and location

import json
import os

# global variable yang harusnya bisa diakses di semua file
places = []
categories_dict = {}
cities_dict = {}
provinces_dict = {}

def createIndexLocation(place, idx):
	# update index location: province
	province = place["location"][0]["province"]
	if not province:
		province = place["location"][0]["island"]
	if province in provinces_dict:
		provinces_dict[province].append(idx)
	else:
		provinces_dict[province] = [idx]

	# update index location: city
	city = place["location"][0]["city"]
	if city in cities_dict:
		cities_dict[city].append(idx)
	else:
		cities_dict[city] = [idx]

def createIndexAttractions(place, idx):
	# update index categories
	ctgs = place["categories"]
	for j in range(len(ctgs)):
		ctg = ctgs[j]
		if ctg in categories_dict:	
			categories_dict[ctg].append(idx)
		else:
			categories_dict[ctg] = [idx]

def createIndexRestaurants(place, idx):
	# update index categories
	categories_dict["restaurant"].append(idx)
	ctg = place["categories"][0]
	if "halal" in ctg.lower():
		categories_dict["halal"].append(idx)


# type: 1 -> attractions; 
# 		2 -> restaurants
def readJson(filename, type):
	# load all json into temporary variable data
	with open(filename) as data_file:
		data = json.load(data_file)
	data_file.close()

	idx = len(places)

	for i in range(len(data["places"])):
		place = data["places"][i]
		
		if place["name"]:
			# insert new place into array
			places.append(place)
			# create index categories
			if (type == 1): 
				createIndexAttractions(place, idx)
			elif (type == 2):
				createIndexRestaurants(place, idx)
			# create index location
			createIndexLocation(place, idx)
			idx += 1

# MAIN PROGRAM
# saat program pertama running, jalankan ini
def initbuild(): 
	# lanjut tambahin restaurant & halal disini
	categories_dict["restaurant"] = []
	categories_dict["halal"] = []
	for filename in os.listdir('./Attractions'):
		fn = "./Attractions/" + filename
		readJson(fn, 1)
	for filename in os.listdir('./Restaurants'):
		fn = "./Restaurants/" + filename
		readJson(fn, 2)

# ini buat bikin index dan load dari json pertama kali
# initbuild()

# PRINT TO CHECK
# ini buat debug aja
# f = open('output_index.json', 'w')
# print("====== JUMLAH TEMPAT ======\n")
# print(len(places))
# key_categories = categories_dict.keys()
# json.dump(key_categories, f)
# f.write("\n\n")
# json.dump(categories_dict, f)
# f.write("\n\n")
# json.dump(cities_dict, f)
# f.write("\n\n")
# json.dump(provinces_dict, f)
# f.close()
