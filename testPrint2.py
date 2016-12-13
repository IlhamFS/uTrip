import pdfkit

body = """
    <html><link rel="stylesheet" type="text/css\" href="{{ url_for('static', filename='css/bootstrap.css') }}\"/><link rel="stylesheet\" type="text/css\" href="{{ url_for('static', filename='css/stylesheet.css') }}\" /><link href="https://fonts.googleapis.com/css?family=Lobster\" rel="stylesheet\"><link href="https://fonts.googleapis.com/css?family=Ubuntu\" rel="stylesheet\"><script type="text/javascript\" src="{{ url_for('static', filename='js/jquery-1.12.3.js') }}\"></script><script type="text/javascript\" src="{{ url_for('static', filename='js/bootstrap.min.js') }}\"></script><script type="text/javascript\" src="{{ url_for('static', filename='js/typed.js') }}\"></script><script type="text/javascript\" src="{{ url_for('static', filename='js/my-js.js') }}\"></script></head><body><div><div><div><br><br><br><br><br><div align = \"center\"><img  id="logo-in-modal\" alt="Brand\" src="http://ilhamfathy.me/static/img/utrip.png\"><br><h4 id="myModalLabel\">Your Itinerary</h4></div><div class="modal-body\"><table id="itinerary-result\" class="result-table table table-bordered table-striped table-hover\"><tr class="itinerary-template\"><td class="itinerary-time col-md-2\"><b>Time</b></td><td class="itinerary-location col-md-3\"><b>Location</b></td><td class="itinerary-address col-md-5\"><b>Address</b></td></td><td class="itinerary-address col-md-1"><b>Google Maps</b></td></tr></table><div align = "center"><h5>Enjoy your trip!</h5></div></div></div></div></div></body></html>
    """

options = {
    'zoom':'15',
    'orientation': 'Landscape',
  	}

css = ['static/css/bootstrap.css', 'static/css/stylesheet.css']  

pdfkit.from_string(body, 'static/pdf/please.pdf', options = options, css=css) #with --page-size=Legal and --orientation=Landscape
