from dataclasses import asdict

import requests
import pytest
import json
from routes.Routes import Routes
from payloads.Payload import Payload


class TestProductAPI:
    @pytest.fixture(autouse=True)
    def init_class_vars(self, setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]
        self.payload = Payload()

    def test_get_all_users(self):
        res = requests.get(self.base_url + Routes.GET_ALL_USERS)
        assert res.status_code == 200
        data = res.json()
        print(json.dumps(data, indent=4))
        assert len(data) > 0

    def test_get_user_by_id(self):
        user_id = self.config.get_property("userId")
        endpoint = self.base_url + Routes.GET_USER_BY_ID.format(id=user_id)
        res = requests.get(endpoint)
        assert res.status_code == 200
        data = res.json()
        print(json.dumps(data, indent=4))

    def test_get_user_with_limit(self):
        limit = self.config.get_property("limit")
        endpoint = self.base_url + Routes.GET_USER_WITH_LIMIT.format(limit=limit)
        res = requests.get(endpoint)
        assert res.status_code == 200
        data = res.json()
        print(json.dumps(data, indent=4))
        assert len(data) == int(limit)

    def test_get_users_sorted_desc(self):
        endpoint = self.base_url + Routes.GET_USER_SORTED.format(order='desc')
        response = requests.get(endpoint)
        assert response.status_code == 200
        data = response.json()
        print(json.dumps(data, indent=4))
        ids = [user['id'] for user in data]
        assert ids == sorted(ids, reverse=True)

    def test_get_users_sorted_asc(self):
        endpoint = self.base_url + Routes.GET_USER_SORTED.format(order='asc')
        response = requests.get(endpoint)
        assert response.status_code == 200
        data = response.json()
        print(json.dumps(data, indent=4))
        ids = [user['id'] for user in data]
        assert ids == sorted(ids)

    def test_create_user(self):
        user_payload = self.payload.user_payload()
        response = requests.post(self.base_url + Routes.CREATE_USER, json=asdict(user_payload))
        assert response.status_code == 201
        data = response.json()
        print(json.dumps(data, indent=4))
        #assert id in data
        print("Generated UserID:", data["id"])

    def test_update_user(self):
        user_id = self.config.get_property("userId")
        updated_user = self.payload.user_payload()
        endpoint = self.base_url + Routes.UPDATE_USER.format(id=user_id)
        response = requests.put(endpoint, json=asdict(updated_user))
        assert response.status_code == 200
        data = response.json()
        print(json.dumps(data, indent=4))
        assert data["username"] == updated_user.username

    def test_delete_user(self):
        user_id = self.config.get_property("userId")
        endpoint = self.base_url + Routes.DELETE_USER.format(id=user_id)
        response = requests.delete(endpoint)
        assert response.status_code == 200
        # data = response.json()
        # print(json.dumps(data, indent=4))
