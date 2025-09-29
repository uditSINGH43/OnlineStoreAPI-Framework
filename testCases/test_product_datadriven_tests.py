import os

import pytest
import requests

from datamodels.Product import Product
from routes.Routes import Routes
from utils.DataProviders import read_json_data

# get file path
path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testData", "product.json"))


class TestProductAPI:
    @pytest.fixture(autouse=True)
    def init_class_vars(self, setup):
        self.base_url = setup["base_url"]
        self.config = setup["config_reader"]

    @pytest.mark.regression
    @pytest.mark.parametrize('order_data', read_json_data(path))
    def test_add_new_delete_product(self, order_data):
        product_data = order_data[0]

        # Extract Fields
        title = product_data["title"]
        price = float(product_data["price"])
        description = product_data["description"]
        image = product_data["image"]
        category = product_data["category"]

        payload = Product(title, price, description, image, category)

        # Adding a product
        response = requests.post(self.base_url + Routes.CREATE_PRODUCT, json=payload.__dict__)
        assert response.status_code == 201
        data = response.json()
        # print(json.dumps(data, indent=4))

        # Validations
        assert data["title"] == payload.__dict__["title"]
        product_id = data["id"]

        # delete Product
        endpoint = self.base_url + Routes.DELETE_PRODUCT.format(id=product_id)
        response = requests.delete(endpoint)
        assert response.status_code == 200
