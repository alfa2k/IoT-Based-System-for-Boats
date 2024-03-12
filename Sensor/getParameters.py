from sense_hat import SenseHat

sense = SenseHat()

temperature = sense.get_temperature()
humidity = sense.get_humidity()
pressure = sense.get_pressure()

message = "Temp: {:.2f}C Humidity: {:.2f}% Pressure: {:.2f}hPa".format(temperature, humidity, pressure)

sense.show_message(message)