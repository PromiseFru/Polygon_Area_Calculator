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

    def get_picture(self):
        W = ""
        L = ""

        for j in range(self.width):
            W += "*"
        for i in range(self.height):
            L += "{}\n".format(W)

        return L
    
    def count(self, pw, ph,cw,ch):
        width = int(pw/cw)
        height = int(ph/ch)
        result = width*height
        return result

    def get_amount_inside(self,shape):
        if (self.width<shape.width or self.height<shape.height):
            return 0
        count = self.count(self.width, self.height, shape.width, shape.height)
        return count

    def __str__(self):
        result = "Rectangle(width={}, height={})".format(self.width, self.height)
        return result

# class Square:


rect = Rectangle(12, 5)
rect2 = Rectangle(4,4)
print(rect.get_area())
# rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
print(rect.get_amount_inside(rect2))