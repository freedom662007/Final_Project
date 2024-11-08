# Матвеев Игорь, 23-я когорта - Финальный проект. Инженер по тестированию плюс.
import configuration
import data
import requests
# создать заказ
def create_order(body):
    return requests.post(configuration.URL_SERVER + configuration.CREATE_ORDER,
                         json=body)
#response = create_order(data.create_body)
#print(response.status_code)
#print(response.json())
# получить заказ по номеру
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVER}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response
def test_order_creation_and_retrieval():
    response = create_order(data.create_body)

    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)
# Получение данных заказа по треку
    order_response = get_order(track_number)
    assert order_response.status_code == 200
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)