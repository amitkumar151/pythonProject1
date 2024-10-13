# password - i store the password in framework

# ENV File- dot.env
# how do you store your password or credential in te framework
# pip install python-dotenv

from dotenv import load_dotenv
import os
def test_update_req():
    load_dotenv()
    username=os.getenv("USERNAME")
    password=os.getenv("PASSWORD")
    print(username)
    print(password)