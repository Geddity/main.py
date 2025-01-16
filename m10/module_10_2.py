import time
import threading

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy_counter = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        day_counter = 0

        while self.enemy_counter > 0:
            self.enemy_counter -= self.power
            day_counter += 1
            enemies_alive = self.enemy_counter - self.power

            if enemies_alive < 0:
                print(f"{self.name} одержал победу спустя {day_counter} дней(дня)!")
                break

            print(f"{self.name} сражается {day_counter} день(дня), осталось {enemies_alive} воинов.")
            time.sleep(1)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()