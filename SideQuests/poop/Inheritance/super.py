class Shape:
    def __init__(self, color, is_filled) -> None:
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {
              'is_filled' if self.is_filled else 'not filled'}.")


class Circle(Shape):
    def __init__(self, color, is_filled, radius) -> None:
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {
              3.14 * self.radius * self.radius}cm^2.")
        return super().describe()


class Square(Shape):
    def __init__(self, color, is_filled, width) -> None:
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {
              self.width * self.width}cm^2.")
        return super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height) -> None:
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {
              (self.width * self.height) / 2}cm^2.")
        return super().describe()


circle = Circle(color="yellow", is_filled=True, radius=15)
square = Square(color="green", is_filled=True, width=9)
triangle = Triangle(color="purple", is_filled=False, width=12, height=11)
print(triangle.describe())
