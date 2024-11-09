# Матвеев Игорь, 23-я когорта - Финальный проект. Инженер по тестированию плюс.
import get_an_order_by_track
import data
def test_order_creation_and_retrieval():
    user_response = get_an_order_by_track.create_response
    track_number = user_response.json()["track"]

    order_response = get_an_order_by_track.get_order(track_number)
    assert order_response.status_code == 200
    order_data = order_response.json()