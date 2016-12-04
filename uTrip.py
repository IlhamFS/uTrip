from flask import Flask
from flask import render_template
import json
import os

places = []
categories_dict = {}
cities_dict = {}
provinces_dict = {}


def create_index_location(place, idx):
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


def create_index_attractions(place, idx):
    # update index categories
    ctgs = place["categories"]
    for j in range(len(ctgs)):
        ctg = ctgs[j]
        if ctg in categories_dict:
            categories_dict[ctg].append(idx)
        else:
            categories_dict[ctg] = [idx]


def create_index_restaurants(place, idx):
    # update index categories
    categories_dict["restaurant"].append(idx)
    ctg = place["categories"][0]
    if "halal" in ctg.lower():
        categories_dict["halal"].append(idx)


# type: 1 -> attractions;
# 		2 -> restaurants
def read_json(filename, type):
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
            if type == 1:
                create_index_attractions(place, idx)
            elif type == 2:
                create_index_restaurants(place, idx)
            # create index location
                create_index_location(place, idx)
            idx += 1


# MAIN PROGRAM
# saat program pertama running, jalankan ini
def init_build():
    # lanjut tambahin restaurant & halal disini
    categories_dict["restaurant"] = []
    categories_dict["halal"] = []
    for filename in os.listdir('./Attractions'):
        fn = "./Attractions/" + filename
        read_json(fn, 1)
    for filename in os.listdir('./Restaurants'):
        fn = "./Restaurants/" + filename
        read_json(fn, 2)


# ini buat bikin index dan load dari json pertama kali
init_build()

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


def get_query_result(location, category, start_hour, end_hour):
    result_places = []
    query_category = categories_dict[category]
    if location in provinces_dict:
        query_places = provinces_dict[location]
    else:
        query_places = cities_dict[location]
    id_places = list(set(query_places) & set(query_category))
    for id_place in id_places:
        place = places[id_place]
        open_time = place["time"][0]["open"]
        close_time = place["time"][0]["close"]
        if not (start_hour >= close_time or end_hour <= open_time):
            result_places.append(place)
    return result_places

# Debug query
# result = get_query_result("Lampung", "Monuments & Statues", 10, 20)
# print result

# Application
app = Flask(__name__)


@app.route('/')
def main():
    with open('static/json/places.json') as data_file:
        data = json.load(data_file)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
