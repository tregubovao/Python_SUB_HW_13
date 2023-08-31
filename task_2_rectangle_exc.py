from os import system
system('cls')


class UnrealRectangleError(Exception):
    def __init__(self, lenght, width) -> None:
        self.lenght = lenght
        self.width = width
    
    def __str__(self) -> str:
        return f'Прямоугольника со сторонами {self.lenght} и {self.width} НЕ существует'


class Rectangle:
    def __init__(self, lenght: float, width: float = None) -> None:
        self.lenght = lenght
        if width == None:
            self.width = lenght
        else:
            self.width = width
        
    def square(self):
        if self.lenght > 0 and self.width > 0:
            return self.lenght * self.width
        raise UnrealRectangleError(self.lenght, self.width)
    
    def perimeter(self):
        if self.lenght > 0 and self.width > 0:
            return (self.lenght + self.width) * 2
        raise UnrealRectangleError(self.lenght, self.width)
    
    def __str__(self) -> str:
        return f'Прямоугольник со сторонами {self.lenght} и {self.width}'

r1 = Rectangle(2)
r2 = Rectangle(4, 2)
r3 = Rectangle(4, 0)

print(f'{r1} имеет площадь {r1.square()}')
print(f'{r2} имеет площадь {r2.square()}')
print(r3.perimeter())