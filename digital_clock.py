import pygame
from math import pi, cos, sin
import datetime

WIDTH, HEIGHT = 1920, 1080

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Digital Clock")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def numbers(number, size, color, position):
    font = pygame.font.SysFont("DS-Digital", size, True, False)
    text = font.render(number, True, color)
    text_rect = text.get_rect(center=position)
    screen.blit(text, text_rect)


def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return int(x + WIDTH / 2 + 175), int(-(y - HEIGHT / 2))


def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        current_time = datetime.datetime.now()
        second = current_time.strftime('%S')
        minute = current_time.strftime('%M')
        hour = current_time.strftime('%I')
        am_pm = current_time.strftime('%p')
        weekday = current_time.strftime('%a')

        screen.fill(BLACK)

        numbers(f"{hour}:{minute}", 200, WHITE, (WIDTH / 2 - 100, HEIGHT / 2))
        numbers(second, 60, RED, (WIDTH / 2 + 175, HEIGHT / 2))
        numbers(am_pm, 60, WHITE, (WIDTH / 2 + 260, HEIGHT / 2 - 45))
        numbers(weekday[:-1], 60, WHITE, (WIDTH / 2 + 260, HEIGHT / 2 + 44))

        r = 45
        theta = int(second) * 360 / 60

        pygame.draw.circle(screen, WHITE, (int(WIDTH / 2 + 175), int(HEIGHT / 2)), r, 1)
        pygame.draw.circle(screen, RED, polar_to_cartesian(r, theta), 8)

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


main()