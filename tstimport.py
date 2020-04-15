from flask import Flask ,render_template, request, url_for, flash,session
import xlrd 


loc = ('dabiraan aval.xlsx') 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)
mohtava = sheet.cell_value(0, 2)
esm = sheet.cell_value(1, 1)
famil = sheet.cell_value(1, 2)
app=Flask(__name__)
datas={"mohtava":mohtava, "esm":esm, "famil":famil }




for i in range(1,7):
 datats=sheet.cell_value(i,4)

print(datats[1])
#Define Route and Contant of that page
@app.route("/")
def excel():
	
	return render_template('excel.html',datas=datas, mohtava=mohtava, esm=esm, famil=famil)
@app.route("/l")
def excell():
	
	return render_template('layout.html', datats=datats)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if (__name__ =="__main__"):
 app.run(debug=True)