import pytest
from rowboat import Rowboat

@pytest.fixture
def rowboat():
    return Rowboat(capacity=3)

def test_add_passenger(rowboat):                    #Тест на добавление пассажира
    rowboat.add_passenger()
    assert rowboat.current_load == 1

def test_remove_passenger(rowboat):                 #Тест на удаление пассажира
    rowboat.add_passenger()
    rowboat.add_passenger()
    rowboat.remove_passenger()
    assert rowboat.current_load == 1

def test_add_passenger_exceed_capacity(rowboat):    #Тест на превышение вместимости
    rowboat.add_passenger()
    rowboat.add_passenger()
    rowboat.add_passenger()
    with pytest.raises(Exception) as excinfo:
        rowboat.add_passenger()
    assert str(excinfo.value) == "Лодка переполнена"



def test_stop_rowing(rowboat):                      #Тест на остановку гребли
    rowboat.add_passenger()
    rowboat.start_rowing(5)
    rowboat.stop_rowing()
    assert not rowboat.is_moving
    assert rowboat.speed == 0

def test_get_status(rowboat):                       #Тест на получение статуса лодки
    rowboat.add_passenger()
    rowboat.start_rowing(3)
    status = rowboat.get_status()
    assert status['capacity'] == 3
    assert status['current_load'] == 1
    assert status['is_moving'] is True
    assert status['speed'] == 3

def test_remove_passenger_no_passengers(rowboat):   #Тест на удаление персонажа из пустой лодки
    with pytest.raises(Exception) as excinfo:
        rowboat.remove_passenger()
    assert str(excinfo.value) == "Нет пассажиров для удаления"