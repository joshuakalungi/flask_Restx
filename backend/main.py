from flask_restx import Api, Resource
from flask import Flask


app = Flask(__name__)


api = Api(app)

@app.route('/')
def hello_get():
    return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)