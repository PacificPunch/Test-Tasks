class Oars:
    def __init__(self):
        self.speed = 0
        self.direction = "вперед"

    def row(self, speed_change):#Изменить скорость гребли
        self.speed += speed_change
        if self.speed < 0:
            self.speed = 0  # Скорость не может быть отрицательной

    def change_direction(self, new_direction):#Изменить направление движения
        valid_directions = ["вперед", "назад"]
        if new_direction in valid_directions:
            self.direction = new_direction
        else:
            print("Недопустимое направление.")

    def get_speed(self): #Получить текущую скорость
        return self.speed

    def get_direction(self): #Получить текущее направление
        return self.direction


class Rowboat:
    def __init__(self, max_speed, max_passengers):
        self.max_speed = max(max_speed, 1)  # Минимальная скорость 1
        self.max_passengers = max(max_passengers, 1)  # Минимальное количество пассажиров 1
        self.passengers = []
        self.oars = Oars()
        self.is_moving = False
        self.speed = 0

    def add_passenger(self, passenger_name): #добавить пассажира в лодку
        assert len(self.passengers) < self.max_passengers, "Лодка переполнена"
        self.passengers.append(passenger_name)

    def remove_passenger(self, passenger_name): #убрать пассажира из лодки
        if passenger_name in self.passengers:
            self.passengers.remove(passenger_name)
        else:
            print("Пассажир не найден")

    def start_rowing(self, speed_change): #начать греблю
        self.oars.row(speed_change)
        self.speed = self.oars.get_speed()
        if self.speed > 0:
            self.is_moving = True
        else:
            self.is_moving = False

    def stop_rowing(self): #остановить греблю
        self.is_moving = False
        self.speed = 0

    def change_direction(self, new_direction): #изменить направление движения
        self.oars.change_direction(new_direction)

    def get_current_speed(self): #получить текущую скорость лодки
        return self.speed

    def get_current_direction(self): #получить текущее направление движения лодки
        return self.oars.get_direction()

    def get_passengers(self): #получить список текущих пассажиров в лодке
        return self.passengers

    def is_rowing(self): #получить текущее состояние лодки движется или нет
        return self.is_moving

# Пример использования
rowboat = Rowboat(10, 5)
rowboat.add_passenger("John")
rowboat.start_rowing(5)
print(f"Скорость: {rowboat.get_current_speed()} км/ч")
print(f"Направление: {rowboat.get_current_direction()}")
print(f"Пассажиры: {rowboat.get_passengers()}")
print(f"Лодка движется: {rowboat.is_rowing()}")