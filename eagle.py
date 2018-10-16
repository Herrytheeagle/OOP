import random

class Eagle:

    def __init__(self, color, x_boundary, y_boundary):

        self.size = random.randrange(4,8)
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)

    def fly(self):
        self.fly_x = random.randrange(-1,2)
        self.fly_y = random.randrange(-1, 2)
        self.x += self.fly_x
        self.y += self.fly_y

        if self.x < 0: self.x = 0
        elif self.x > self.x_boundary: self.x = self.x_boundary

        if self.y < 0: self.y = 0
        elif self.y > self.y_boundary: self.y = self.y_boundary
