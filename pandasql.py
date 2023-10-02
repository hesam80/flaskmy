import pandas as pd
import sqlite3
import xlrd
import os.path

def display_menu():
    selected = input(f"""which task number select
    if select 1 read_from_excel run
    if select 2 sqlite createtable
    if select 3 read_db
    if select 4 tstop1 pandas

    """)
    print("select Number is:",selected)
    if selected == "1":
        excelfilename = str(input(f""" excelfilename morede nazar ra vaared konid """))
        read_from_excel(excelfilename)
    elif selected == "2":
       createtable()
       connect()
    elif selected == "3":
        insert_excel_todb()
        read_db()
    elif selected == "4":
        read_op1()


def read_from_excel(excelfilename):
    data=pd.read_excel(excelfilename)
    descripe=data['DESCRIPTION']
    PNO=data['P/N']
    snof=data['S/N  OFF']
    snon=data['S/N  ON']
    date=data['DATE']
    ata=data['ATA']
    #return data
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
    createtable()
    with sqlite3.connect('cmp.db3') as db, \
        ExcelDocument('comptst.xlsx') as src:
        insert_template = "INSERT INTO db " \
         "(dec, pn, snf, snn) " \
         "VALUES (?, ?, ?, ?);"
    db.commit()

def read_db():
    createtable()
    with sqlite3.connect('cmp.db3') as db, \
        ExcelDocument('comptst.xlsx') as src:
        insert_template = "INSERT INTO cmp " \
         "(dec, pn, snf, snn) " \
         "VALUES (?, ?, ?, ?);"
        cur = db.cursor()
        res=cur.execute(
            "SELECT * FROM src ;"
        )
        for row in db.execute(res).fetchall():
            print(';'.join(row))
        res.fetchone()
        print("ok",res.fetchone())
    db.commit()

def connect():
    db = sqlite3.connect('cmp.db3')
    insert_template = "INSERT INTO cmp " \
         "(dec, pn, snf, snn) " \
         "VALUES (?, ?, ?, ?);"
    data= pd.read_excel('comptst.xlsx')
    descripe=data['DESCRIPTION']
    PNO=data['P/N']
    snof=data['S/N  OFF']
    snon=data['S/N  ON']
    date=data['DATE']
    ata=data['ATA']
    db.executemany(insert_template )
    db.commit
    print(data)

def read_op1():
    df=pd.read_excel('MON.xlsx' , sheet_name='Export from MACS')
    #print(df)
    defect_count=df.groupby('Chapter').size()
    print (defect_count)
    actions=df['Action']
    defects=df["Defect"]
    print(defect[2])
    for action in actions:
        
        #print(action)
        #print(action.find('P/N OFF:'))
        filter_tag=action[(int(action.find('P/N OFF:'))):]
            #filter_tag.find('P/N OFF:')
        filter_1st= filter_tag.replace('P/N OFF:', '')
        filter_2nd= filter_1st.replace('S/N OFF:', '')
        filter_3nd= filter_2nd.replace('P/N ON:', '')
        filter_4nd= filter_3nd.replace('S/N ON:', '')
        expose= filter_4nd[int(filter_4nd.find('P/N'))+9:].strip()
        x =expose.split()
        x=pd.DataFrame(x)
        return x

 





display_menu()

