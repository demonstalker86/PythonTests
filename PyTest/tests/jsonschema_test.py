import requests

from jsonschema import validate

SERVICE_URL = 'http://headers.jsontest.com/'
POST_SCHEMA = {        
        "properties":{
                "headers": {"type": "string", "type": "number"}
            },        
    }

class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, "Received status code is not equal to expected."
        else:
            assert self.response_status == status_code, "Received status code is not equal to expected."
        return self

def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)    
    response.assert_status_code(200).validate(POST_SCHEMA)

    






