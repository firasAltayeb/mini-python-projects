import pygame
import random

screen_width = 380
screen_height = 380

grid_size = 20
grid_width = screen_width / grid_size
grid_height = screen_height / grid_size


def draw_grid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            # Rect((left, top), (width, height))
            if(x + y) % 2 == 0:
                rectangle = pygame.Rect((x * grid_size, y * grid_size),
                                        (grid_size, grid_size))
                pygame.draw.rect(surface, (93,216,228), rectangle)
            else:
                rectangle = pygame.Rect((x * grid_size, y * grid_size),
                                        (grid_size, grid_size))
                pygame.draw.rect(surface, (84,194,205), rectangle)


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(
        (screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    time_out = 0
    while time_out < 3:
        clock.tick(1)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        # time_out = time_out + 1
        time_out += 1


main()
