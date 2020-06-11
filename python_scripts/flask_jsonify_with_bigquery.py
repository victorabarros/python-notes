from google.cloud import bigquery
from flask import Flask, jsonify, make_response
import json
from decimal import Decimal
from datetime import datetime
import uuid

app = Flask(__name__)


@app.route('/')
def hello_world():
    return main()


def main():
    _client = bigquery.Client()
    query_str = '''
        SELECT
            series_id,
            CAST(MAX(value) AS NUMERIC) AS max,
            MIN(value) AS min
        FROM `bigquery-public-data.bls.c_cpi_u`
        GROUP BY series_id
    '''
    query_response = _client.query(query_str)
    _results = query_response.result()
    _response = _build_response(_results)
    return _response


def _build_response(results):
    _results_handled = _handle_result(results)
    return make_response(
        json.dumps({'results': _results_handled},
                   cls=EncodeDefault),
        200,
        {"Content-Type": "application/json"}
    )


def _handle_result(results):
    list_result = []
    for result in results:
        row = {}
        for item in result.items():
            row[item[0]] = item[1]
        list_result.append(row)
    return list_result


class EncodeDefault(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, uuid.UUID):
            return str(obj)
        if isinstance(obj, str):
            return str(obj).replace('"', '')
        if isinstance(obj, datetime):
            return f"{obj.isoformat()}Z"
        return str(obj)


if __name__ == "__main__":
    app.run(debug=True)
