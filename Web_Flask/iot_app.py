from flask import Flask, render_template, jsonify
import serial
import pynmea2
import folium



app = Flask(__name__)
port="/dev/ttyAMA0"
ser=serial.Serial(port, baudrate=9600, timeout=0.5)

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/get_gps')
def get_gps():
    try:
        line = ser.readline().decode('unicode_escape')
        msg = pynmea2.parse(line)
        
        if hasattr(msg,'latitude') and hasattr(msg, 'longitude'):
            lat = msg.latitude
            lon = msg.longitude
            return {'latitude':lat, 'longitude':lon}
        else:
            return {'latitude':None, 'longitude':None}
    
    except Exception as e:
        print(f'Error: {e}')
        return {'latitude':None, 'longitude':None}

if __name__ == '__main__':
    app.run(debug=True)
    