from pandas import  read_excel
	

#resource tamame inha dar
def createtable():
    with sqlite3.connect('cmp.db3') as db:
        db.row_factory = sqlite3.Row
        db.execute(
        "CREATE TABLE IF NOT EXISTS cmp(" \
            "id INTEGER PRIMARY KEY," \
            "dec TEXT NOT NULL," \
            "pn TEXT NOT NULL," \
            "snf TEXT NOT NULL," \
            "snn TEXT NOT NULL);")
            
    db.commit()

def insert_excel_todb():
    with sqlite3.connect('cmp.db3') as db, \
        ExcelDocument('comptst.xlsx') as src:
        insert_template = "INSERT INTO cmp " \
         "(dec, pn, snf, snn) " \
         "VALUES (?, ?, ?, ?);"
            
        # Clear the database        
        # Load data from each Excel sheet into the database
    for sheet in src:
            try:
                db.executemany(insert_template, sheet.iter_rows())
            except sqlite3.Error as e:
                print(e)
                db.rollback()
            else:
                db.commit()
        
def show_data():
     # Check if all data have been loaded
    select_stmt = 'SELECT DISTINCT dec, pn FROM cmp;'
    for row in db.execute(select_stmt).fetchall():
            print(';'.join(row))
    db.close()


def delete():
    db = sqlite3.connect('cmp.db3')
    db.execute('DELETE FROM cmp;')

def test():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
    db.execute('DROP TABLE IF EXISTS test')
    db.execute('CREATE TABLE test(t1 text, i1 int)')

    db.execute('INSERT INTO test (t1, i1) VALUES (?, ?)', ('one', 1))
    db.execute('INSERT INTO test (t1, i1) VALUES (?, ?)', ('two', 2))
    db.execute('INSERT INTO test (t1, i1) VALUES (?, ?)', ('three', 3))
    db.execute('INSERT INTO test (t1, i1) VALUES (?, ?)', ('four', 4))
    db.execute('INSERT INTO test (t1, i1) VALUES (?, ?)', ('five', 5))

    db.commit()

    cursor = db.execute('SELECT * FROM test ORDER BY i1 ASC')
   
    for row in cursor:
        #print(row)
        #print(dict(row))
        #print(row['t1'])
        #print(row['i1'])
        print(row['t1'], row['i1'])
        
        #print(list(row))
        #print(tuple(row))
    db.close()
def tst_fetchone():
    with sqlite3.connect('cmp.db3') as db, \
        ExcelDocument('comptst.xlsx') as src:
        insert_template = "INSERT INTO cmp " \
         "(dec, pn, snf, snn) " \
         "VALUES (?, ?, ?, ?);"
            
        # Clear the database        
        # Load data from each Excel sheet into the database
    for sheet in src:
            try:
                db.executemany(insert_template, sheet.iter_rows())
            except sqlite3.Error as e:
                print(e)
                db.rollback()
            else:
                db.commit()
        

# http://www.projelecom.ir/2018/08/21/%D8%B4%D8%B1%D9%88%D8%B9-%D8%A8%D9%87-%D8%A7%D8%B3%D8%AA%D9%81%D8%A7%D8%AF%D9%87-%D8%A7%D8%B2-%DA%A9%D8%AA%D8%A7%D8%A8%D8%AE%D8%A7%D9%86%D9%87-numpy-%D8%AF%D8%B1-%D9%BE%D8%A7%DB%8C%D8%AA%D9%88%D9%86/ 
	X, Y = np.meshgrid(np.linspace(-1,1,10), np.linspace(-1,1,10))
	D = np.sqrt(X*X+Y*Y)
	sigma, mu = 1.0, 0.0
	G = np.exp(-( (D-mu)**2 / ( 2.0 * sigma**2 ) ) )
	print(G)
    query = 'SELECT dec, pn, snf FROM cmp ' \
        "WHERE snn='RS066';"
    curs = db.execute(query)
    row = curs.fetchone()
    print(','.join(row))
    #while row is not None:
        #print(','.join(row))
        #row = curs.fetchone()
    


createtable()
#insert_excel_todb()
tst_fetchone()
#readexcl()
=======
import numpy as np
df=read_excel('tst.xlsx',0)
tst=df.head()
sum_bedehkar=df['bedehkar'].sum()
print(tst)
print("sum_bedehkar is" ,sum_bedehkar)
min_bedehkar=np.min(df['bedehkar'])
print("min_bedehkar is ",min_bedehkar)
>>>>>>> origin/edare
