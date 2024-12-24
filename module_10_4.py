import threading
import time
import random
from queue import Queue

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(1, 3))



class Table():

    def __init__(self, number, guest: Guest  = None):
        self.number = number
        self.guest = guest



class Cafe():
    queue = Queue()

    def __init__(self, *tbl_args):
        self.tables = tbl_args

    def guest_arrival(self, *guests):
        for g in guests:
            free_table = [t for t in self.tables if t.guest is None]
            if len(free_table):
                free_table[0].guest = g
                g.start()
                print(f'{g.name} сел(-а) за стол {free_table[0].number}')
            else:
                self.queue.put(g)
                print(f'{g.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or len([t for t in self.tables if t.guest is not None]) > 0:
            for t in self.tables:
                if t.guest is not None and not t.guest.is_alive():
                    print(f"{t.guest.name} покушал(-а) и ушёл (ушла)")
                    print(f"Стол {t.number} свободен")
                    t.guest = None
                    if not self.queue.empty():
                        tmp_guest = self.queue.get()
                        print(f"{tmp_guest.name} ушел из очереди и сел за стол номер {t.number}")
                        t.guest = tmp_guest
                        t.guest.start()



tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman','Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya',
                'Alexandra']
# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

