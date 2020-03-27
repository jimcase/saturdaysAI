import time

from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app, support_credentials=True)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/api/query', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def get_query_from_react():
    print("hello data")

    print(request.get_json()['fileContent'])

    return "OK"


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
