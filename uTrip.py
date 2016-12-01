from flask import Flask
from flask import render_template
import json
app = Flask(__name__)


@app.route('/')
def main():
    with open('static/json/places.json') as data_file:
        data = json.load(data_file)
    return render_template('index.html', data = data)

if __name__ == '__main__':
   app.run()
