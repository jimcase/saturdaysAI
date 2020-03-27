import time
from io import StringIO

from flask import Flask, request
from flask_cors import CORS

from src.utils.dataframe import DataFrame

app = Flask(__name__)

CORS(app)


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/api/query', methods=['POST'])
def get_query_from_react():
    print("hello data")

    print(request.get_json()['fileContent'])

    dt = DataFrame()

    test_data = StringIO(request.get_json()['fileContent'])

    dt.read_tsv_data_file(test_data)

    print(dt.describe())

    return "OK"


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
