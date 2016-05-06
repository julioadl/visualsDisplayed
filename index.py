from flask import Flask, render_template, request, redirect, url_for, make_response
import json
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    data = json.load(open('dta.json'))
    return json.dumps(data)

@app.route('/nikko')
def chord():
    return render_template('nikko_analysis.html')

if __name__ == '__main__':
    app.run(debug = True)
