#import requests
#from pydantic import BaseModel, validator, Field

#SERVICE_URL = 'http://headers.jsontest.com/'


#class Post(BaseModel):
#    headers: str | None # Python 3.9 - headers: Optional[str], from typing import Optional 
    
#    @validator('headers')
#    def check_headers_not_empty(cls, v):
#        assert v != '', 'Empty strings are not allowed.'
#        return v


#class Response:

#    def __init__(self, response):
#        self.response = response
#        self.response_json = response.json()
#        self.response_status = response.status_code

#    def validate(self, schema):
#        if isinstance(self.response_json, list):
#            for item in self.response_json:
#                schema.parse_obj(item)                
#        else:
#            schema.parse_obj(self.response_json)
#        return self

#    def assert_status_code(self, status_code):
#        if isinstance(status_code, list):
#            assert self.response_status in status_code, "Received status code is not equal to expected."
#        else:
#            assert self.response_status == status_code, "Received status code is not equal to expected."
#        return self

#def test_getting_posts():
#    r = requests.get(url=SERVICE_URL)
#    response = Response(r)    
#    response.assert_status_code(200).validate(Post)