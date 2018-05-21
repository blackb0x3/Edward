from flask import Flask, redirect, json
from flask_restful import reqparse, abort, Api, Resource

from controllers import AlgorithmController

app = Flask(__name__)
api = Api(app)

################# CONTROLLERS #################

api.add_resource(AlgorithmController, '/algorithms/<algorithmname>')

############# END OF CONTROLLERS ##############

if __name__ == '__main__':
    app.run(debug=True)