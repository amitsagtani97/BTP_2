import json
import urllib.request
#from geojson import Feature, Point

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/') 
def hello_world(): 
	var = '{"geometry": {"type": "Point", "coordinates": [-118.244, 34.0544779]}, "type": "Feature", "properties": {}}'
	
	#my_point = Point((-3.68, 40.41))
	#return var


	contents = urllib.request.urlopen("https://wanderdrone.appspot.com/").read()
	print(contents)
	return contents
  
# main driver function 
if __name__ == '__main__': 
  
    # run() method of Flask class runs the application  
    # on the local development server. 
    app.run() 