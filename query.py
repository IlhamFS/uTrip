# feti
# modified made: 2016-12-5


import settings

# input : String location, List of String categories, integer start_hour, integer end_hour
# output: dictionary of array index places, keys String category
def get_query_result(location, categories, start_hour, end_hour):
    results = {};
    for category in categories:
        result_places = []
        query_category = settings.categories_dict[category]
        if location in settings.provinces_dict:
            query_places = settings.provinces_dict[location]
        else:
            query_places = settings.cities_dict[location]
        id_places = list(set(query_places) & set(query_category))
        for id_place in id_places:
            place = settings.places[id_place]
            open_time = place["time"][0]["open"]
            close_time = place["time"][0]["close"]
            if not (start_hour >= close_time or end_hour <= open_time):
                result_places.append(id_place)
        results[category] = result_places
    return results;
