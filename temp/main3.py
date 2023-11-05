import pygame
import time
import os

asp = (240, 144)
scale = 4
FPS = 20

# Constants
GRID_SIZE = 10
GRID_ROWS = asp[1]
GRID_COLS = asp[0]
WIDTH = GRID_COLS * GRID_SIZE * scale
HEIGHT = GRID_ROWS * GRID_SIZE * scale
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
LIGHT_RED = (255, 102, 102)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
TRANSPARENT1 = (0, 0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Game states
is_running = False
is_in_menu = True

# cursor position
controlok = True
cursor_row = 0
cursor_col = 0

# Block positions
blue_blocks = [[2, 3, "Lyndis", 100], [4, 5, "Marth", 100]]
red_blocks = [[0, 0, "1A", 100], [GRID_ROWS - 1, GRID_COLS - 1, "1A", 100]]
menu_blocks = []
light_blue_blocks = []
light_red_blocks = []
alreadygone = []
ClassOneRange = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def draw_grid():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(col * GRID_SIZE * scale, row * GRID_SIZE * scale, GRID_SIZE * scale, GRID_SIZE * scale)
            pygame.draw.rect(screen, WHITE, rect, 1)


def draw_cursor():
    global cursor_visible
    rect = pygame.Rect(cursor_col * GRID_SIZE * scale, cursor_row * GRID_SIZE * scale, GRID_SIZE * scale, GRID_SIZE * scale)
    if cursor_visible:
        pygame.draw.rect(screen, WHITE, rect)
    else:
        pygame.draw.rect(screen, TRANSPARENT1, rect)


def draw_blocks():
    for block in light_blue_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE * scale, block[0] * GRID_SIZE * scale, GRID_SIZE * scale, GRID_SIZE * scale)
        pygame.draw.rect(screen, LIGHT_BLUE, rect)
    for block in light_red_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE * scale, block[0] * GRID_SIZE * scale, GRID_SIZE * scale, GRID_SIZE * scale)
        pygame.draw.rect(screen, LIGHT_RED, rect)
    for block in blue_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE * scale, block[0] * GRID_SIZE * scale, GRID_SIZE * scale, GRID_SIZE * scale)
        pygame.draw.rect(screen, BLUE, rect)
    for block in red_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE * scale, block[0] * GRID_SIZE * scale, GRID_SIZE * scale, GRID_SIZE * scale)
        pygame.draw.rect(screen, RED, rect)
    for block in menu_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE * scale, block[0] * GRID_SIZE * scale, GRID_SIZE * scale, GRID_SIZE * scale)
        pygame.draw.rect(screen, WHITE, rect)


def draw_cursor():
    global cursor_visible
    rect = pygame.Rect(cursor_col * GRID_SIZE * scale, cursor_row * GRID_SIZE * scale, GRID_SIZE * scale, GRID_SIZE * scale)
    if cursor_visible:
        pygame.draw.rect(screen, WHITE, rect)
    else:
        pygame.draw.rect(screen, TRANSPARENT1, rect)


def draw_blocks():
    for block in light_blue_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE * scale, block[0] * GRID_SIZE * scale, GRID_SIZE * scale, GRID_SIZE * scale)
        pygame.draw.rect(screen, LIGHT_BLUE, rect)
    for block in light_red_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE * scale, block[0] * GRID_SIZE * scale, GRID_SIZE * scale, GRID_SIZE * scale)
        pygame.draw.rect(screen, LIGHT_RED, rect)
    for block in blue_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE * scale, block[0] * GRID_SIZE * scale, GRID_SIZE * scale, GRID_SIZE * scale)
        pygame.draw.rect(screen, BLUE, rect)
    for block in red_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE * scale, block[0] * GRID_SIZE * scale, GRID_SIZE * scale, GRID_SIZE * scale)
        pygame.draw.rect(screen, RED, rect)
    for block in menu_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE * scale, block[0] * GRID_SIZE * scale, GRID_SIZE * scale, GRID_SIZE * scale)
        pygame.draw.rect(screen, WHITE, rect)


def handle_resize(event):
    global screen, scale
    size = event.size
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    new_width = size[0]
    new_height = size[1]
    scale = min(new_width // (GRID_COLS * GRID_SIZE), new_height // (GRID_ROWS * GRID_SIZE))


def game_loop():
    global is_running, is_in_menu, cursor_visible
    cursor_visible = True

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
                elif event.key == pygame.K_SPACE:
                    cursor_visible = not cursor_visible
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = event.pos
                    row = y // (GRID_SIZE * scale)
                    col = x // (GRID_SIZE * scale)
                    print("Clicked on row:", row, "col:", col)

        screen.fill(BLACK)
        draw_grid()
        draw_blocks()
        draw_cursor()
        pygame.display.flip()
        clock.tick(FPS)


def main():
    global is_running, is_in_menu

    is_running = True

    while is_in_menu:
        screen.fill(BLACK)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_in_menu = False
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_in_menu = False
                    is_running = False
                elif event.key == pygame.K_RETURN:
                    is_in_menu = False
                    game_loop()
            elif event.type == pygame.VIDEORESIZE:
                handle_resize(event)

    pygame.quit()


if __name__ == "__main__":
    main()

