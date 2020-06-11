from flask import Flask, jsonify
from flask_admin import Admin

app = Flask(__name__)

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

@app.route("/book/<str:id>")
def fetch_hotels(id=""):
    return jsonify({"1": {"name": "foo", ""}})

admin = Admin(app, name='microblog', template_mode='bootstrap3')
# Add administrative views here

app.run(port=8090, debug=True, host="0.0.0.0")
