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

        if (self.width>50 or self.height>50):
            return "Too big for picture."

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

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, s_side):
        self.side = s_side
        super().__init__(s_side, s_side)

    def set_width(self, width):
        self.side = width

    def set_height(self, height):
        self.side = height

    def __str__(self):
        result = "Square(side={})".format(self.side)
        return result



# rect = Rectangle(10, 5)
# print(rect.get_area())
# rect.set_height(3)
# print(rect.get_perimeter())
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# rect.set_height(8)
# rect.set_width(16)
# print(rect.get_amount_inside(sq))