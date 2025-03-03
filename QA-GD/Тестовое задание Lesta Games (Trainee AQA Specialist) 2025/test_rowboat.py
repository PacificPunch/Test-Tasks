import pytest
from rowboat import Rowboat

'TESTS ROWBOAT'

def test_create_rowboat():  # проверка создания лодки
    rowboat = Rowboat(5, 3)
    assert rowboat.max_speed == 5
    assert rowboat.max_passengers == 3
    assert rowboat.is_moving == False
    assert rowboat.speed == 0

def test_zero_max_speed():  # проверка создания лодки c нулевой скоростью
    rowboat = Rowboat(0, 3)
    assert rowboat.max_speed == 1
    assert rowboat.max_passengers == 3

def test_zero_max_passengers():  # проверка создания лодки с нулевым колл макс пассажиров
    rowboat = Rowboat(5, 0)
    assert rowboat.max_speed == 5
    assert rowboat.max_passengers == 1
#######################################################################################################

'TESTS OURS'

def test_oars_interaction():  # проверка активации гребли
    rowboat = Rowboat(5, 3)
    rowboat.start_rowing(4)
    assert rowboat.get_current_speed() == 4
#######################################################################################################

'TESTS SPEED'

def test_get_speed():  # проверка изменения скорости
    rowboat = Rowboat(5, 3)
    assert rowboat.get_current_speed() == 0
    rowboat.start_rowing(3)
    assert rowboat.get_current_speed() == 3

def test_decrease_speed():  # проверка уменьшения скорости до нуля
    rowboat = Rowboat(5, 3)
    rowboat.start_rowing(3)
    assert rowboat.get_current_speed() == 3
    rowboat.start_rowing(-3)
    assert rowboat.get_current_speed() == 0

def test_negative_speed():  # проверка попытки установить отрицательную скорость
    rowboat = Rowboat(5, 3)
    rowboat.start_rowing(-3)
    assert rowboat.get_current_speed() == 0  # Скорость не должна стать отрицательной

def test_multiple_speed_changes():  # роверка нескольких последовательных изменений скорости
    rowboat = Rowboat(5, 3)
    rowboat.start_rowing(2)
    assert rowboat.get_current_speed() == 2
    rowboat.start_rowing(1)
    assert rowboat.get_current_speed() == 3
    rowboat.start_rowing(-1)
    assert rowboat.get_current_speed() == 2
#######################################################################################################

'TESTS DIRECTION'

def test_get_direction():  # проверка получения направления лодки
    rowboat = Rowboat(5, 3)
    assert rowboat.get_current_direction() == "вперед"
    rowboat.change_direction("назад")
    assert rowboat.get_current_direction() == "назад"

def test_change_direction():  # проверка изменения направления
    rowboat = Rowboat(5, 3)
    rowboat.change_direction("назад")
    assert rowboat.get_current_direction() == "назад"
    rowboat.change_direction("вперед")
    assert rowboat.get_current_direction() == "вперед"

def test_invalid_direction():  # проверка попытки установить недопустимое направление
    rowboat = Rowboat(5, 3)
    rowboat.change_direction("влево")  # Это должно вывести сообщение об ошибке
    assert rowboat.get_current_direction() == "вперед"  # Направление не должно измениться

def test_multiple_direction_changes():  # проверка нескольких последовательных изменений направления
    rowboat = Rowboat(5, 3)
    rowboat.change_direction("назад")
    assert rowboat.get_current_direction() == "назад"
    rowboat.change_direction("вперед")
    assert rowboat.get_current_direction() == "вперед"
    rowboat.change_direction("назад")
    assert rowboat.get_current_direction() == "назад"
#######################################################################################################

'TESTS PASSENGERS'

def test_add_passenger():  # проверка добавления пассажира
    rowboat = Rowboat(5, 3)
    rowboat.add_passenger("Alice")
    assert "Alice" in rowboat.get_passengers()

def test_remove_passenger():  # проверка удаления пассажира
    rowboat = Rowboat(5, 3)
    rowboat.add_passenger("Alice")
    rowboat.remove_passenger("Alice")
    assert "Alice" not in rowboat.get_passengers()

def test_get_passengers():  # проверка получения списка пассажиров в лодке
    rowboat = Rowboat(5, 3)
    rowboat.add_passenger("John")
    assert "John" in rowboat.get_passengers()

def test_empty_passengers_list():  # проверка пустого списка пассажиров
    rowboat = Rowboat(5, 3)
    assert rowboat.get_passengers() == []

def test_multiple_passengers():  # проверка добавления нескольких пассажиров
    rowboat = Rowboat(5, 3)
    rowboat.add_passenger("John")
    rowboat.add_passenger("Jane")
    assert "John" in rowboat.get_passengers() and "Jane" in rowboat.get_passengers()

def test_passenger_limit():
    rowboat = Rowboat(5, 3)
    for i in range(3):
        rowboat.add_passenger(f"Passenger{i}")
    with pytest.raises(AssertionError):  # Проверяем, что добавление лишнего пассажира вызывает AssertionError
        rowboat.add_passenger("ExtraPassenger")
#######################################################################################################

'TESTS ROWING'

def test_is_rowing():  # проверка движения лодки (скорость >0)
    rowboat = Rowboat(5, 3)
    assert rowboat.is_rowing() == False  # Лодка изначально не движется
    rowboat.start_rowing(3)
    assert rowboat.is_rowing() == True  # После начала гребли лодка должна двигаться
    rowboat.start_rowing(-3)
    assert rowboat.is_rowing() == False  # После остановки гребли лодка не должна двигаться

def test_rowing():
    rowboat = Rowboat(5, 3)
    rowboat.start_rowing(3)
    assert rowboat.get_current_speed() == 3
    assert rowboat.is_rowing() == True
    rowboat.start_rowing(-3)
    assert rowboat.get_current_speed() == 0
    assert rowboat.is_rowing() == False
#######################################################################################################