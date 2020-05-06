from pandas import  read_excel
import pandas as pd
from exceldoc import *
import sqlite3
import xlrd
import os.path

def readexcl():
    df=pd.read_excel('comptst.xlsx',0)
    ind=df.index
    decprition=df['dec']
    part=df['pn']
    serof=df['snf']
    seron=df['snn']

    for i in df.index:
    #print("To iterate over the list we can use a loop:",df['mandeh'][i])
	    print(';', decprition[i])
	

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
