import os
import random
from flask import Flask, flash, redirect, render_template, request, url_for

# pylint: disable=C0103
app = Flask(__name__)


@app.route('/')
def view():
    """Return a friendly HTTP greeting."""
    message = "It's redeployedd Wow how it's Beautiful!"
    congramessage="Congratulations, you successfully deployed a container image to Cloud Run!"
    """Get Cloud Run environment variables."""
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')
    num=random.randint(1,12)
    hitt= num*2
    return render_template('index.html',num=num,hit=hitt,congmsg=congramessage,
        message=message,
        Service=service,
        Revision=revision)

@app.route("/indexx")
def indexx():
	

    return render_template("indexx.html")
 
#Define 2nd Route and Content
@app.route("/success", methods = ['POST'])
def success():
  
  height=request.form["tool"]
  vazn = request.form["arz"]
  num=random.randint(1,12)
  return render_template('success.html', hit=height , number=num , vazn=vazn)
 
@app.route('/resultst')
def resultst():
	num=random.randint(1,12)
	return render_template('resultst.html', number=num)


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '80')
    app.run(debug=True)
