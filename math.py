"""
This is the people module and supports all the ReST actions for the
PEOPLE collection .
Solution borrowed from https://realpython.com/flask-connexion-rest-api/
"""

# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort
import numpy as np

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


def create(simvalue):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    runid = simvalue.get("runid", None)
    invalue = simvalue.get("invalue", None)

  #basic return back + 100
    return invalue+100, 201
  
