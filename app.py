from flask import Flask
from flask import json
from flask import render_template
from datacollector import datacollector
app = Flask(__name__)

data = datacollector()

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    #return "<h1>Home Page</h1>"
    return render_template('home.html')

@app.route('/debug')
def summary():
    response = app.response_class(
        response=json.dumps(data),
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)