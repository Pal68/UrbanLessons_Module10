import threading
import random
import time

class Bank():
    balance: int
    lock: threading.Lock()

    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(1, 101):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            inc_balance = random.randint(50, 500)
            self.balance = self.balance + inc_balance
            print(f"Пополнене {inc_balance}. Баланс {self.balance}")
            time.sleep(0.001)

    def take(self):
        for i in range(1, 101):
            dec_balance = random.randint(50, 500)
            print(f"Запрос на {dec_balance}")
            if dec_balance <= self.balance:
                self.balance = self.balance - dec_balance
                print(f"Снятие {dec_balance}. Баланс {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)



sber = Bank(0)

thread1 = threading.Thread(target = Bank.deposit, args = (sber, ))
thread2 = threading.Thread(target = Bank.take, args = (sber, ))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Итоговый баланс: {sber.balance}")


