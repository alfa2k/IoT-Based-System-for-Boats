from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from sense_hat import SenseHat
import time

sense = SenseHat()

app = Flask(__name__)
socketio = SocketIO(app)

# Define a route to render the template with the graph
@app.route('/')
def home():
    return render_template('graphs.html')

# Define a function to read sensor data and emit it to the client
def get_sensor_data():
    while True:
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        emit('sensor_data', {'temperature': temperature, 'humidity': humidity, 'pressure': pressure}, broadcast=True)
        time.sleep(1)

# Start the Flask-SocketIO server
if __name__ == '__main__':
    socketio.start_background_task(get_sensor_data)
    socketio.run(app, debug=True)