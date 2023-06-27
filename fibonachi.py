import sys
import stdio

def display_menu():
    selected = input(f"""which task number select
    if select 1 fibonachi run
    if select 2 length run

    """)
    print("select Number is:",selected)
    if selected == "1":
        n = int(input(f""" addade morede nazar ra vaared konid """))
        fibonachi(n)
    if selected == "2":
        n = int(input(f""" addade morede nazar ra vaared konid """))
        strlengh(n)


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

        
display_menu()

