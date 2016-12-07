from flask import Flask, render_template, request, session
from query_expansion import query_expansion
from ItineraryGenerator import generate_itinerary
from query import get_query_result
import json

# Application
app = Flask(__name__)


@app.route('/')
def main():
  #destroy session
  session.pop('open_time', None)
  session.pop('close_time', None)
  session.pop('search_result', None)
  return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
  par = request.form['json_str']
  (place, categories, open_time, close_time) = query_expansion(par)
  print categories  

  #destroy session
  session.pop('open_time', None)
  session.pop('close_time', None)
  session.pop('search_result', None)

  #create session   
  session['open_time'] = open_time
  session['close_time'] = close_time
  if (open_time == ""):
    session['open_time'] = "10.00"
  if (close_time == ""):
    session['close_time'] = "17.00"


  #dilanjutkan dengan pencarian kode feti

  #olah data nya dulu disini
  with open('static/json/places.json') as data_file:
    data = json.load(data_file)

  session['search_result'] = data
  return json.dumps(data)


@app.route('/itinerary', methods=['POST'])
def itinerary():
  par = json.loads(request.form['json_str'])
  #ambil recommendation attraction dan resto dari setiap par
  
  data = session['search_result']
  ot = session['open_time']
  ct = session['close_time']

  itin =generate_itinerary(ot, ct, data, par)
  return json.dumps(itin)


@app.route('/submit_itinerary', methods=['POST'])
def submit_itinerary():
  par = request.form['json_str']

  #olah data nya dulu disini

  return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host='0.0.0.0')
