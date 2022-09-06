import math


class Figures:
    def __init__(self):
        pass

    def perimeter(self):
        pass

    def area(self):
        pass


class Square(Figures):

    def __init__(self, top_right: list, side: int):

        self.top_right = top_right
        self.side = side

    def perimeter(self) -> float:
        return self.side*4

    def area(self) -> float:
        return self.side**2


class Rectangle(Figures):

    def __init__(self, top_right: list, bottom_left: list):
        self.top_right = top_right
        self.bottom_left = bottom_left

    def first_size(self):
        return abs(self.top_right[0]-self.bottom_left[0])

    def second_size(self):
        return abs(self.top_right[1]-self.bottom_left[1])

    def perimeter(self):
        return 2*(self.first_size())+2*(self.second_size())

    def area(self):
        return self.first_size()*self.second_size()


class Circle(Figures):

    def __init__(self, center: list, radius: int):
        self.center = center
        self.radius = radius

    def perimeter(self):
        return 2*math.pi*self.radius

    def area(self):
        return math.pi*self.radius**2


if __name__ == "__main__":
    figures = ["square", "rectangle", "circle"]
    figure_name = input("Write your figure:")

    if figure_name.lower() in figures:
        parameters = input("Write its parameters with a space between: ")
        splitted_param = parameters.split()
        end_param = []
        for i in splitted_param:
            end_param.append(int(i))
    else:
        print(f"Write correct figure from the list: {figures}")

    if figure_name.lower() == "square":
        square = Square(list((end_param[0], end_param[1])), side=end_param[2])
        print("Square perimeter:", square.perimeter(),
              "Square area:", square.area())
    if figure_name.lower() == "rectangle":
        rectangle = Rectangle(list((end_param[0], end_param[1])), list((end_param[2], end_param[3])))
        print("Rectangle perimeter:", rectangle.perimeter(),
              "Rectangle area:", rectangle.area())
    if figure_name.lower() == "circle":
        circle = Circle(list((end_param[0], end_param[1])), end_param[2])
        print("circle perimeter:", circle.perimeter(),
              "circle area:", circle.area())

