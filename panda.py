import pandas as pd

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
    

read_from_excel('comptst.xlsx')

