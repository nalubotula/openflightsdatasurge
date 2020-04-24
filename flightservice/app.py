from flask import Flask
from parserservice.parseurl import Pareser

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/parseUrl',methods=['GET'])
def parseDataFronURL():
    # inputReq=request.data;
    parse=Pareser('https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat')
    parse.pareseDataFromURL();
    return ""

if __name__ == '__main__':
    app.run(host='localhost',port='8443')
    parseDataFronURL()