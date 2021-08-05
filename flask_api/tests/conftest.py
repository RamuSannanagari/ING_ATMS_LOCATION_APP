import pytest

from middleware.AtmFlow import AtmflowMiddleware

"""
@pytest.fixture(scope='module')
def new_user():
    user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
    return user
"""

@pytest.fixture(scope='module')
def login():
    payload={}
    payload['username']="test"
    payload['password']="test"
    flow = AtmflowMiddleware()
    return_status, result = flow.run(payload,"authenticate")
    return return_status,result

@pytest.fixture(scope='module')
def list_atms():
    payload=None
    flow = AtmflowMiddleware()
    return_status, result = flow.run(payload,"select")
    return return_status,len(result)

@pytest.fixture(scope='module')
def insert_atms():
    payload={"atm_details": {"address": {"street": "Raadhuislaan 110 -", "housenumber": "110", "postalcode": "3202 EM", "city": "Spijkenisse", "geoLocation": {"lat": "51.84766", "lng": "4.329365"}}, "distance": 0, "openingHours": [{"dayOfWeek": 2, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}, {"dayOfWeek": 3, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}, {"dayOfWeek": 4, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}, {"dayOfWeek": 5, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}, {"dayOfWeek": 6, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}, {"dayOfWeek": 7, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}, {"dayOfWeek": 1, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}], "functionality": "Geld storten en opnemen", "type": "GELDMAAT"}}
    flow = AtmflowMiddleware()
    return_status, result = flow.run(payload,"insert")
    return return_status,

@pytest.fixture(scope='module')
def update_atms():
    payload={"id": 3, "atm_details": {"address": {"street": "Raadhuislaan 120 -", "housenumber": "120", "postalcode": "3202 EM", "city": "Spijkenisse", "geoLocation": {"lat": "51.84766", "lng": "4.329365"}}, "distance": 0, "openingHours": [{"dayOfWeek": 2, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}, {"dayOfWeek": 3, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}, {"dayOfWeek": 4, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}, {"dayOfWeek": 5, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}, {"dayOfWeek": 6, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}, {"dayOfWeek": 7, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}, {"dayOfWeek": 1, "hours": [{"hourFrom": "07:00", "hourTo": "23:00"}]}], "functionality": "Geld storten en opnemen", "type": "GELDMAAT"}}
    flow = AtmflowMiddleware()
    return_status, result = flow.run(payload,"update")
    return return_status,

@pytest.fixture(scope='module')
def delete_atms():
    payload={"id": 3}
    flow = AtmflowMiddleware()
    return_status, result = flow.run(payload,"delete")
    return return_status,

@pytest.fixture(scope='module')
def insert_atms_invalid_payload():
    payload={}
    flow = AtmflowMiddleware()
    return_status, result = flow.run(payload,"insert")
    return return_status,result

@pytest.fixture(scope='module')
def update_atms_invalid_payload():
    payload={}
    flow = AtmflowMiddleware()
    return_status, result = flow.run(payload,"update")
    return return_status,result

@pytest.fixture(scope='module')
def delete_atms_invalid_payload():
    payload={}
    flow = AtmflowMiddleware()
    return_status, result = flow.run(payload,"delete")
    return return_status,result

@pytest.fixture(scope='module')
def login_invalid_payload():
    payload={}
    flow = AtmflowMiddleware()
    return_status, result = flow.run(payload,"authenticate")
    return return_status,result

@pytest.fixture(scope='module')
def invalid_payload():
    payload=[]
    flow = AtmflowMiddleware()
    return_status, result = flow.run(payload,"authenticate")
    return return_status,result