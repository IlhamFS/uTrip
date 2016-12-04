import json


def get_query_result(location, categories, start_hour, end_hour):
    results = {};
    for category in categories:
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
                result_places.append(id_place)
        results[category] = result_places
    return results;

result = get_query_result("Manado", "Bridges", 10, 12)
for r in result:
    print r["name"]


