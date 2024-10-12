# create a booking
# verify booking is not null
# Status code , header

# Request module
import pytest
import allure
import requests


@allure.title("Test Authentication")
@allure.description(
    "This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TC#1 -> verify the get request is id work ")
@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 200
@allure.title("Test Authentication")
@allure.testcase("TC#2-> verify the get request is invalid id ")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    assert response_data.status_code == 404
@allure.title("Test Authentication")
@allure.testcase("TC#3 -> verify to get invalid booking")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = ("https://restful-booker.herokuapp.com/booking/invalid")
    response_data = requests.get(url)
    assert response_data.status_code == 404
