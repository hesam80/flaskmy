import pandas as pd
from exceldoc import *
import sqlite3
import xlrd
import os.path
def display_menu():
    selected = input(f"""which task number select
    if select 1 read_from_excel run
    if select 2 length run
    if select 3 tstregex

    """)
    print("select Number is:",selected)
    if selected == "1":
        excelfilename = str(input(f""" excelfilename morede nazar ra vaared konid """))
        read_from_excel(excelfilename)
    elif selected == "2":
       createtable()
    elif selected == "3":
        insert_excel_todb()


def read_from_excel(excelfilename):
    data=pd.read_excel(excelfilename)
    descripe=data['DESCRIPTION']
    PNO=data['P/N']
    snof=data['S/N  OFF']
    snon=data['S/N  ON']
    date=data['DATE']
    ata=data['ATA']
    print(data)
    column_headers = data.keys().values.tolist()
    print("The Column Header :", column_headers)
    print("The Column Header :", data.columns.ravel())
    print(ata)
    
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

display_menu()

