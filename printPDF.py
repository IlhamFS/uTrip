import pdfkit

def create(data):
    try:
        config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
        
        appendHtml = "<!DOCTYPE html><html lang=\"en\" xmlns=\"http://www.w3.org/1999/xhtml\"><head><meta charset=\"utf-8\" /><title>uTrip</title>  <link rel=\"stylesheet\" type=\"text/css\" href=\"{{ url_for('static', filename='css/bootstrap.css') }}\"/><link rel=\"stylesheet\" type=\"text/css\" href=\"{{ url_for('static', filename='css/stylesheet.css') }}\" /><link href=\"https://fonts.googleapis.com/css?family=Lobster\" rel=\"stylesheet\"><link href=\"https://fonts.googleapis.com/css?family=Ubuntu\" rel=\"stylesheet\"><script type=\"text/javascript\" src=\"{{ url_for('static', filename='js/jquery-1.12.3.js') }}\"></script><script type=\"text/javascript\" src=\"{{ url_for('static', filename='js/bootstrap.min.js') }}\"></script><script type=\"text/javascript\" src=\"{{ url_for('static', filename='js/typed.js') }}\"></script><script type=\"text/javascript\" src=\"{{ url_for('static', filename='js/my-js.js') }}\"></script></head><body><div><div><div><br><br><br><br><br><div align = \"center\"><img  id=\"logo-in-modal\" alt=\"Brand\" src=\"http://ilhamfathy.me/static/img/utrip.png\"><br><h4 id=\"myModalLabel\">Your Itinerary</h4></div><div class=\"modal-body\"><table id=\"itinerary-result\" class=\"result-table table table-bordered table-striped table-hover\"><tr class=\"itinerary-template\"><td class=\"itinerary-time col-md-2\"><b>Time</b></td><td class=\"itinerary-location col-md-3\"><b>Location</b></td><td class=\"itinerary-address col-md-5\"><b>Address</b></td></td><td class=\"itinerary-address col-md-1\"><b>Google Maps</b></td></tr>"
        for i in data:
          appendHtml += "<tr class=\"itinerary-template\">"
          appendHtml += "<td class=\"itinerary-location col-md-5\"><center>"
          appendHtml += i['time']
          appendHtml += "</center></td>"
          appendHtml += "<td class=\"itinerary-location col-md-3\">"
          appendHtml += i['location']
          appendHtml += "</td>"
          appendHtml += "<td class=\"itinerary-address col-md-5\">"

          address = i['address']
          appendHtml += address
          appendHtml += "</td>"

          appendHtml += "<td class=\"itinerary-direction col-md-1\">"

          if len(address) != 0:
            if "near"  not in address: 
              appendHtml += "<center><a href=\"https://www.google.com/maps/dir/here/"+address+"\">Here</a></center>";

          appendHtml += "</td>"      
          appendHtml += "</tr>"

        appendHtml +="</table><div align = \"center\"><h5>Enjoy your trip!</h5></div></div></div></div></div></body></html>"

        options = {'orientation': 'Landscape'}
        css = ['static/css/bootstrap.css', 'static/css/stylesheet.css']
        pdfkit.from_string(appendHtml, 'itinerary.pdf', options = options, css=css, configuration=config) #with --page-size=Legal and --orientation=Landscape
        pdfkit.from_string(appendHtml, './static/pdf/itinerary.pdf', options = options, css=css, configuration=config) #with --page-size=Legal and --orientation=Landscape
    
    except:
            print("error occured")
            sys.exit(0)