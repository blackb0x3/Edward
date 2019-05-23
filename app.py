import subprocess

from flask import Flask, redirect, json, render_template
from flask_restful import reqparse, abort, Api, Resource

from controllers import AlgorithmController, AlgorithmListController, GraphController

REACT_BUILD_COMMAND = "cd static && yarn run build"

app = Flask(__name__, template_folder="./static/dist")
api = Api(app)

################# API CONTROLLERS #################

api.add_resource(AlgorithmListController, '/api/algorithms')
api.add_resource(AlgorithmController, '/api/algorithms/<algorithmname>')
api.add_resource(GraphController, '/api/algorithms/graphs/<graphid>')

############# END OF API CONTROLLERS ##############




##################### APP ENDPOINT ####################

@app.route('/')
def index():
    return render_template("index.html")

################# END OF APP ENDPOINT #################

if __name__ == '__main__':
    subprocess.run(REACT_BUILD_COMMAND, shell=True)
    app.run(debug=True)
