import time

from flask import Flask, request
from flask_cors import CORS

from src.utils.dataframe import DataFrame

app = Flask(__name__)

CORS(app)

dt = DataFrame()

@app.route('/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/api/query', methods=['POST'])
def get_query_from_react():
    print("hello data")

    # print(request.get_json()['fileContent'])

    data = request.get_json()['fileContent']

    dt.read_data_from_string(data, '\t')

    print(dt.data_frame.to_json())

    return dt.data_frame.to_json()


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
