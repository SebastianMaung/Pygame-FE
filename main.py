import random
import pygame 
#test 5
#import pygame_menu 
import time
import os 
main_game_running = True
#pygame_menu controls
#print(os.getcwd())
#os.chdir("E:\WaterEmblem")
#custom_theme = pygame_menu.themes.Theme(background_color=(0, 0, 0, 0))
import sys #only used for sys.exit()
def Constants():
    #scale = 2
    global InBattle, BLACK, WHITE, LIGHT_BLUE, LIGHT_RED, BLUE, RED, ORANGE, TRANSPARENT1,  FPS
    #scale = 3 
    InBattle = False
    #WIDTH = asp[0]*scale
    #HEIGHT = asp[1]*scale
    FPS = 60
    # Constants
    #WIDTH = asp[0]*scale
    #HEIGHT = asp[1]*scale
    #(WIDTH, HEIGHT)
    #GRID_SIZE = 10 * scale
    #GRID_ROWS = HEIGHT // GRID_SIZE
    #GRID_COLS = WIDTH // GRID_SIZE
    #(GRID_ROWS, GRID_COLS)
    ORANGE = (255, 128, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    LIGHT_BLUE = (173, 216, 230)
    LIGHT_RED = (255, 102, 102)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    TRANSPARENT1 = (0, 0, 0, 0)


# Initialize Pygame
scale = 3
def ReloadScale():
    global scale, GRID_SIZE, WIDTH, HEIGHT, GRID_ROWS, GRID_COLS, SCREENX, SCREENY, CenterOfScreen
    SCREENX, SCREENY = screen.get_size()
    #if SCREENX//asp[0] == SCREENY//asp[1] and not SCREENX//asp[0] == 0:
    #    scale = SCREENX//asp[0]
    #    ###print("OK")
    #else:
    #    scale = scale
    if SCREENX/asp[0] > 1:
        scale = SCREENX/asp[0]
    GRID_SIZE = 10 * scale
    WIDTH = asp[0]*scale
    HEIGHT = asp[1]*scale
    GRID_SIZE = 10 * scale
    GRID_ROWS = HEIGHT // GRID_SIZE
    GRID_COLS = WIDTH // GRID_SIZE
    if GRID_ROWS != 14:
        GRID_ROWS = 14
    if GRID_COLS != 26:
        GRID_COLS = 26
    SCREENX, SCREENY = screen.get_size()

    WIDTH = round(WIDTH, 0)
    HEIGHT = round(HEIGHT, 0)
    GRID_SIZE = int(round(GRID_SIZE, 0))
    GRID_ROWS = int(round(GRID_ROWS, 0))
    GRID_COLS = int(round(GRID_COLS, 0))
    #(GRID_ROWS, GRID_COLS)
    CenterOfScreen = (SCREENX//2, SCREENY//2)
    #(SCREENX//asp[0],"screenx divided by width")
    #(SCREENX)
    #(SCREENY//asp[1],"screeny divided by width")
    #(SCREENX,SCREENY)
pygame.init()
asp = (264,144)
screen = pygame.display.set_mode((1080, 720), pygame.RESIZABLE)
#SCREENX, SCREENY = screen.get_size()
#(SCREENX//asp[0],"screenx divided by width")
#(SCREENX,SCREENY)
#ReloadScale()
Constants()
start_time = pygame.time.get_ticks()
#GRID_SIZE = 10 * scale
#WIDTH = asp[0]*scale
#HEIGHT = asp[1]*scale

#GRID_ROWS = HEIGHT // GRID_SIZE
#GRID_COLS = WIDTH // GRID_SIZE

clock = pygame.time.Clock()

# Game states

is_running = False
is_in_menu = True
#timers
event_500ms = pygame.USEREVENT + 1
pygame.time.set_timer(event_500ms, 500)
event_5000ms = pygame.USEREVENT + 2
pygame.time.set_timer(event_5000ms, 5000)
# cursor position
controlok = True
cursor_row = 0
cursor_col = 0
global light_blue_blocks
# Block positions
blue_blocks = [[2, 3,"Lyndis",100, "Rank1Swords"], [4, 5,"Marth", 100, "Rank1Swords"]]
red_blocks = [[0, 0, "Footsoldier",100, "Rank1Swords"], [1,1, "Footsoldier",100, "Rank1Swords"]]
EnemyPositions = []
for i in range(len(red_blocks)):
    EnemyPositions.append((red_blocks[i][0],red_blocks[i][1]))
#print(EnemyPositions)
###print(red_blocks)
AdjacentBlocks = []
menu_blocks = []
light_blue_blocks = []
light_red_blocks = []
alreadygone = []
ClassOneRange = [(1,0), (0,1), (0,-1), (-1,0)]
def draw_grid():
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            rect = pygame.Rect(col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

def draw_cursor():
    global cursor_visible
    rect = pygame.Rect(cursor_col * GRID_SIZE, cursor_row * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    if cursor_visible:
        pygame.draw.rect(screen, WHITE, rect)
    else:
        pygame.draw.rect(screen, TRANSPARENT1, rect)

def draw_blocks():
    for block in light_blue_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE, block[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, LIGHT_BLUE, rect)
    for block in light_red_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE, block[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, LIGHT_RED, rect)
    for block in AdjacentBlocks:
        rect = pygame.Rect(block[1] * GRID_SIZE, block[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, ORANGE, rect)
    for block in blue_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE, block[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, BLUE, rect)

    for block in red_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE, block[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, RED, rect)
    for block in menu_blocks:
        rect = pygame.Rect(block[1] * GRID_SIZE, block[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, BLACK, rect)



#def AfterMoveMenu():

def show_menu():
    play_button_rect = pygame.Rect(WIDTH // 2 - 00, HEIGHT // 2 - 0, 100, 50)
    pygame.draw.rect(screen, WHITE, play_button_rect)
    font = pygame.font.Font(None, 36)
    text = font.render("Play", True, BLACK)
    text_rect = text.get_rect(center=play_button_rect.center)
    screen.blit(text, text_rect)

def start_game():
    global is_running, is_in_menu
    is_running = True
    is_in_menu = False


def start_cursor_blink():
    global blinkingc
    blinkingc = True

def stop_cursor_blink():
    global blinkingc
    global cursor_visible 
    blinkingc = False
    cursor_visible = True
def clearrange():
    light_red_blocks.clear()
    light_blue_blocks.clear()
    #DrawEverything()

def rangeout(range1, color=LIGHT_BLUE, x=None, y=None):
    global AdjacentBlocks  # Declare it as global
    if x is None:
        x = cursor_row
    if y is None:
        y = cursor_col

    color_blocks = {
        LIGHT_BLUE: light_blue_blocks,
        LIGHT_RED: light_red_blocks,
        ORANGE: AdjacentBlocks
        # Add more color options and corresponding block lists if needed
    }

    blocks = color_blocks.get(color, [])
    
    for i in range(range1):
        blocks.append((x - i - 1, y))
        blocks.append((x, y - i - 1))
        blocks.append((x, y + i + 1))
        blocks.append((x + i + 1, y))

        # Add elements to create the diamond shape
        for j in range(i):
            blocks.append((x - i + j, y - j - 1))
            blocks.append((x - i + j, y + j + 1))
            blocks.append((x + j + 1, y - i + j))
            blocks.append((x + j + 1, y + i - j))

    # Use a list to store the indices of blocks to remove
    indices_to_remove = []

    for i in range(len(blocks)):
        try:
            if (x, y) == (blocks[i][0], blocks[i][1]):
                indices_to_remove.append(i)
        except IndexError:
            pass

    # Remove the blocks with the stored indices in reverse order
    for idx in reversed(indices_to_remove):
        blocks.pop(idx)
    DrawEverything()
    #pygame.display.flip()



def attackrange(UnitClass):
    if UnitClass == "Rank1Swords":
        ##print("Lyndis, Class One")
        for i in range( len(ClassOneRange)):
            light_red_blocks.append((cursor_row + ClassOneRange[i][0], cursor_col + ClassOneRange[i][1]))
        ##print(light_red_blocks)
        draw_blocks()

def show_small_menu(options):
    selected_option = 0

    while True:
        screen.fill(TRANSPARENT1)
        draw_menu_options(options, selected_option)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_x:
                    return options[selected_option]

def draw_menu_options(options, selected_option):
    menu_font = pygame.font.Font(None, 36)
    for i, option in enumerate(options):
        text = menu_font.render(option, True, WHITE if i == selected_option else BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, (HEIGHT // 2) + i * 40))
        screen.blit(text, text_rect)

def DoNothing():
    pass



def draw_square(position, size, color):
    square_rect = pygame.Rect(position[0] * GRID_SIZE, position[1] * GRID_SIZE, size, size)
    pygame.draw.rect(screen, color, square_rect)


def csleep(amount):
    start_time = pygame.time.get_ticks()
    duration = amount  # Duration in milliseconds
    while pygame.time.get_ticks() - start_time < duration:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


def draw_rectangle(screen, width, height, color, JustGetDim=False):
    # Get the dimensions of the screen
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # Calculate the position of the rectangle's top-left corner to center it on the screen
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Create a rectangle surface
    rectangle = pygame.Surface((width, height))
    rectangle.fill(color)

    # Draw the rectangle on the screen
    if JustGetDim == False:
        return (x, y, width, height)
    else:
        screen.blit(rectangle, (x, y))
        return (x, y, width, height)  # Return the dimensions when JustGetDim is True



#def DisplayText(text, position):
#    font = pygame.font.Font(None, 24)  # Choose the font and size you want
#    text_surface = font.render(text, True, (255, 255, 255))  # Render the text
#    screen.blit(text_surface, position)  # Blit the text surface onto the screen


def DisplayText(screen, text, font_name, font_size, color, position, align="left", rotation=0):
    font = pygame.font.SysFont(font_name, font_size)
    text_surface = font.render(text, True, color)
    text_surface = pygame.transform.rotate(text_surface, rotation)

    if align == "center":
        text_rect = text_surface.get_rect(center=position)
    elif align == "right":
        text_rect = text_surface.get_rect(topright=position)
    else:
        text_rect = text_surface.get_rect(topleft=position)

    screen.blit(text_surface, text_rect)

def FriendlyAttackLogic(min=0, max=0, Class=""):
    if Class == "Rank1Swords":
        pass

    return ["Hit", 10]
    #For now, just a placeholder
def FightScene(EnemyPos):
    global EnemyPositions
    #print(EnemyPositions)
    #print(EnemyPos)
    #menu.disable()
    if not EnemyPos in EnemyPositions:
        raise Exception("EnemyPos not in EnemyPositions, must have attacked an empty space")
        #exit()
    RectDim = (200,100)
    ImgSize = (60, 40)
    #time.sleep(1)
    # Load and display the first GIF
    font = pygame.font.Font(None, 36)
    #gif1 = pygame.image.load("Swordmaster-Sword.gif")  # Replace "gif1.gif" with the actual file path of your first GIF
    pngs = sum(1 for file in os.listdir('assests/units/friendly/swordmaster-sword-a/') if file.endswith('.png'))
    gif1 = pygame.image.load("assests/units/friendly/swordmaster-sword-a/slash-0.png")  # Replace "gif1.gif" with the actual file path of your first GIF
    #text = font.render("Fire Embdlem: Blazing Sword", True, (255, 255, 255))
    wait = pygame.USEREVENT + 3
    pygame.time.set_timer(wait, 70)
    #a = 0
    i = 0
    for i in range (pngs):
        #(i)
        screen.fill((0, 0, 0, 0))
        csleep(70)
        pygame.time.delay(0)  # Delay in milliseconds (0.07 seconds)
        #pygame.time.delay(70)  # Delay in milliseconds (0.07 seconds)
        #draw_rectangle(screen, ImgSize[0]*scale*2, ImgSize[1]*scale*2, (220,220,220))
        gif1 = pygame.image.load("assests/units/friendly/swordmaster-sword-a/slash-"+str(i)+".png")  # Replace "gif1.gif" with the actual file path of your first GIF
        gif1 = pygame.transform.scale(gif1, (ImgSize[0]*scale*5, ImgSize[1]*scale*5))
        gif1_rect = gif1.get_rect()
        #(gif1_rect)
        gif1_rect = ((RectDim[0]-175)*scale, (RectDim[1]-105)*scale)  # Adjusting the position of the GIF may cause some issues with scaling and positioning
        screen.blit(gif1, gif1_rect)
        pygame.display.flip()
        i+=1
        if i > pngs-2:
            break

    # Load and display the second GIF
    screen.fill((0, 0, 0, 0))
    draw_rectangle(screen, RectDim[0]*scale, RectDim[1]*scale, (0, 98, 255))
    RectanglePos = draw_rectangle(screen, RectDim[0]*scale, RectDim[1]*scale, (0, 98, 255), JustGetDim=True)
    #(RectanglePos)
    #(scale, "scale")
    #exit()
    #(scale, WIDTH, HEIGHT)
    #exit()
    gif1 = pygame.image.load("assests/units/friendly/swordmaster-sword-a/slash-5.png")
    gif1 = pygame.transform.scale(gif1, (ImgSize[0]*scale*2, ImgSize[1]*scale*2))
    #ImgOne is on the right
    Nscale = 4.090909090909091
    ImgOneXOffset =  340/Nscale #-300 is original
    ImgOneYOffset = 50/Nscale #-200 is original
    ImgTwoXOffset = -30/Nscale
    ImgTwoYOffset = 50/Nscale
    #center1=(screen.get_width() // 2, screen.get_height()-1 //2)
    #(center1)
    scale_offset = scale * 2
    #mouse_pos = pygame.mouse.get_pos()
    #png dimensions are 240x160 pixels 
    gif1_rect = pygame.Rect(
        int((RectanglePos[0]) + ImgOneXOffset*scale),  # Apply the x-axis offset and scale
        int((RectanglePos[1]) + ImgOneYOffset *scale),  # Apply the y-axis offset and scale
        #int((0) * scale),  # Apply the x-axis offset and scale
        #int((0) * scale),  # Apply the x-axis offset and scale
        int(ImgSize[0] * scale_offset),  # Scale the width
        int(ImgSize[1] * scale_offset)   # Scale the height
    )
    screen.blit(gif1, gif1_rect)
    
    #(RectDim,"RECTDIM")
    #(scale,"SCALE")
    #gif1_rect = ((0-x_offset), (0-y_offset))  # Adjusting the position of the GIF may cause some issues with scaling and positioning
    #gif1 = pygame.transform.scale(gif1, gif1_rect.size)
    gif2 = pygame.image.load("assests/units/friendly/swordmaster-sword-a/slash-0.png")
    gif2 = pygame.transform.scale(gif2, (ImgSize[0]*scale*2, ImgSize[1]*scale*2))
    gif2 = pygame.transform.flip(gif2, True, False)
    gif2_rect = gif2.get_rect()
    gif2_rect = pygame.Rect(
        int((RectanglePos[0]) + ImgTwoXOffset*scale),  # Apply the x-axis offset and scale
        int((RectanglePos[1]) + ImgTwoYOffset *scale),  # Apply the y-axis offset and scale
        int(ImgSize[0] * scale_offset),
        int(ImgSize[1] * scale_offset)
    )
    #((gif2_rect[0]//scale+20) * scale,(RectanglePos[1]) + ImgTwoYOffset *scale)
    #gif2 = pygame.transform.scale(gif2, gif2_rect.size)
    screen.blit(gif2, gif2_rect)
    FriendlyAttackData = FriendlyAttackLogic()
    if FriendlyAttackData[0] == "Hit":
            DisplayText(screen, "Hit for "+str(FriendlyAttackData[1])+"!", "Arial", round(36.0//Nscale*scale)+1, (255, 255, 255), ((gif2_rect[0]//scale+20+5/5) * scale,gif2_rect[1]//scale*scale+3/3))
    ##print(EnemyPos)
    ##print(EnemyPositions)
    for i in range(len(EnemyPositions)):
        if EnemyPos == EnemyPositions[i]:
            ##print(EnemyPositions[i])
            ##print(red_blocks[i][3])
            red_blocks[i][3] = red_blocks[i][3] - FriendlyAttackData[1]
    
    ##print(red_blocks[i][3])

    # Display text on the screen
    text = font.render(" ", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 50))
    screen.blit(text, text_rect)
    pygame.display.flip()
    csleep(4000)
    screen.fill((0, 0, 0, 0))
    pygame.display.flip()


    '''
    i = 0
    max = 50
    while i < max:
        #("A")
        for event in pygame.event.get():
            if event.type == wait:
                ##print(i)

        #for i in range (pngs):
        #    if(i==pngs-1):
        #        break
                pygame.time.delay(1)  # Delay in milliseconds (0.07 seconds)
                i+=1
                if i < max:
                    break
                #(i)
    '''
    #exit()
    #ctime = pygame.time.get_ticks()
    #while pygame.time.get_ticks() - ctime < 10000:
        #a += 1
    #    draw_rectangle(screen, 0, 0, (255,255,255))
        #(a)

    #    clock.tick(60)  # Limits the frame rate to 60 FPS
    
    #(a)
    #if pygame.time.get_ticks()- start_time >= 5000:
    #    # Execute the desired action after the delay
    #    ##print("Delay finished")
        #running = False
    # Wait for a few seconds before ending the cutscene
    #a = 0
    #for i in range(0, 1000):
    #    pygame.time.delay(10)
    #    a += 1
#    menu.disable()


    #draw_square((cursor_row, cursor_col), GRID_SIZE, RED)
    #menu.disable()




#def print_cursor_position():
#    pass
    #mouse_pos = pygame.mouse.get_pos()
    #(scale)
    #("Cursor position:", mouse_pos)

start_cursor_blink()
stop_cursor_blink()
global cursor_visible 
cursor_visible = True
global selecting
global selectingEnemy
selectingEnemy = False
selecting = False
CurrentEnemyIAmSelecting = []
global id
id = ""
PlacedOnAnotherUnit = False
PlacedCorrectly = False
# Game loop
OldWindowSize = [SCREENX, SCREENY] = screen.get_size()
ReloadScale()
def MenuBack():
    global menu
    menu.disable()
    global selecting
    selecting = False
    global selectingEnemy
    selectingEnemy = False
    global id
    id = ""
    global PlacedOnAnotherUnit
    PlacedOnAnotherUnit = False
    global PlacedCorrectly
    PlacedCorrectly = False



#menu_options = []
selected_option = 0
ActionMenu = False
PressedOption = ""
# Function to draw the menu
def draw_menu():
    global LastSelectedUnit
    global PressedOption
    global menu_options
    global selected_option
    global controlok
    global AdjacentBlocks
    global EnemyPositions
    global cursor_row
    global cursor_col
    global red_blocks
    global ActionMenu
   # #print(cursor_row,cursor_col)
    AdjacentBlocks = []



    #if ActionMenu == False:
        #raise Exception("ActionMenu should be true")
    while ActionMenu:
        adjacent_positions = [
            [cursor_row - 1, cursor_col],
            [cursor_row + 1, cursor_col],
            [cursor_row, cursor_col - 1],
            [cursor_row, cursor_col + 1]
        ]
                                
        for i in range(len(adjacent_positions)):
            ##print(i)
            for block in red_blocks:
                if adjacent_positions[i] == block[:1]:
                    ##print(i)
                    ##print(block[:2], "LINE 593")
                    AdjacentBlocks.append(block[:2])
                    #selecting = True
                    selectingEnemy = True
                    rangeout(1, ORANGE)
                    ##print(i)
                    ##print("enemy unit adjacent")
        ##print(AdjacentBlocks)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_x:
                    
                    if ActionMenu:
                        ##print("You selected", menu_options[selected_option])
                        PressedOption = menu_options[selected_option]
                        if PressedOption== "Wait":
                            #DrawEverything()
                            ActionMenu = False
                            pass
                        if PressedOption== "Attack":
                            #DrawEverything()
                            ActionMenu = False
                            CurrentEnemyIAmSelecting = (cursor_row, cursor_col)
                            FightScene(CurrentEnemyIAmSelecting)

                        ##print(selected_option)
                        ActionMenu = False
                        DrawEverything()
                      #  raise Exception("ActionMenu should be false")
                        controlok = True
                    else:
                        print("ACTION 602")
                        ActionMenu = True

        if ActionMenu:
            controlok = False

            # Calculate the position and size of the menu box
            box_width = WIDTH // 4
            box_height = HEIGHT // 2
            box_x = (WIDTH - box_width) // 2
            box_y = (HEIGHT - box_height) // 2
            
            # Fill the inside of the box
            pygame.draw.rect(screen, WHITE, (box_x + 1, box_y + 1, box_width - 2, box_height - 2))
            
            # Draw the box
            pygame.draw.rect(screen, BLACK, (box_x, box_y, box_width, box_height), 3)
            
            # Draw the menu options
            font = pygame.font.Font(None, 12 * int(scale))
            for i, option in enumerate(menu_options):
                text = font.render(option, True, BLACK)
                text_rect = text.get_rect()
                text_rect.center = (WIDTH // 2, (HEIGHT // 2) + (i - 1) * scale * 11)
                screen.blit(text, text_rect)
                
                # Highlight the selected option
                if i == selected_option:
                    pygame.draw.rect(screen, BLACK, (text_rect.left - 10, text_rect.top - 5, text_rect.width + 20, text_rect.height + 10), int(scale) - 1)
            
        pygame.display.update()

def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5



def EnemyTurn():
    start_cursor_blink()
    EnemyMovementPath = []
    AmountOfSteps = 4
    AdjacentBlocks.clear()
    for i in range(len(red_blocks)):
        rangeout(AmountOfSteps+3, color=ORANGE, x=red_blocks[i][0], y=red_blocks[i][1])
        csleep(1000)
        nearest_blue_block = None
        min_distance = None
 
        for blue_block in blue_blocks:
            distance = calculate_distance(red_blocks[i][0], red_blocks[i][1], blue_block[0], blue_block[1])
 
            if min_distance is None or distance < min_distance:
                nearest_blue_block = blue_block
                min_distance = distance
 
        # Move towards the nearest blue block
        breakLoop = False
        EnemyMovementPath.append((red_blocks[i][0], red_blocks[i][1]))  # Save starting position
        while True:
            if breakLoop:
                #final checks to see if the enemy unit has ended up on top of another unit
                for red_block in red_blocks:
                    if tuple(red_block[:2]) in blue_blocks:
                        print("inside blue block!")
                        print("Final move")
                        red_block[:2] = EnemyMovementPath[-2]
                        breakLoop = True
                        break
                for l in range (len(red_blocks)):
                    if i != l and (red_blocks[i][0], red_blocks[i][1]) == (red_blocks[l][0], red_blocks[l][1]):
                        #print("I've ended up on top of another enemy unit!")
                        print("Final move") 
                        red_blocks[i][0] = EnemyMovementPath[-2][0]
                        red_blocks[i][1] = EnemyMovementPath[-2][1]
                        breakLoop = True
                        #print(bloc)
                        break 
                print("broke out!")
                DrawEverything()
                break
        #for j in range(AmountOfSteps): #amount of times to move
            csleep(100)
            if nearest_blue_block:
                if red_blocks[i][0] < nearest_blue_block[0]:
                    red_blocks[i][0] += 1
                elif red_blocks[i][0] > nearest_blue_block[0]:
                    red_blocks[i][0] -= 1
 
                elif red_blocks[i][1] < nearest_blue_block[1]:
                    red_blocks[i][1] += 1
                elif red_blocks[i][1] > nearest_blue_block[1]:
                    red_blocks[i][1] -= 1
                EnemyMovementPath.append((red_blocks[i][0], red_blocks[i][1]))
                #check if still inside adjacent blocks (range)
                if (red_blocks[i][0], red_blocks[i][1]) not in AdjacentBlocks:
                    break
                for k in range (len(blue_blocks)):
                    if (red_blocks[i][0], red_blocks[i][1]) == (blue_blocks[k][0], blue_blocks[k][1]):
                        print("inside blue block!")
                        red_blocks[i][0] = EnemyMovementPath[-2][0]
                        red_blocks[i][1] = EnemyMovementPath[-2][1]
                        breakLoop = True
                        break 
 
                for l in range (len(red_blocks)):
                    if i != l and (red_blocks[i][0], red_blocks[i][1]) == (red_blocks[l][0], red_blocks[l][1]):
                        #print("I've ended up on top of another enemy unit!")
                        red_blocks[i][0] = EnemyMovementPath[-2][0]
                        red_blocks[i][1] = EnemyMovementPath[-2][1]
                        breakLoop = True
                        #print(bloc)
                        break 
            k = 0
            l = 0
            for k in range (len(blue_blocks)):
                if (red_blocks[i][0], red_blocks[i][1]) == (blue_blocks[k][0], blue_blocks[k][1]):
                    print("inside blue block!")
                    red_blocks[i][0] = EnemyMovementPath[-2][0]
                    red_blocks[i][1] = EnemyMovementPath[-2][1]
                    breakLoop = True
                    break 
 
            for l in range (len(red_blocks)):
                if i != l and (red_blocks[i][0], red_blocks[i][1]) == (red_blocks[l][0], red_blocks[l][1]):
                    #print("I've ended up on top of another enemy unit!")
                    red_blocks[i][0] = EnemyMovementPath[-2][0]
                    red_blocks[i][1] = EnemyMovementPath[-2][1]
                    breakLoop = True
                    #print(bloc)
                    break 
           # breakLoop = True
            DrawEverything()
 
 
 
        #[[0, 0, 'Footsoldier', 100, 'Rank1Swords'], [1, 1, 'Footsoldier', 100, 'Rank1Swords']]
        #print(red_blocks)
        #check if enemy unit is on top of another friendly unit
 
        #check if enemy unit is on top of another enemy unit
 
 
        '''
        print("Enemy unit "+str(i)+" moved")
        if red_blocks[i][0] == nearest_blue_block[0] and red_blocks[i][1] == nearest_blue_block[1]:
            print("Enemy unit "+str(i)+" is attacking")
            FightScene((nearest_blue_block[0], nearest_blue_block[1]))
            #print("Enemy unit "+str(i)+" attacked")
            #print(red_blocks)
        '''
        #csleep(1000)
        #red_blocks[i][0] = EnemyMovementPath[-2][0]
        #red_blocks[i][1] = EnemyMovementPath[-2][1]
        #breakLoop = True
        DrawEverything()
        csleep(2000)
        AdjacentBlocks.clear()
        #print(i)
ActionMenu = False

def switch_turn():
    pygame.display.flip()
    global main_game_running
    global Turn 
    global TurnCount
    global ActionMenu
    ActionMenu = False
    DrawEverything()

    RectDim = (200, 50)
    if Turn == "Friendly":
        Turn = "Enemy"
    elif Turn == "Enemy":
        EnemyTurn()
        alreadygone.clear()
        #raise Exception("Turn works")
        Turn = "Friendly"
    TurnCount += 1

    # Display the turn banner
    banner_color = (255, 255, 255)  # White color for the banner background
    banner_pos = (screen.get_width() // 2, screen.get_height() // 2)  # Center of the screen
    banner_rotation = 0  # No rotation

    # Draw the grid (excluding menu, cursor, and menu draw)
    DrawEverything(exclude_menu=True, exclude_cursor=True, exclude_menu_draw=True)

    # Create and display the banner
    draw_rectangle(screen, RectDim[0]*scale, RectDim[1]*scale, banner_color, JustGetDim=True)
    DisplayText(screen, f"Turn {TurnCount}, {Turn}", "Arial", 30, (0, 0, 0), banner_pos, align="center", rotation=banner_rotation)

    # Update only the area where the banner will be drawn next
    pygame.display.update(pygame.Rect(banner_pos[0] - RectDim[0]//2, banner_pos[1] - RectDim[1]//2, RectDim[0], RectDim[1]))

    # Pause for a second before continuing the game
    csleep(1000)

 
def sortRoster():
    MyRoster = []
    for i in range (len(blue_blocks)):
        MyRoster.append(blue_blocks[i][2])
    MyRoster.sort()
    alreadygone.sort
    #print(MyRoster, alreadygone)
    if MyRoster == alreadygone:
        print("All units have moved")
        switch_turn()
        csleep(1000)

def DrawEverything(exclude_menu=False, exclude_grid=False, exclude_blocks=False, exclude_cursor=False, exclude_menu_draw=False):
    # pygame.display.flip()
    if not exclude_menu and is_in_menu:
        show_menu()
    elif not exclude_grid and is_running:
        draw_grid()
    if not exclude_blocks and is_running:
        draw_blocks()
    if not exclude_cursor and is_running:
        draw_cursor()
        if not exclude_menu_draw and ActionMenu:
            draw_menu()
    pygame.display.flip()
    #screen.fill(TRANSPARENT1)
    screen.fill(TRANSPARENT1)


TurnCount = 0
Turn = "Friendly"
while True:
    #global Turn
    sortRoster()
    MyRoster = []
    for i in range (len(blue_blocks)):
        MyRoster.append(blue_blocks[i][2])
    MyRoster.sort()
    alreadygone.sort()
    #print(MyRoster, alreadygone)
    global LastSelectedUnit
    global menu_options
    menu_options = ["Wait"]
    #print(alreadygone)
    if ActionMenu:
        pass
            #break
    if main_game_running:
        EnemyPositions = []
        for i in range(len(red_blocks)):
            EnemyPositions.append((red_blocks[i][0],red_blocks[i][1]))
        SCREENX, SCREENY = screen.get_size()
        #(SCREENX//asp[0],"screenx divided by width")
        #(SCREENX,SCREENY)
        NewWindowSize = [SCREENX, SCREENY]
        if NewWindowSize != OldWindowSize:
            ReloadScale()
            # (scale)
            #("window resized")
            #scree1n = pygame.display.set_mode((SCREENX, SCREENY), pygame.RESIZABLE)
            #scale = SCREENX//asp[0]

            OldWindowSize = NewWindowSize
        #scale = 3
        InBattle = False
        WIDTH = asp[0]*scale
        HEIGHT = asp[1]*scale
        #id = ""
        #scree1n = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        global blinkingc
        #blinkingc = True
        #start_cursor_blink()
        #stop_cursor_blink()
        #global cursor_visible
        #cursor_visible = cursor_visible
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == event_5000ms:
                pass
                #scree1n = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            if event.type == event_500ms and blinkingc:
                cursor_visible = not cursor_visible
            #print_cursor_position()
            if event.type == pygame.KEYDOWN:
                if is_in_menu and event.key == pygame.K_RETURN:
                    start_game()
                elif is_running:
                    if event.key == pygame.K_UP and cursor_row > 0 and controlok:
                        if cursor_row > 0 and controlok:
                            cursor_row -= 1
                        #selected_option = (selected_option - 1) % len(menu_options)
                        #cursor_row -= 1
                        #selected_option = (selected_option - 1) % len(menu_options)
                    elif event.key == pygame.K_DOWN:
                        if cursor_row < GRID_ROWS - 1 and controlok:
                            cursor_row += 1
                       # selected_option = (selected_option + 1) % len(menu_options)
                    elif event.key == pygame.K_LEFT and cursor_col > 0 and controlok:
                        cursor_col -= 1
                    elif event.key == pygame.K_RIGHT and cursor_col < GRID_COLS - 1 and controlok:
                        cursor_col += 1
                    elif event.key == pygame.K_x:
                        if ActionMenu:
                            #    #print("You selected", menu_options[selected_option])
                                ActionMenu = False
                                controlok = True
                        if selectingEnemy:
                            ##print("DD")
                            ##print(red_blocks, "red_blocks")
                            ##print(AdjacentBlocks[0], "AdjacentBlocks")
                            selectingEnemy = False
                            selecting = True
                           # #print("selecting enemy end")
                            if (cursor_row, cursor_col) in AdjacentBlocks and (cursor_row, cursor_col) in EnemyPositions:
                                ##print("MY COORDS ARE", cursor_row, cursor_col)
                                CurrentEnemyIAmSelecting = (cursor_row, cursor_col)
                                #print("CurrentEnemyIAmSelecting", CurrentEnemyIAmSelecting)
                                menu_options.append("Attack")
                                #menu.add.button('Attack', lambda: FightScene(CurrentEnemyIAmSelecting))

                            AdjacentBlocks=[]

                        if selecting: 
                            #("selecting end")
                            if (cursor_row, cursor_col) in light_blue_blocks: #if in range
                                ##print("attempting to place")
                                for i in range (len(blue_blocks)): #scan through blue blocks
                                    if (cursor_row, cursor_col) == (blue_blocks[i][0], blue_blocks[i][1]) or (cursor_row, cursor_col) == (red_blocks[i][0], red_blocks[i][1]): #if on another unit or enemy unit
                                        ##print("cannot place on another unit")
                                        PlacedOnAnotherUnit = True
                                        break
                                    #(id)
                                for i in range (len(blue_blocks)): 
                                    if id == blue_blocks[i][2] and not PlacedOnAnotherUnit: #while going through blue blocks, if id matches the id of the unit selected pop it and place it on the new grid space
                                        blue_blocks.pop(i)
                                        clearrange()
                                        stop_cursor_blink()
                                        selecting = False
                                        blue_blocks.append((cursor_row, cursor_col, id))
                                        alreadygone.append(id)
                                        ###print("selecting ended after placing correctly")
                                        PlacedCorrectly = True
                                        #attackrange(id)



                                        #menu.add.text_input('Name :', default='John Doe')
                                        #menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=DoNothing())
                                        #check if enemy units adjacent
                                        #menu = pygame_menu.Menu('Select', 400, 300,theme=pygame_menu.themes.THEME_BLUE)
                                        ##menu.add.button('Wait', menu.disable)
                                        #menu.add.button('Attack', menu.disable)
                                        #menu.mainloop(screen)
                                        break

                                    elif PlacedOnAnotherUnit:
                                        PlacedOnAnotherUnit = False
                                        break
                                ###print(cursor_row, cursor_col)
                                ###print(red_blocks)
                                ###print(WIDTH, HEIGHT)
                                #menu = pygame_menu.Menu('Select', WIDTH//scale, HEIGHT//scale,theme=pygame_menu.themes.THEME_BLUE)
                                #menu_options.append("Wait")
                                ##print(menu_options)
                                #menu.add.button('Wait', menu.disable)
                                
                                #start checking if enemy units are adjacent by looking through red blocks list
                                adjacent_positions = [
                                    [cursor_row - 1, cursor_col],
                                    [cursor_row + 1, cursor_col],
                                    [cursor_row, cursor_col - 1],
                                    [cursor_row, cursor_col + 1]
                                ]
                                
                                for i in range(len(adjacent_positions)):
                                    for block in red_blocks:
                                        if adjacent_positions[i] == block[:2]:
                                            ##print(i)
                                            ###print(block[:2], "LINE 593")
                                            AdjacentBlocks.append(block[:2])
                                            #selecting = True
                                            selectingEnemy = True
                                            rangeout(1, ORANGE)
                                            ###print(i)
                                            ###print("enemy unit adjacent")
                            if PlacedCorrectly and not selectingEnemy:
                                selected_option = (selected_option + 1) % len(menu_options)
                                print("ACTION 989")
                                ActionMenu = True
                                #draw_menu()

                               # menu.mainloop(screen)
                                selectingEnemy = False
                                PlacedCorrectly = False
                            
                        
                            ###print("selecting ended")
                            #return
                            stop_cursor_blink()
                            clearrange()
                            selecting = False
                        for i in range(len(blue_blocks)):
                            #(alreadygone)
                            if (cursor_row, cursor_col) == (blue_blocks[i][0], blue_blocks[i][1]):
                                LastSelectedUnit = blue_blocks[i]
                                ##print(LastSelectedUnit)
                                if blue_blocks[i][2] in alreadygone:
                                    ###print("unit already moved")
                                    break
                                clearrange()
                                
                                id = blue_blocks[i][2]
                                ####print(id) # id of unit selected
                                ####print("blue")
                                #(event.key)
                                selecting = True
                                #(light_blue_blocks)
                                rangeout(5, LIGHT_BLUE)
                                #rangeout(cursor_row + 1, cursor_col + 1, cursor_row + 1, cursor_col - 1, cursor_row - 1, cursor_col + 1, cursor_row - 1)
                                if blinkingc:
                                    stop_cursor_blink()
                                    selecting = False
                                else:
                                    start_cursor_blink()

                                    
                        #if is_cursor_blinking:
                        #    stop_cursor_blink()
                        #else:
                        #    start_cursor_blink()
            #(event.type)



            #if event.type == pygame.MOUSEMOTION and is_running:
            #    mouse_pos = pygame.mouse.get_pos()
            #    cursor_col = mouse_pos[0] // GRID_SIZE
            #    cursor_row = mouse_pos[1] // GRID_SIZE

    scaled_screen = pygame.transform.scale(screen, (WIDTH, HEIGHT))
    screen.blit(scaled_screen, (0, 0))
    #print(alreadygone)
    DrawEverything()    
        #draw_square((cursor_row, cursor_col), GRID_SIZE, RED)
    clock.tick(FPS)