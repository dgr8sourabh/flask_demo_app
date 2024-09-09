from flask import Blueprint, request, jsonify, redirect
from flask_restful import Resource, Api


homepage_bp = Blueprint('homepage', __name__)
api_homepage = Api(homepage_bp)


class ProcessTaxonomyHomepage(Resource):
    def get(self):
        return str("Welcome to Process Taxonomy homepage")


api_homepage.add_resource(ProcessTaxonomyHomepage, '/homepage')
