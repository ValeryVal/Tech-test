from Tech_test import Square, Rectangle, Circle
figu = {
    "square": Square,
    "rectangle": Rectangle,
    "circle": Circle,
}

inp = input("write figure")
if inp in figu.keys():
    # obrobka paramertiv dlia figur
    argums = {}
    for fig in figu.keys():
        if fig == inp:
            figure = figu[fig](kwargs=argums)
            figure.area()
            figure.perimeter()

rect = Rectangle([1, 2], [5, 7])
print(rect.perimeter())