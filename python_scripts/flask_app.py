from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
# import pdb; pdb.set_trace()


@app.route('/<bp_id>')
def get(bp_id):
    return json.dumps({'get': bp_id})


@app.route('/', methods=['POST'])
def find():
    params = request.args
    response = json.dumps({'find': params})
    # import pdb; pdb.set_trace()
    return response


@app.route('/lis', methods=['POST'])
def hello_world():
    path = request.get_json()['path']
    # lis = os.listdir(path)
    # print(lis)


if __name__ == '__main__':
    app.run(debug=True)
