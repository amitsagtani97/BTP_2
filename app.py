import json
import urllib.request
#from geojson import Feature, Point

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


lat = 45.78
lon = 76.80

@app.route('/') 
def hello_world(): 
	global lat
	global lon
	var = {"geometry": {"type": "Point", "coordinates": [lat, lon]}, "type": "Feature", "properties": {}}
	
	#my_point = Point((-3.68, 40.41))
	#return var


	# contents = urllib.request.urlopen("https://wanderdrone.appspot.com/").read()
	# print(contents)
	# return contents
	print(var)
	return var


@app.route('/send',methods=['POST','GET'])
def config():
#   Retrieves the configurations available in the database at present.
    if request.method=='POST':
        global lat
        global lon
        lat=request.args.get('lat')
        lon=request.args.get('long')
        print(lat)
        print(lon)
        return "data updated!"
# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run() 