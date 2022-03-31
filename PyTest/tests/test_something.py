from pydantic import BaseModel, validator
from enum import Enum



#response = requests.get(SERVICE_URL)

#print(response.__getstate__())

class Genders(Enum):
    female = "female"
    male = "male"

class Statuses(Enum):
    inactive = "inactive"
    active = "active"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn`t contain @"


class User(BaseModel):
    id: int | None
    name: str | None
    email: str | None
    gender: Genders | None
    status: Statuses | None


    @validator('email')
    def check_that_dog_presented_in_email_address(cls, email):
        if '@' in email:
            return email
        else:
             raise ValueError(UserErrors.WRONG_EMAIL.value)



class Response:

    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)                
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self  
        else:
            assert self.response_status == status_code, self 
        return self
    def __str__(self):
        return  \
            f"\n Status code: {self.response_status} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json}"
            

def test_getting_users_list(get_users):    
    Response(get_users).assert_status_code(200).validate(User)
   

def test_another():
    assert 1 == 1