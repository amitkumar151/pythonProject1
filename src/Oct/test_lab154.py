import allure
import pytest
import requests


@allure.title("TC# 1 Create  booking of CRUD Positive")
@allure.description("TC# 1 verify the create booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"content-type": "application/json"}
    payload = {
        "firstname":"Sally",
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
    assert response.status_code == 200

    responseData = response.json()

    bookingid = responseData["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int

    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]

    assert firstname =="Sally"
    assert lastname == "Brown"
    assert totalprice == 111

    checking = responseData["booking"]["bookingdates"]["checkin"]
    assert checking == "2013-02-23"

@allure.title("TC# 2 Create  booking of CRUD negative")
@allure.description("TC# 2 verify booking is not created {} data")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"content-type": "application/json"}
    payload={}
    response = requests.post(url=URL, headers=headers, json=payload)
    print(type(URL))
    print(type(headers))

    assert response.status_code == 500

@allure.title("TC# 3 Create  booking of CRUD Positive")
@allure.description("TC# 3 verify total price is given string negative")
@pytest.mark.crud
def test_create_booking_negative_tc3():
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"content-type": "application/json"}
    payload = {
        "firstname":"Sally",
        "lastname": "Brown",
        "totalprice": "amit",
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
