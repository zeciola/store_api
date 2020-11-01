from flask import json

from api_config import api


def generate_postman_collection():
    urlvars = False
    swagger = True
    data = api.as_postman(urlvars=urlvars, swagger=swagger)
    with open('napp_postman_collection.json', 'w') as outfile:
        json.dump(data, outfile)
