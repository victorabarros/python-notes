from datetime import datetime
from quart import Quart
import requests
import time

app = Quart(__name__)


@app.route('/request')
async def request():
    url = 'http://www.google.com.br'
    r = requests.get(url)
    return f"request to {url}: {r} - {datetime.utcnow()}\n"


@app.route('/sleep/<int:seconds>')
async def sleep(seconds):
    time.sleep(seconds)
    return f'sleeped {seconds} - {datetime.utcnow()}\n'


@app.route('/hello')
async def hello():
    return f'hello world - {datetime.utcnow()}\n'


app.run()
