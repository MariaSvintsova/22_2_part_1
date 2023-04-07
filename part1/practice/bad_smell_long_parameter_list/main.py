# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, y_coord, x_coord, speed, state, field):
        self.y_coord = y_coord
        self.x_coord = x_coord
        self.speed = speed
        self.state = state
        self.field = field

    def fly_or_crawl(self):
        if self.state == 'is_fly':
            self.speed *= 1.2
            return self.speed
        elif self.state == 'crawl':
            self.speed *= 0.5
            return self.speed
        elif 'is_fly' in self.state and 'crawl' in self.state:
            raise ValueError('Рожденный ползать летать не должен!')

    def move(self, direction):
        speed = self.fly_or_crawl()
        if direction == 'UP':
            new_y = self.y_coord + speed
            new_x = self.x_coord
        elif direction == 'DOWN':
            new_y = self.y_coord - speed
            new_x = self.x_coord
        elif direction == 'LEFT':
            new_y = self.y_coord
            new_x = self.x_coord - speed
        elif direction == 'RIGTH':
            new_y = self.y_coord
            new_x = self.x_coord
        self.field.set_unit(x=new_x, y=new_y, unit=self)


