from flask import Flask, render_template, request
from query_expansion import query_expansion
from query import get_query_result
import json

# Application
app = Flask(__name__)


@app.route('/')
def main():
    with open('static/json/places.json') as data_file:
        data = json.load(data_file)
    return render_template('index.html', data=data)


@app.route('/search', methods=['POST'])
def search():
  #print request.form['json_str']
  par = request.form['json_str']
  (place, categories, open_time, close_time) = query_expansion(par)
  print categories

  #dilanjutkan dengan pencarian kode feti

  #olah data nya dulu disini
  with open('static/json/places.json') as data_file:
    data = json.load(data_file)
  return json.dumps(data)


@app.route('/itinerary', methods=['POST'])
def itinerary():
  #print request.form['json_str']
  par = request.form['json_str']

  #olah data nya dulu disini

  with open('static/json/itinerary.json') as data_file:
    data = json.load(data_file)
  return json.dumps(data)


@app.route('/submit_itinerary', methods=['POST'])
def submit_itinerary():
  #print request.form['json_str']
  par = request.form['json_str']

  #olah data nya dulu disini

  return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
