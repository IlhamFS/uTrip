# made
# This class is used to read file json at the beginning
# Also to build index based on category and location

import json
import os

def get_places(place_ids):
    result = {"places": []}
    for i in place_ids:
        result["places"].append(places[i])
    return result


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
#       2 -> restaurants
def read_json(filename, type):
    # load all json into temporary variable data
    with open(filename) as data_file:
        data = json.load(data_file)
    data_file.close()

    idx = len(places)

    for i in range(len(data["places"])):
        place = data["places"][i]
        name = place["name"]

        if name:
            is_new = 1

            # check if place already exist
            if name_ids.get(name):
                for j in range(len(name_ids[name])):
                    if place["location"][0] == name_ids[name][j]["location"]:
                        is_new = 0
                if is_new:
                    name_ids[name].append({"location": place["location"][0], "index": idx})
            else:
                name_ids[name] = [{"location": place["location"][0], "index": idx}]

            if is_new:
                # insert new place into array
                places.append(place)

                # update max review
                if (place["review"]):
                    crev = int(place["review"])
                    global max_review
                    if (crev > max_review):
                        max_review = crev
                else:
                    place["review"] = "0"

                # fix rate
                if not place["rate"]:
                    place["rate"] = "0.0"

                # create index categories
                if type == 1: 
                    create_index_attractions(place, idx)
                elif type == 2:
                    create_index_restaurants(place, idx)

                # create index location
                create_index_location(place, idx)

                idx += 1

# run this at the beginning in main program
def init_build(): 
    # define global variable 
    global places 
    global categories_dict
    global cities_dict
    global provinces_dict
    global name_ids
    global max_review
    global max_download

    # init global variable
    places = []
    categories_dict = {}
    cities_dict = {}
    provinces_dict = {}
    name_ids = {}
    max_review = 1
    max_download = 1

    # add category restaurant & halal here
    categories_dict["restaurant"] = []
    categories_dict["halal"] = []
    
    # read all files, save it, and create index
    for filename in os.listdir('./Attractions'):
        fn = "./Attractions/" + filename
        read_json(fn, 1)
    for filename in os.listdir('./Restaurants'):
        fn = "./Restaurants/" + filename
        read_json(fn, 2)
