from flask import Flask, render_template, request, jsonify, flash
import qrcode
from environs import Env

env = Env()
env.read_env()

app = Flask(__name__)
app.secret_key=env.str("SECRET_KEY")

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/api/get', methods=['GET'])
def get_data():
    data = {
        "name": "User",
        "age": 19,
        "email": "john@example.com"
    }
    return jsonify(data)

@app.route('/api/post', methods=['POST', 'GET'])
def add_data():
    if request.method=='POST':
        data = request.get_json()
        return jsonify(data)
    else: 
        return "Something went wrong!"

@app.route('/qrcode', methods=['POST', 'GET'])
def generate_qrcode():
    if request.method=='POST':
        url = request.form.get('url')
        img = qrcode.make(url)
        img.save('static/image/result.png')
        flash(message="Success. Thank you!!!", category='info')
    return render_template('form.html')


if __name__=="__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)