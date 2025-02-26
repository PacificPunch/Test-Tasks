class Rowboat:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_load = 0
        self.is_moving = False
        self.speed = 0

    def add_passenger(self):
        if self.current_load < self.capacity:
            self.current_load += 1
        else:
            raise Exception("Лодка переполнена")

    def remove_passenger(self):
        if self.current_load > 0:
            self.current_load -= 1
        else:
            raise Exception("Нет пассажиров для удаления")

    def start_rowing(self, speed):
        if self.current_load > 0:
            self.is_moving = True
            self.speed = speed

    def stop_rowing(self):
        self.is_moving = False
        self.speed = 0

    def get_status(self):
        return {
            "capacity": self.capacity,
            "current_load": self.current_load,
            "is_moving": self.is_moving,
            "speed": self.speed,
        }