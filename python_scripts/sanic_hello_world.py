from sanic import Sanic, request
from sanic import response as res
import json

app = Sanic(__name__)


@app.route("/", methods=['POST'])
def test(request):
    response = res.text("I\'m a teapot", status=418)
    import pdb; pdb.set_trace()
    return response


if __name__ == '__main__':
    app.run(port=8000, debug=True)
