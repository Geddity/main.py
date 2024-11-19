import math

class Figure:
    sides_count = 0

    def __init__(self, color=(255, 255, 255), sides=None):
        self.__color = color
        self.filled = True
        if sides is None:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = [sides] * self.sides_count

    def __is_valid_color(self, r, g, b):
        if (isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
                and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if not self.__is_valid_color(r, g, b):
            print("введены некорректные данные")
        else:
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count or not all(isinstance(side, int) for side in new_sides):
            return False
        else:
            return True

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self, color=(255, 255, 255), sides=1):
        super().__init__(color, sides)
        self.__radius = sides / (math.pi * 2)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def __len__(self):
        return int(self.__radius * math.pi * 2)



class Triangle(Figure):
    sides_count = 3

    def __init__(self, color=(255, 255, 255), sides=1):
        super().__init__(color, sides)
        self.__sides = [sides] * self.sides_count

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)
        if len(new_sides) == self.sides_count and all(isinstance(side, int) for side in new_sides):
            self.__sides = new_sides

    def get_square(self):
        a, b, c = self.__sides
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(255, 255, 255), sides=1):
        super().__init__(color, sides)
        self.__sides = [sides] * self.sides_count

    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and all(isinstance(side, int) for side in new_sides):
            self.__sides = new_sides * self.sides_count

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        a = self.__sides[0]
        v = a ** 3
        return v

    def __len__(self):
        return self.__sides[0] * 12



circle1 = Circle((200, 200, 100),  10)
trian1 = Triangle((100,100,100), 7)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
print(circle1.get_sides())
print(f"Периметр: {len(circle1)}")
print(f"Площадь: {circle1.get_square()}")
print("\n")

trian1.set_sides(4, 5, 'a')
print(trian1.get_sides())
print(f"Периметр: {len(trian1)}")
print(f"Площадь: {trian1.get_square()}")
print("\n")

cube1.set_color(300, 70, 15)
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5, 4, 4, 5, 5, 7, 3, 2)
print(cube1.get_sides())
cube1.set_sides(4)
print(cube1.get_sides())
print(f"Периметр: {len(cube1)}")
print(f"Объем: {cube1.get_volume()}")
