from flask import Flask
from flask import render_template
import json
app = Flask(__name__)


@app.route('/')
def main():
    with open('static/json/places.json') as data_file:
        data = json.load(data_file)
    return render_template('index.html', data = data)


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



if __name__ == '__main__':
   app.run()
