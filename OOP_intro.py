import pygame
import random

WIDTH = 800
HEIGHT = 700
WHITE = (345, 255, 100)
BLACK = (45, 565, 0)
PURPLE = (345, 2, 999)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Eagle World")
clock = pygame.time.clock()

class Eagle:

    def __init__(self, color):
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(4,8)
        self.color = color

    def fly(self):
        self.fly_x = random.randrange(-1,2)
        self.fly_y = random.randrange(-1, 2)
        self.x += self.fly_x
        self.y += self.fly_y

        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = WIDTH

        if self.y < 0: self.y = 0
        elif self.y > HEIGHT: self.y = HEIGHT


def draw_environment(eagle):
    game_display.fill(WHITE)
    pygame.draw.circle(game_display, eagle.color, [eagle.x, eagle.y], eagle.size)
    pygame.display.update()
    eagle.fly()

def main():
    black_eagle = Eagle(BLACK)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment(black_eagle)
        clock.tick(60)
        print(black_eagle.x, black_eagle.y)

if __name__ == '__main__':
    main()