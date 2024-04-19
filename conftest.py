import pytest
import requests
from faker import Faker
from urls import Urls
from data import IngredientsData
from data import GenerateUserCredentials

faker = Faker()


@pytest.fixture
def generate_user_credentials():
    email = GenerateUserCredentials.email
    password = GenerateUserCredentials.password
    name = GenerateUserCredentials.name
    return email, password, name


@pytest.fixture
def create_new_user(generate_user_credentials):
    email, password, name = generate_user_credentials
    payload = {"email": email, "password": password, "name": name}
    response = requests.post(f"{Urls.REGISTER_USER}", data=payload)
    data = response.json()
    user_credentials = [email, password, name]

    yield user_credentials, response.json()

    access_token = data.get("accessToken")
    requests.delete(f"{Urls.DELETE_USER}", headers={'Authorization': f'{access_token}'})


@pytest.fixture
def create_new_order(create_new_user):
    access_token = create_new_user[1]["accessToken"]
    headers = {"Authorization": f"{access_token}"}
    payload = {
        'ingredients': [IngredientsData.BUN, IngredientsData.SAUCE, IngredientsData.FILLER]
    }
    response = requests.post(f'{Urls.GET_USER_ORDERS}', data=payload, headers=headers)
    data = response.json()
    return data
