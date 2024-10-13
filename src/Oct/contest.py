import pytest
import requests


@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    jason_payload1 = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url = url, headers = headers, json= jason_payload1)
    token = response.json()["token"]
    print(token)
    return token


# create booking

@pytest.fixture()
def create_booking():
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"content-type": "application/json"}
    payload = {
        "firstname": "Sally",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=payload)
    print((type(URL)))
    print(type(headers))
    assert response.status_code == 200

    data = response.json()
    booking_id = data["bookingid"]
    return booking_id