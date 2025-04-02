from flask import Flask, request, jsonify, render_template, url_for
from flask_cors import CORS
import pytz
from datetime import datetime
import requests
import os
from dotenv import load_dotenv
import markdown

load_dotenv()

app = Flask(__name__)
CORS(app)

# You'll need to get a free API key from timezonedb.com
TIMEZONEDB_API_KEY = os.getenv('TIMEZONEDB_API_KEY')
GEONAMES_USER_ID = os.getenv('GEONAMES_USER_ID')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/api/time', methods=['GET'])
def get_city_time():
    city = request.args.get('city')
    print(f"City : {city}")
    
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    try:
        # First, geocode the city to get its coordinates
        geocode_url = f"http://api.geonames.org/searchJSON?q={city}&maxRows=1&username={GEONAMES_USER_ID}"
        geo_response = requests.get(geocode_url)
        geo_data = geo_response.json()
        
        
        if not geo_data:
            return jsonify({'error': 'City not found'}), 404

         
        lat = geo_data['geonames'][0]['lat']
        lng = geo_data['geonames'][0]['lng']

        

        # print(f"Lat : {lat}, Long : {lng}")
        
        # Get timezone information
        timezone_url = f"http://api.timezonedb.com/v2.1/get-time-zone?key={TIMEZONEDB_API_KEY}&format=json&by=position&lat={lat}&lng={lng}"
        timezone_response = requests.get(timezone_url)
        print(f"Timezone response: {timezone_response}")
        timezone_data = timezone_response.json()
        
        if timezone_data['status'] != 'OK':
            return jsonify({'error': 'Timezone not found'}), 404
            
        timezone_name = timezone_data['zoneName']
        current_time = datetime.now(pytz.timezone(timezone_name))
        
        return jsonify({
            'city': city,
            'timezone': timezone_name,
            'current_time': current_time.strftime('%Y-%m-%d %H:%M:%S'),
            'timezone_offset': timezone_data['gmtOffset'],
            'abbreviation': timezone_data['abbreviation'],
            'formatted': f"{current_time.strftime('%H:%M:%S')} ({timezone_data['abbreviation']})"
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)