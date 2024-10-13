# fixture concept
# you can use fixture
# context to the rest
# similar - pre condition , post condtion


# pre condition -token , booking id, -fixture
# test_update_negative1
# test_updte_postive 1

import pytest

@pytest.fixture()
def create_token():
    return "abc"
@pytest.fixture()
def create_booking_id():
    return "1"
@pytest.fixture()
def read_excel_file():
    return "xyz"
@pytest.fixture()
def update_booking():
    return "amit"
@pytest.fixture()
def read_json_file():
    return "{}"

def test_consume(create_token,create_booking_id,read_excel_file,update_booking):
    print(create_token)
    print(create_booking_id)
    print(read_excel_file)
    print(update_booking)
    print(read_json_file())