from flask import Flask, render_template, request, session, jsonify
from query_expansion import query_expansion
from ItineraryGenerator import generate_itinerary
from query import get_query_result
from settings import json, init_build, get_places
from sorting import sort_all
import settings
import numpy as np

init_build()

# Application
app = Flask(__name__)



@app.route('/')
def main():
    # destroy session
    session.pop('open_time', None)
    session.pop('close_time', None)
    session.pop('search_result', None)
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    par = request.form['json_str']
    (place, categories, open_time, close_time) = query_expansion(par)

    # destroy session
    session.pop('open_time', None)
    session.pop('close_time', None)
    session.pop('search_result', None)

    if (open_time == ""):
        open_time = "10.00"
    if (close_time == ""):
        close_time = "17.00"

    # create session
    session['open_time'] = open_time
    session['close_time'] = close_time

    # dilanjutkan dengan pencarian kode feti
    query_result = get_query_result(place, categories, open_time, close_time)

    # olah data nya dulu disini
    sorted_query = sort_all(query_result)
    data = get_places(sorted_query)

    session['search_result'] = data
    return json.dumps(data)


@app.route('/itinerary', methods=['POST'])
def itinerary():
    par = json.loads(request.form['json_str'])
    # ambil recommendation attraction dan resto dari setiap par

    data = session['search_result']
    ot = session['open_time']
    ct = session['close_time']

    itin = generate_itinerary(ot, ct, data, par)
    return json.dumps(itin)


@app.route('/submit_itinerary', methods=['POST'])
def submit_itinerary():
    par = request.form['json_str']

    # olah data nya dulu disini

    return render_template('index.html')


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    data = list(settings.cities_dict) + list(settings.provinces_dict)
    results = np.array([x for x in data if str(search).lower() in x.lower()])
    results = list(results[:5])
    return jsonify(matching_results=results)


if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'  
    app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    app.run(host='0.0.0.0')
