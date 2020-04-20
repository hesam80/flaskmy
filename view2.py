#!C:\Users\Pars\AppData\Local\Programs\Python\Python38-32\python.exe

print("Content-Type: text/html\n charset:utf-8\n")
def hello(request):
    return HttpResponse("Hello world")
    print("Content-Type: text/html\n charset:utf-8\n")
print("<br><B>hello python</B>")
print ("""
    <H1>CGI script ! Python</H1>
    <H2>This is my first CGI script</H2>
    """)
print("""<body>
	<header>
		<div class="container">
		<br>
		<p>salam be hame</p>
			<ul>
				<li><a href="tst.py">go to tst python</a></li>
				<li><a href="view.py">go to view</a></li>
				<li><a href=""></a></li>
				<li><a href=""></a></li>
				<li><a href=""></a></li>	
			</ul>
		</div>
	</header>
</body>""")
x=12
y=2

x = int(x)
y = int(y)
s = x+y

print("""<li><a href="tst.py">go to tst python</a></li>""" , s)
#f= open('tt.html')
#content = f.read()
#print(content)
print(__name__)


