class Oars: #Весла
    def __init__(self):
        pass

    def row(self):
        # Симуляция гребли
        return True

class Rowboat: #Лодка
    def __init__(self, capacity):
        self.capacity = capacity    #(вместимость) - максимальное количество людей
        self.current_load = 0       #(текущая загрузка) - текущее количество людей в лодке
        self.is_moving = False      #(движение) - состояние лодки (движется или нет)
        self.speed = 0              #(скорость) - скорость движения лодки
        self.oars = Oars()          #(Весла) -

    def add_passenger(self):        #добавить пассажира в лодку
        if self.current_load < self.capacity:
            self.current_load += 1
        else:
            raise Exception("Лодка переполнена")

    def remove_passenger(self):     #убрать пассажира из лодки
        if self.current_load > 0:
            self.current_load -= 1
        else:
            raise Exception("Нет пассажиров для удаления")

    def start_rowing(self, speed):  #начать греблю с заданной скоростью
        if self.current_load > 0:
            self.is_moving = True
            self.speed = speed

    def stop_rowing(self):          #остановить греблю
        self.is_moving = False
        self.speed = 0

    def get_status(self):           #получить текущее состояние лодки
        return {
            "capacity": self.capacity,
            "current_load": self.current_load,
            "is_moving": self.is_moving,
            "speed": self.speed,
        }