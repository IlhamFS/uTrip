import json


def get_query_result(location, category, start_hour, end_hour):
    with open('static/json/places.json') as data_file:
        data = json.load(data_file)
        id_places = []
        places = data["places"]
        result_places = []
        for categories in data["categories"]:
            if categories["name"] == category:
                id_places = categories["id_places"]
                break
        for id_place in id_places:
            place = places[id_place]
            open_time = place["time"][0]["open"]
            close_time = place["time"][0]["close"]
            locations = place["location"]
            if locations[0]["island"] == location or locations[0]["province"] == location or locations[0]["city"] == location or locations[0]["address"] == location:
                if not (start_hour >= close_time or end_hour <= open_time):
                    result_places.append(place)
        return result_places


result = get_query_result("Manado", "Bridges", 10, 12)
for r in result:
    print r["name"]


