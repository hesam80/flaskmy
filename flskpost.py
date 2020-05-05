from flask import Flask, flash, redirect, render_template, request, url_for
import random
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import read_excel

#Create instance of Flask App
app = Flask(__name__)
 
#Define Route and Contant of that page
@app.route("/")
def indexx():
	

    return render_template("indexx.html")
 
#Define 2nd Route and Content
@app.route("/success", methods = ['POST'])
def success():	
  height=request.form["height"]
  vazn = request.form["vazn"]
  num=random.randint(1,12)
  return render_template('success.html', hit=height , number=num , vazn=vazn)
 
@app.route('/resultst')
def resultst():
	num=random.randint(1,12)
	return render_template('resultst.html', number=num)




#Running and Controlling the script
if (__name__ =="__main__"):
 app.run(debug=True)