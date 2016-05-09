from flask import Flask, render_template, request, redirect, url_for, make_response
import json
import urllib

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/us-elections2016-1')
def usElections1():
    return render_template('us-elections-1.html')

@app.route('/us-elections2016-2')
def usElections2():
    return render_template('us-elections-2.html')

@app.route('/us-elections2016-3')
def usElections3():
    return render_template('us-elections-3.html')

@app.route('/us-elections2016-4')
def usElections4():
    return render_template('us-elections-4.html')

@app.route('/data')
def data():
    data = json.load(open('dta.json'))
    return json.dumps(data)

@app.route('/nikko')
def chord():
    return render_template('nikko_analysis.html')

if __name__ == '__main__':
    app.run(debug = True)
