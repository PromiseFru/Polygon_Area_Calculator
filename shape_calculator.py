class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return (self.width*self.height)
    
    def get_perimeter(self):
        return(2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return((self.width ** 2 + self.height ** 2) ** .5)

    # def get_picture(self):

    # def get_amount_inside(self):

    def __str__(self):
        result = "Rectangle(width={}, height={})".format(self.width, self.height)
        return result

# class Square:


rect = Rectangle(10,5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
# print(rect.get_picture())