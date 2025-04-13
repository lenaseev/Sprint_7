import requests
import random
import string
from urls import Urls

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def register_new_courier_and_return_login_password():
    urls = Urls()
    login_pass = []
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(urls.COURIER, data=payload)

    if response.status_code == 201:
        login_pass.extend([login, password, first_name])

    return login_pass

def delete_courier(login, password):
    urls = Urls()
    response = requests.post(
        urls.COURIER_LOGIN,
        data={"login": login,
              "password": password}
    )

    if response.status_code == 200:
        courier_id = response.json().get("id")
        if courier_id:
            requests.delete(urls.courier_delete(courier_id))
