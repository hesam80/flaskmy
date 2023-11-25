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
    print("column heading is:")
    print(df.columns)


display_menu()

