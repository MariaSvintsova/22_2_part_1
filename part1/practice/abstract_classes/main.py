
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Boat(Transport):
    def start_engine(self):
        print('Катер громко затарахтел')

    def stop_engine(self):
        print('Двигатель катера приостоновлен')

    def move(self):
        print('Прохожие в ужасе разбегаются от очередного камикадзе')

    def stop(self):
        print('Двигатель катера чихнул напоследок и заглох')
class Car(Transport):
    def start_engine(self):
        print('Машина заурчала двигателем')

    def stop_engine(self):
        print('Машина остановилась')

    def move(self):
        print('Машина едет к цели назначения')

    def stop(self):
        print('Машина стоит с заглушенным двигателем')

class Electroscooter(Transport):
    def start_engine(self):
        print('Мигнул светодиодом')

    def stop_engine(self):
        print('Мигнул светодиодом дважды')
    def move(self):
        print('Прохожие в ужасе разбегаются от очередного камикадзе')

    def stop(self):
        print('Торможение об стену прошло успешно')

class Person:

    def use_transport(self, tr: Transport):
        tr.start_engine()
        tr.move()
        tr.stop_engine()
        tr.stop()


# Отрезок кода для самопроверки.
# Запустите его, после того как выполните задание
if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikadze)
