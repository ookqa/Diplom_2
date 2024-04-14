import pytest
import requests
from faker import Faker
from urls import Urls

faker = Faker()


@pytest.fixture
def create_new_user():
    user_credentials = []
    email = ('buntester' + faker.lexify(text='????????????') + '@bunstester.com').lower()
    password = faker.lexify(text='????????????')
    name = faker.name()
    payload = {"email": email, "password": password, "name": name}
    response = requests.post(f"{Urls.REGISTER_USER}", data=payload)
    data = response.json()
    if response.status_code == 200:
        user_credentials.append(email)
        user_credentials.append(password)
        user_credentials.append(name)

    yield user_credentials, response.json()

    access_token = data.get("accessToken")
    requests.delete(f"{Urls.DELETE_USER}", headers={'Authorization': f'{access_token}'})


@pytest.fixture
def create_new_order(create_new_user):
    access_token = create_new_user[1]["accessToken"]
    headers = {"Authorization": f"{access_token}"}
    payload = {
        'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa75', '61c0c5a71d1f82001bdaaa78']
    }
    response = requests.post(f'{Urls.GET_USER_ORDERS}', data=payload, headers=headers)
    data = response.json()
    return data
