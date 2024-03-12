from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/live_location')
def live_location():
    return render_template('live-location.html')

@app.route('/live_camera')
def live_camera():
    return render_template('live-cameras.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
