from flask import Flask, render_template, request, session
from query_expansion import query_expansion
from query import get_query_result
from settings import json

# Application
app = Flask(__name__)


@app.route('/')
def main():
  return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
  par = request.form['json_str']
  (place, categories, open_time, close_time) = query_expansion(par)
  print categories  
  
  #create session 
  session['open_time'] = open_time
  session['close_time'] = close_time

  #dilanjutkan dengan pencarian kode feti

  #olah data nya dulu disini
  with open('static/json/places.json') as data_file:
    data = json.load(data_file)

  session['search_result'] = data
  return json.dumps(data)


@app.route('/itinerary', methods=['POST'])
def itinerary():
  par = request.form['json_str']

  #olah data nya dulu disini

  with open('static/json/itinerary.json') as data_file:
    data = json.load(data_file)
  return json.dumps(data)


@app.route('/submit_itinerary', methods=['POST'])
def submit_itinerary():
  par = request.form['json_str']

  #olah data nya dulu disini

  #destroy session
  session.pop('open_time', None)
  session.pop('close_time', None)
  session.pop('search_result', None)
  return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host='0.0.0.0')
