# made
# relevance feedback if user download ittenary

import settings
import json

# input : array of downloaded place id
# Update sum of download in 
def update_downloads(pid):
    place = settings.places[pid]
    if place.get("feedback"):
        cmax = place["feedback"]["download"]
        cmax += 1
        settings.places[pid]["feedback"]["download"] = cmax

        if cmax > settings.max_download:
            settings.max_download = cmax
    else:
        settings.places[pid]["feedback"] = {"download": 1}

def give_feedback(par):

    for plc in par:
        if settings.name_ids.get(plc["location"]):
            aloc = settings.name_ids[plc["location"]]
            for loc in aloc:
                ceklocation = loc["location"]["address"]+" "+loc["location"]["city"]+" "+loc["location"]["province"]+" "+loc["location"]["island"]
                if ceklocation == plc["address"]:
                    update_downloads(loc["index"])
                    print ("[CHECK] Update " + plc["location"])
                    # print (settings.places[loc["index"]])
