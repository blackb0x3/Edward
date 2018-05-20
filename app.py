from flask import Flask, redirect, json
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)