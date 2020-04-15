
#Import dependencies
from flask import Flask, flash, redirect, render_template, request, url_for
from factoriel import factoriel
from pprint import pprint as pp


#Create instance of Flask App
app = Flask(__name__)

#Define Route
@app.route("/")

#Content

#def home():
#    return("hello world ")
def index():
	return render_template (
		'weather.html', data = [{'name':'Toronto'},{'name':'Montreal'}, {'name':'Calgary'},
{'name':'Ottawa'}, {'name':'Edmonton'}, {'name':'Mississauga'},
{'name':'Winnipeg'}, {'name':'Vancouver'}, {'name':'Brampton'},
{'name':'Quebec'}])

@app.route("/result" , methods=['GET' , 'POST'])
def result():
	data=[]
	error= None
	select = request.form.get('comp_select')
	resp = query_api(select)
	pp(resp)
	if resp:
		data.append(resp)
	if len(data)!=2 :
		error = 'Bad Response from weather API'
	return render_template(
		'result.html', data=data, error=error)
	


#Running and Controlling the script
if (__name__ =="__main__"):
    app.run(debug=True)