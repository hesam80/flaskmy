from pandas import  read_excel
def readexcl():
	df=read_excel('tst.xlsx',0)
#print(df)
	date=df['date']

	for i in df.index:
    #print("To iterate over the list we can use a loop:",df['mandeh'][i])
		print(date[i])
	df=read_excel('comptst.xlsx',0)
	ind=df.index
	decprition=df['dec']
	part=df['pn']
	serof=df['snf']
	seron=df['snn']

def createtable():
    with sqlite3.connect('cmp.db3') as db:
        db.execute(
        "CREATE TABLE IF NOT EXISTS cmp(" \
            "id INTEGER PRIMARY KEY," \
            "dec TEXT NOT NULL," \
            "pn TEXT NOT NULL," \
            "snf TEXT NOT NULL," \
            "snn TEXT NOT NULL);")
            
    db.commit()

createtable()