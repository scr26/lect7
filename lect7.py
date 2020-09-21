import flask
import os
import random

app = flask.Flask(__name__)

@app.route('/') # Python decorator
def index():
    num = random.randint(1, 20)
    birthday = '05/29/1993'
    return flask.render_template(
        "index.html",
        random_number = num, # HTML variable = python variable
        birth_date = birthday
        )
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)
