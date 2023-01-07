import pygame

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# BLOCK_COLOR
B = (137, 82, 199)
# SIDEWALK_COLOR
S = (141, 174, 210)
# ROAD_COLOR
R = (104, 105, 107)

# SCREEN Def:
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TAXI CAB GAME")

# game board:
GB_COLUMNS = 3
GB_ROWS = 3

# DEF MAP :
# ---------------------------------------------------------------------------------
# !important note!: i don't use the whole 9X9 table -> only the 3X3 game board!!!!!!
# try to fix after the graphic level!!!!!
# ---------------------------------------------------------------------------------
MAP_COLUMNS = 9
MAP_ROWS = 9
# needs a loop to separate the different values in each array
MAP_info = [[0 for column in range(MAP_COLUMNS)] for row in range(MAP_ROWS)]
# inserting the in rectangles (general) info
for row in range(MAP_ROWS):
    for column in range(MAP_COLUMNS):
        MAP_info[row][column] = pygame.Rect(200 * row, 200 * column, WIDTH / 3, HEIGHT / 3)

# TAXI:
taxi_width = 150
taxi_height = 150
taxi = pygame.Rect(
    WIDTH / GB_COLUMNS + (WIDTH / GB_COLUMNS - taxi_width) / 2,
    HEIGHT / GB_ROWS + (HEIGHT / GB_ROWS - taxi_height) / 2,
    taxi_width, taxi_height)
taxi_VEL = 1

def minimap_scope(starting_gamecell_x, starting_gamecell_y, rest_x, rest_y):

    MAP_info[starting_gamecell_x][starting_gamecell_y]

    return  #size and place temp rect

def draw_window(cursor):
    gameboard_fill_x = 0

    brush_x = 0
    brush_y = 0

    # game MAP:
    MAP_COLORS = [
        [B, S, R, S, B, S, R, S, B],
        [S, S, R, S, S, S, R, S, S],
        [R, R, R, R, R, R, R, R, R],
        [S, S, R, S, S, S, R, S, S],
        [B, S, R, S, B, S, R, S, B],
        [S, S, R, S, S, S, R, S, S],
        [R, R, R, R, R, R, R, R, R],
        [S, S, R, S, S, S, R, S, S],
        [B, S, R, S, B, S, R, S, B]
    ]

    WIN.fill(WHITE)

    # Finding The beginning of labor on top of the big map (starting game cell & the rest of each axis)
    # Starting game cell:
    for c in range(MAP_COLUMNS):
        if c * 200 <= cursor[0] < (c * 200) + 199:
            starting_gamecell_x = c
    for r in range(MAP_ROWS):
        if r * 200 <= cursor[1] < (r * 200) + 199:
            starting_gamecell_y = r
    # The rest of each axis:
    rest_x = cursor[0] % 200
    rest_y = cursor[0] % 200

    # Printing the Game board
    while gameboard_fill_x < WIDTH:
        for brush_x
            for brush_y
            pygame.draw.rect(WIN,
                             MAP_COLORS[starting_gamecell_x + brush_x][starting_gamecell_y + brush_y],
                             minimap_scope(starting_gamecell_x, starting_gamecell_y, rest_x, rest_y))


    for row in range(GB_ROWS):
        for column in range(GB_COLUMNS):
            pygame.draw.rect(
                WIN, MAP_COLORS[row + cursor[0]][column + cursor[1]], MAP_info[row][column])

    # taxi player
    pygame.draw.rect(WIN, BLACK, taxi)

    pygame.display.update()


def taxi_handle(cursor, keys_pressed):
    if keys_pressed[pygame.K_UP]:  # UP
        cursor[1] -= taxi_VEL
    if keys_pressed[pygame.K_DOWN]:  # DOWN
        cursor[1] += taxi_VEL
    if keys_pressed[pygame.K_RIGHT]:  # RIGHT
        cursor[0] += taxi_VEL
    if keys_pressed[pygame.K_LEFT]:  # LEFT
        cursor[0] -= taxi_VEL


def main():
    start_x = 0
    start_y = 0
    cursor = [start_x, start_y]
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        # events in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Checking onetime key pressed
            # if event.type == pygame.KEYDOWN:

        keys_pressed = pygame.key.get_pressed()
        # Functions to handle the different objects
        taxi_handle(cursor, keys_pressed)
        print(cursor)

        # Draw on the screen function
        draw_window(cursor)

    pygame.quit()


if __name__ == "__main__":
    main()
