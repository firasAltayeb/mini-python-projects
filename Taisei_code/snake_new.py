import pygame
import random

screen_width = 380
screen_height = 300

grid_size = 20
grid_width = screen_width / grid_size
grid_height = screen_height / grid_size


def draw_grid(surface):
    for x in range(0, int(grid_width)):
        # Rect((left, top), (width, height))
        rectangle = pygame.Rect((0, x * grid_size),
                                (grid_size, grid_size))
        pygame.draw.rect(surface, (102, 255, 178), rectangle)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(
        (screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    time_out = 0
    while time_out < 10:
        clock.tick(1)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        # time_out = time_out + 1
        time_out += 1


main()
