from flask import Flask
from flask import render_template
import json

app = Flask(__name__)


@app.route('/')
def main():
    with open('static/json/places.json') as data_file:
        data = json.load(data_file)
    return render_template('index.html', data=data)

def get_query_result(location, category, start_hour, end_hour):
    with open('static/json/places.json') as data_file:
        data = json.load(data_file)
        id_places = []
        places = data["places"]
        result_places = []
        for categories in data["categories"]:
            if category in categories:
                id_places = category["id_places"]
        for id_place in id_places:
            open_time = places[id_place]["time"]["open"]
            close_time = places[id_place]["time"]["close"]
            locations = places[id_place]["location"]
            if locations["island"] == location or locations["province"] == location or locations["city"] == location or locations["address"] == location:
                if not (start_hour > close_time or end_hour < open_time):
                    result_places.append(places[id_place])
        return result_places


if __name__ == '__main__':
    app.run(host='0.0.0.0')
