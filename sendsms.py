from flask import Flask ,render_template, request, url_for, flash,session
import requests , random
from pandas import  read_excel
from numpy import *
import numpy as np
"""
inja khode kave neGAR CODE DADE
from kavenegar import *
api = KavenegarAPI('6E2F4F744E66394E474F4270484A56567A4A4F313662336B34726F4135766E646A47626C534A6C356B74593D')
params = { 'sender' : '1000596446', 'receptor': '09368663893', 'message' :'.وب سرویس پیام کوتاه کاوه نگار' }
response = api.sms_send( params)
"""

#API-KEY='6E2F4F744E66394E474F4270484A56567A4A4F313662336B34726F4135766E646A47626C534A6C356B74593D'
def send_sms(receptor,message):
	url = f'https://api.kavenegar.com/v1/6E2F4F744E66394E474F4270484A56567A4A4F313662336B34726F4135766E646A47626C534A6C356B74593D/sms/send.json'
	data={"message":message , "receptor":receptor}
	response=requests.post(url,data)
	print("message",message)

#send_sms('09368663893','HI DEAR')


app = Flask(__name__)

"""@app.route('/')
def view():
	df=read_excel('comptst.xlsx',0)
	ind=df.index
	date=df['date']
	mandeh = df['mandeh']

	num = random.randint(1,200)
	return render_template('tt.html',number=num,date=date , ind=ind , mandeh=mandeh)
	"""
@app.route('/')
def view():
	df=read_excel('comptst.xlsx',0)
	ind=df.index
	decprition=df['dec']
	part=df['pn']
	serof=df['snf']
	seron=df['snn']
	num=random.randint(1,300)
	
	a = np.arange(12).reshape((3,4))
	return render_template('tt.html',number=num, part=part, ind=ind , decprition=decprition , seron=seron, serof=serof, a=a)

# @app.route('/tst')
# def view():
# 	return "hi there"

if(__name__=="__main__"):
	app.run(debug=True)