import math
import pytest

class Figures:
    def __init__(self, name):
        self.name = name

    def perimeter(self):
        pass

    def area(self):
        pass

    def print_result(self):
        return f"{self.name} perimeter: {self.perimeter()} {self.name} area: {self.area()}"


class Square(Figures):

    def __init__(self, parameters):

        super().__init__("square")
        self.top_right = (parameters[0], parameters[1])
        self.side = parameters[2]
        assert self.side >= 0, "side cannot be negative"


    def perimeter(self) -> float:
        return self.side*4

    def area(self) -> float:
        return self.side**2


class Rectangle(Figures):

    def __init__(self, parameters):
        super().__init__("rectangle")
        self.top_right = (parameters[0], parameters[1])
        self.bottom_left = (parameters[2], parameters[3])

    def first_size(self):
        return abs(self.top_right[0]-self.bottom_left[0])

    def second_size(self):
        return abs(self.top_right[1]-self.bottom_left[1])

    def perimeter(self):
        return 2*(self.first_size())+2*(self.second_size())

    def area(self):
        return self.first_size()*self.second_size()


class Circle(Figures):

    def __init__(self, parameters):
        super().__init__("circle")
        self.radius = parameters[2]
        self.center = (parameters[0], parameters[1])



    def perimeter(self):
        return 2*math.pi*self.radius

    def area(self):
        return math.pi*self.radius**2


def test_square():
    square = Square([2, 3, 4])
    assert square.perimeter() == 16
    assert square.area() == 16

def test_result():
    square = Square([2, 3, 4])
    assert square.print_result() == "square perimeter: 16 square area: 16"

def test_rectangle_validation():
    rectangle = Rectangle([2, 3, 2, 3])
    assert rectangle.print_result() == "rectangle perimeter: 0 rectangle area: 0"

def test_square_validation():

    with pytest.raises(Exception):
        square = Square([2, 3, -1])



if __name__ == "__main__":
    figures = {"square": Square, "rectangle": Rectangle, "circle": Circle}
    figure_name = input("Write your figure:")

    if figure_name.lower() in figures:
        parameters = input("Write its parameters with a space between: ")
        splitted_param = parameters.split()
        end_param = []
        for i in splitted_param:
            end_param.append(int(i))
    else:
        print(f"Write correct figure from the list: {figures}")

    figure = None

    for key in figures:
        if figure_name.lower() == key:
            try:
                figure = figures[key](end_param)
            except Exception as e:
                print("error:", str(e))



    if figure:
        print(figure.print_result())

