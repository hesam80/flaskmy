from flask import Flask ,render_template, request, url_for, flash,session
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas import read_excel 



# mohtava = sheet.cell_value(0, 2)
# esm = sheet.cell_value(1, 1)
# famil = sheet.cell_value(1, 2)
app=Flask(__name__)
# datas={"mohtava":mohtava, "esm":esm, "famil":famil }
# for s in sheet :
#   datats

# print(datats[0])
# for i in range(1,7):
#  datats=sheet.cell_value(i,4)


# Define Route and Contant of that page
@app.route("/")
def excel():
	
    df= pd.read_excel('tst.xlsx',0) 

   # return render_template('excelpd.html',sheet=sheet , sotoon=sotoon)
   return f"mandeh {df['mandeh']}"

# @app.route("/l")
# def excell():
	
# 	return render_template('layout.html', datats=datats)

# @app.route('/logout')
# def logout():
#     # remove the username from the session if it's there
#     session.pop('username', None)
#     return redirect(url_for('index'))


if (__name__ =="__main__"):
  app.run(debug=True)