# Матвеев Игорь, 23-я когорта - Финальный проект. Инженер по тестированию плюс.
from http.client import responses

import configuration
import data
import requests
# создать заказ
def create_order(body):
    return requests.post(configuration.URL_SERVER + configuration.CREATE_ORDER,
                         json=body)
create_response = create_order(data.create_body)

# получить заказ по номеру
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVER}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response
