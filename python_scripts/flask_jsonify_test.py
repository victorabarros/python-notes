from flask import Flask#, jsonify

app = Flask(__name__)

@app.route('/')
def get_test():
    results = {
        'Decimal': 10
    }
    # response = jsonify({'results': results})
    print('response')

if __name__ == "__main__":
    app.run()
