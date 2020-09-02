from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
import json
import os
import random
import numpy as np
import time

from datetime import datetime

app = Flask(__name__)
api = Api(app)



class Math(Resource):
    def get(self, runid):
        return Response({"error": "unknown patient_id"}, status=404, mimetype='application/json')

    def post(self, runid):
        body = request.get_json(silent=True)
        print (str(body))
        retarray = np.random.randint(body["value"], size=1)
        return jsonify ({"retvalue": str(retarray[0]), "runid": runid, "executedonon":datetime.now()  })


api.add_resource(Math, '/domath/<string:runid>')
#api.add_resource(Score, '/score/<string:patient_id>')


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=4996, threaded=True)