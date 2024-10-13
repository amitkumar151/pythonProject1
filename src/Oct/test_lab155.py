# put -request
# url
# path -booking id
# token -auth
# payload
# headers


import allure
import pytest
import requests


# creating a token -post
# creating

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


def test_put_request_postive():
    base_url = "https://restful-booker.herokuapp.com/"
    base_path = "/booking/" + str(create_booking())
    PUT_URL = base_url + base_path
    cookies = "token=" + str(create_booking)
    headers = {
        "content_Type": "application/json",
        "cookie": cookies
    }

    json_payload = {
        "firstname": "amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }


    response1 = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response1.status_code==200
    data = response1.json()
    print(data)
    assert data["firstname"] == ["amit"]

def test_delete():
    URL="https://restful-booker.herokuapp.com/booking/"
    booking_id=create_booking()
    DELETE_URL= URL + str(booking_id)
    cookie_value= "token" + create_token()
    headers= {
        "content-Type": "application/json",
        "cookie": cookie_value
    }
    print(headers)

    respnse2= requests.delete(url=DELETE_URL, headers=headers)