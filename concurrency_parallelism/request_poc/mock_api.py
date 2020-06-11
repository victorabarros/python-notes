from flask import Flask
import time


app = Flask(__name__)


@app.route("/hello")
def hello():
    time.sleep(.5)
    return {"message": "hello ~ vbarros"}


app.run(port=5001)
