from flask import Flask
import time
import calendar

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello,folks I am running Flask! </h1>"

@app.route('/users/<name>')
def user(name):
    localtime = time.asctime( time.localtime(time.time()) )
    return "<h1>Hello, {}! time is {} </h1>".format(name.upper(),localtime)

@app.route('/calender')
def calender():
    cal = calendar.month(2008, 1)
    return cal
    
if __name__ == '__main__':
    app.run(debug=True)
