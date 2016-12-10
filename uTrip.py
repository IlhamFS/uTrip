from flask import Flask, render_template, request, jsonify
from query_expansion import query_expansion
from ItineraryGenerator import generate_itinerary
from query import get_query_result
from settings import json, init_build, get_places
from sorting import sort_all
<<<<<<< a40534b6fe46f0d78a5aa3ce9018083fb853b5d8
from feedback import give_feedback
=======
from printPDF import print_pdf
>>>>>>> download, waiting for abs download path
import settings
import numpy as np

init_build()

# Application
app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    par = request.form['json_str']
    par = par.replace("%3A", ".")
    (place, categories, open_time, close_time) = query_expansion(par)

    if (open_time == ""):
        open_time = "10.00"
    if (close_time == ""):
        close_time = "17.00"
    if place != "":
    # dilanjutkan dengan pencarian kode feti
        query_result = get_query_result(place, categories, open_time, close_time)

        # olah data nya dulu disini
        sorted_query = sort_all(query_result)
        data = get_places(sorted_query)
    else:
        data = {"places": []}

    return json.dumps({'data': data, 'open': open_time, 'close': close_time})


@app.route('/itinerary', methods=['POST'])
def itinerary():
    par = json.loads(request.form['json_str'])
    # ambil recommendation attraction dan resto dari setiap par

    data = json.loads(request.form['values'])
    ot = request.form['open']
    ct = request.form['close']

    itin = generate_itinerary(ot, ct, data, par)
    return json.dumps(itin)


@app.route('/submit_itinerary', methods=['POST'])
def submit_itinerary():
    par = json.loads(request.form['json_str'])

    # give_feedback
    give_feedback(par)

    # print pdf
    try:
        print_pdf(par) 

    except Exception:
        pass

    return render_template('index.html')


@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('q')
    data = list(settings.cities_dict) + list(settings.provinces_dict)
    results = np.array([x for x in data if str(search).lower() in x.lower()])
    results = list(results[:5])
    return jsonify(matching_results=results)


if __name__ == '__main__':
    app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    app.run(host='0.0.0.0')
