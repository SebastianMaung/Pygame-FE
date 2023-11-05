import pygame
import sys

# Constants
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 50
GRID_ROWS = HEIGHT // GRID_SIZE
GRID_COLS = WIDTH // GRID_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Game states
is_running = False
is_in_menu = True

# Player position
player_row = 0
player_col = 0

def draw_grid():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

def draw_player():
    rect = pygame.Rect(player_col * GRID_SIZE, player_row * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, WHITE, rect)

def show_menu():
    play_button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 25, 100, 50)
    pygame.draw.rect(screen, WHITE, play_button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Play", True, BLACK)
    text_rect = text.get_rect(center=play_button_rect.center)
    screen.blit(text, text_rect)

def start_game():
    global is_running, is_in_menu
    is_running = True
    is_in_menu = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if is_in_menu and event.key == pygame.K_RETURN:
                start_game()
            elif is_running:
                if event.key == pygame.K_UP and player_row > 0:
                    player_row -= 1
                elif event.key == pygame.K_DOWN and player_row < GRID_ROWS - 1:
                    player_row += 1
                elif event.key == pygame.K_LEFT and player_col > 0:
                    player_col -= 1
                elif event.key == pygame.K_RIGHT and player_col < GRID_COLS - 1:
                    player_col += 1

        if event.type == pygame.MOUSEMOTION and is_running:
            mouse_pos = pygame.mouse.get_pos()
            player_col = mouse_pos[0] // GRID_SIZE
            player_row = mouse_pos[1] // GRID_SIZE

    screen.fill(BLACK)

    if is_in_menu:
        show_menu()
    elif is_running:
        draw_grid()
        draw_player()

    pygame.display.flip()
    clock.tick(60)
