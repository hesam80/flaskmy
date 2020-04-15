from flask import Flask, flash, redirect, render_template, request, url_for
import random
app = Flask(__name__)

@app.route("/")
def hroot():
	return "this is root path"

@app.route("/index")

def index():
	return render_template (
		'index.html')

@app.route("/index<path>")
def hell(path):
	num = 2
	return f"hiogujg {path}ghjjjjjjf{num}"

@app.route("/weather")

def weather():
	return render_template (
		'weather.html')

@app.route('/result')
def result():
	return render_template('result.html')

@app.route('/resultst')
def resultst():
	num=random.randint(1,12)
	return render_template('resultst.html', number=num)

if (__name__ =="__main__"):
    app.run(debug=True)
