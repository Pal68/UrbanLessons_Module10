import threading
from threading import Thread
import time

class Knight(threading.Thread):
    def __init__(self, name = '', power = 0):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        number_of_enemies = 100
        current_enemies = number_of_enemies
        while current_enemies > 0:
            current_enemies = current_enemies - self.power
            print(f"{self.name} сражается {(number_of_enemies - current_enemies)/self.power} дней(дня) "
                  f"осталось {current_enemies} врагов \n")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {number_of_enemies/self.power} дней(дня)!")

first_knight = Knight('Sir Ilia Muromerts', 10)
second_knight = Knight("Sir Dobrunya Nikitich", 20)

first_knight.start()
second_knight.start()



