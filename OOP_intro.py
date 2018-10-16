import pygame
import random
from eagle import Eagle

STARTING_BLACK_EAGLE = 10
STARTING_PURPLE_EAGLE = 3

WIDTH = 800
HEIGHT = 700
WHITE = (345, 255, 100)
BLACK = (45, 565, 0)
PURPLE = (345, 2, 999)

game_display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Eagle World")
clock = pygame.time.clock()


class BlackEagle(Eagle):
    def __init__(self, color, x_boundary, y_boundsry):
        super().__init__(color, x_boundary, y_boundary)
        self.color = BLACK

    def fly_high(self):
        self.x +=random.randrange(-7, 7)
        self.y +=random.randrange(-7, 7)

def draw_environment(eagle_list):
    game_display.fill(WHITE)

    for eagle_dict in eagle_list:
        for eagle_id in eagle_dict:
            eagle = eagle_dict[eagle_id]
            pygame.draw.circle(game_display, eagle.color, [eagle.x, eagle.y], eagle.size)
            eagle.fly_high()
            eagle.check_flies()

    pygame.display.update()


def main():
    black_eagle = dict(enumerate([BlackEagle(BLACK, WIDTH, HEIGHT) for i in range(STARTING_BLACK_EAGLE)]))
    purple_eagle = dict(enumerate([BlackEagle(PURPLE, WIDTH, HEIGHT) for i in range(STARTING_PURPLE_EAGLE)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_environment(black_eagle, purple_eagle)
        clock.tick(60)
        # print(black_eagle.x, black_eagle.y)

if __name__ == '__main__':
    main()