# Laptop Service
  
from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
import os
import sys
import subprocess
import get_sentiment as gs
#from pymongo import MongoClient
#from bson.json_util import loads, dumps
#import json
#import pandas


# Instantiate the app
app = Flask(__name__)
api = Api(app)

#client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
#client = MongoClient("172.19.0.2", 27017)
#db = client.tododb
#col = db.tododb

class home(Resource):
    def get(self):
        return make_response(render_template('home.html'),200) #ender_template('home.html')


class get_sentiment(Resource):
    def get(self):
        #g++ main.cpp -lcurlpp -lcurl -g -pg `xml2-config --cflags --libs` `pkg-config libxml++-2.6 --cflags --libs` --std=c++0x
        #subprocess.run(["gcc", "get_sentiment.cpp", "-lstdc++", "-lcurl"], cwd='./backend_data')
        #subprocess.run(["g++", "v_2get_sentiment.cpp", "-lcurlpp", "-lcurl", "-g", "-pg", "`xml2-config --cflags --libs`", "`pkg-config libxml++-2.6 --cflags --libs`",
        #                "--std=c++0x"], cwd='./backend_data')

        args = request.args

        sentiment = gs.Request(args['ticker'])

        return { args['ticker'] : str(sentiment.make_request()) } 



api.add_resource(home, '/')
api.add_resource(get_sentiment, '/get_sentiment')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
