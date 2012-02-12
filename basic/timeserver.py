import bobo
import json
from datetime import datetime

@bobo.query('')
def redirect():
    return bobo.redirect('/')

@bobo.query('/')
def serve():
    return json.dumps({'timestamp':datetime.now().isoformat(' ')})

application = bobo.Application(bobo_resources=__name__)
