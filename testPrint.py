import pdfkit
import os
from flask import Flask, url_for
import sys


def print_pdf(par):
	body = """
	<html>
	<head>
	<meta name="pdfkit-page-size" content="Legal"/>
	<meta name="pdfkit-orientation" content="Landscape"/>
	</head>
	Hello World!
	</html>
	"""
	#os.system("wkhtmltopdf http://google.com pleasegoogle3.pdf")

	#filePath = url_for('static', filename='pdf/itinerary.pdf')
	#filePath = 'static/pdf/itinerary.pdf'
	#os.system("echo " + filePath)
	#config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
	#pdfkit.from_string(body, filePath) #with --page-size=Legal and --orientation=Landscape

def create():
    print("creating new  file")
    name="testingFile"
    extension="txt"
    try:
        name=name+"."+extension
        file=open(name,'a')
        file.close()
        config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
        pdfkit.from_url('http://google.com', 'COBA1.pdf', configuration=config)
        body = """<html><link rel="stylesheet" type="text/css\" href="{{ url_for('static', filename='css/bootstrap.css') }}\"/><link rel="stylesheet\" type="text/css\" href="{{ url_for('static', filename='css/stylesheet.css') }}\" /><link href="https://fonts.googleapis.com/css?family=Lobster\" rel="stylesheet\"><link href="https://fonts.googleapis.com/css?family=Ubuntu\" rel="stylesheet\"><script type="text/javascript\" src="{{ url_for('static', filename='js/jquery-1.12.3.js') }}\"></script><script type="text/javascript\" src="{{ url_for('static', filename='js/bootstrap.min.js') }}\"></script><script type="text/javascript\" src="{{ url_for('static', filename='js/typed.js') }}\"></script><script type="text/javascript\" src="{{ url_for('static', filename='js/my-js.js') }}\"></script></head><body><div><div><div><br><br><br><br><br><div align = \"center\"><img  id="logo-in-modal\" alt="Brand\" src="http://ilhamfathy.me/static/img/utrip.png\"><br><h4 id="myModalLabel\">Your Itinerary</h4></div><div class="modal-body\"><table id="itinerary-result\" class="result-table table table-bordered table-striped table-hover\"><tr class="itinerary-template\"><td class="itinerary-time col-md-2\"><b>Time</b></td><td class="itinerary-location col-md-3\"><b>Location</b></td><td class="itinerary-address col-md-5\"><b>Address</b></td></td><td class="itinerary-address col-md-1"><b>Google Maps</b></td></tr></table><div align = "center"><h5>Enjoy your trip!</h5></div></div></div></div></div></body></html>"""
        options = {'orientation': 'Landscape'}
      	css = ['static/css/bootstrap.css', 'static/css/stylesheet.css']
      	pdfkit.from_string(body, 'COBA2.pdf', options = options, css=css, configuration=config) #with --page-size=Legal and --orientation=Landscape
    except:
            print("error occured")
            sys.exit(0)

