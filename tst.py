import pandas as pd
def display_menu():
    """
    DISPLAY MENU OF WHT CAN DO:
    """
    selected=input(f"""WHICH ONE YOU TO DO?
    RUN PANDAS PRACTICE
    2)RUN TAHLIL DEFECT
    3)ETC...
    """)
    if selected=="1":
        pandas_practice()
    elif selected=="2":
        pass

def pandas_practice():
    df = pd.read_excel("comptst.xlsx")
    df1 = pd.DataFrame({'a':[1,3,5,7,4,5,6,4,7,8,9],
                   'b':[3,5,6,2,4,6,7,8,7,8,9]})
    rows = df.index
    description=df['DESCRIPTION']
    partno=df['P/N']
    print (description)
    print(partno)
    df2=pd.DataFrame({'DESCRIPTION':['MAIN WHEEL ASSY'],'P/N':['AHA1925-2']})
    print("column heading is:")
    print(df2.columns)


display_menu()

