# 9.4.1, 9.4.2 and 9.4.3 - flask app
from flask import Flask
# create an instance
app = Flask(__name__)
# create route - define a starting point
@app.route('/')
# create a function for the root
def hello_world():
    return 'Hello World'
# navigate to folder in terminal and run: export FLASK_APP=app.py
# followed by: flask run