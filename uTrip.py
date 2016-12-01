from flask import Flask
from flask import render_template
import json

app = Flask(__name__)


@app.route('/')
def main():
    with open('static/json/places.json') as data_file:
        data = json.load(data_file)
    return render_template('index.html', data=data)

def get_query_result(location, category, start_hour, end_hour)
    with open('static/json/places.json') as data_file:
        data = json.load(data_file)
        id_places = []
        places = data["places"]
        result_places = []
        for category in data["categories"]:
            if category["name"] == location:
                id_places = category["id_palces"]
        for id_place in id_places:
            open_time = places[id_place]["time"]["open"]
            close_time = places[id_place]["time"]["close"]


if __name__ == '__main__':
    app.run()
