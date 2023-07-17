import sys
import stdio
import redis

def display_menu():
    selected = input(f"""which task number select
    if select 1 fibonachi run
    if select 2 length run
    if select 3 tstregex

    """)
    print("select Number is:",selected)
    if selected == "1":
        n = int(input(f""" addade morede nazar ra vaared konid """))
        fibonachi(n)
    elif selected == "2":
        n = int(input(f""" addade morede nazar ra vaared konid """))
        strlengh(n)
    elif selected == "3":
        n = input(f""" addade morede nazar ra vaared konid """)
        tstregex(n)


def fibonachi(n):
	a=0
	b=1
	print("series fibonachi",n,"is = ",end='')
	while a<n:
		print(a , end='')
		
		a, b = b, a+b
	print()
	

def strlengh(n):
        
        s=fibonachi(n)
        strleng=readInt(len(s))
        print(s)
        print(strleng[0])

def tstregex(n):
    s = _readRegExp(r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?')
    print(n)

        
display_menu()

