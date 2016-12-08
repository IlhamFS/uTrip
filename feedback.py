# made
# relevance feedback if user download ittenary

import settings

# input : array of downloaded place id
# Update sum of download in 
def update_downloads(places_id):
    for i in places_id:
        place = settings.places[i]
        if place.get("feedback"):
            cmax = place["feedback"]["download"]
            cmax += 1
            settings.places[i]["feedback"]["download"] = cmax

            if cmax > settings.max_download:
                settings.max_download = cmax
        else:
            settings.places[i]["feedback"] = {"download": 1}
