from flask import Flask
from flask import render_template
import time
import calendar

app = Flask(__name__)


@app.route('/')
def index():
    localtime = time.asctime( time.localtime(time.time()) )
    return render_template('index.html',time=localtime)

@app.route('/users/<name>')
def user(name):
    localtime = time.asctime( time.localtime(time.time()) )
    return render_template('users.html',name=name.upper())

@app.route('/calender')
def calender():
    cal = calendar.month(2008, 1)
    return render_template('calender.html',cal=cal)
 
    
if __name__ == '__main__':
    app.run(debug=True,port=4000)
