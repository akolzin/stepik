import json

from api import random
from random import randint
from conftest import client
import requests

link = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=68d9c6557101f408224e83aa3c323c11"
link1 = "https://restful-booker.herokuapp.com"
response = requests.get(link1)

class TestExample:
    def test_status_code(self, client):  # тест кода ответа
        assert 200 == response.status_code or 201 == response.status_code, "Код ответа неверен"

    def test_is_json(self, client):  # проверяем что пришел json
        response = requests.get("https://restful-booker.herokuapp.com/booking/")
        try:
            json_data = json.loads(response.text)
            print(json_data)
            print(json.dumps(response.json()))
        except ValueError:
            assert False, "Данные не соответствуют json"

    def test(self, client):
        response = requests.get(link)
        json_data = json.loads(response.text)
        path = json_data["main"]
        path1 = path['temp_max']
        path2 = json_data["main"]["temp_min"]
        print(json_data)
        print(path1)
        print(path2)
        assert 'main' in json_data
        assert path1 > path2

    def test2(self, client):
        print()

    def test_create_new_booking(self, client):
        data = random.random_booking()
        res = client.create_booking(data)
        created = res.json()
        assert created.get("bookingid")
        assert created.get("booking") == data

    def test_new_booking_exists(self, client):
        data = random.random_booking()
        res = client.create_booking(data)
        created = res.json()
        bookingid = created.get("bookingid")
        res = client.get_booking(bookingid)
        exists = res.json()
        assert exists == data

    def test_update_booking(self, client):
        data = random.random_booking()
        res = client.create_booking(data)
        created = res.json()
        bookingid = created.get("bookingid")
        data2 = random.random_booking()
        res = client.update_booking(bookingid, data2)
        updated = res.json()
        assert updated == data2

    def test_not_existing_booking(self, client):
        res = client.get_booking(randint(10000, 99999))
        assert res.status_code == 404