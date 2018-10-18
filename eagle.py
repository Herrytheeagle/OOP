import random


class Eagle:

    def __init__(self, color, x_boundary, y_boundary, size_range=(4, 8), movement_range=(-1, 2)):
        self.size = random.randrange(size_range[0], size_range[1])
        self.movement_range = random.randrange(movement_range[0], movement_range[1])
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)

        def __repr__(self):
            return 'Eagle({}, {}, {}, {}))'.format(self.color,
                                                   self.size,
                                                   self.y,
                                                   self.x)

    def fly(self):
        self.fly_x = random.randrange(self.movement_range[0], self.movement_range[1])
        self.fly_y = random.randrange(self.movement_range[0], self.movement_range[1])
        self.x += self.fly_x
        self.y += self.fly_y

    def check_flies(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.x_boundary:
            self.x = self.x_boundary

        if self.y < 0:
            self.y = 0
        elif self.y > self.y_boundary:
            self.y = self.y_boundary