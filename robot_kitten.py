# # Peter Wells, CS-510 Computer Game Design, 2023/07/09
# # Homework 1: Robot Finds Kitten

# --- References Used ---
# https://docs.python.org/3/howto/curses.html
# http://www.ibiblio.org/pub/Linux/docs/HOWTO/other-formats/html_single/NCURSES-Programming-HOWTO.html#WHATIS

import curses
import random

# Change these values to alter the game
# MAX_X = 42
MAX_X = 100
MAX_Y = 24
BOARD_X = 40
BOARD_Y = 22
NUM_OBJECTS = 10
MAX_TURNS = 120
GAME_OBJECTS = []
DESCRIPTIONS = [
    "Hi there, I'm an object of some kind.", 
    "You found a mysterious D20! You rolled a 1.", 
    "That's a bar of soap.", 
    "Golly Gee that's Mr T!", 
    "This is a very expensive microphone.", 
    "That's a drumset. Ba-dum tish!", 
    "Congratulations, you've found yourself :)", 
    "Oh no, the Flying Spaghetti Monster! RUN!", 
    "This block contains a lawsuit from Nintendo of America.", 
    "It's Radioactive Man. Up and atom!",
    "It's a big box of la croix.",
    "It's a half eaten sandwhich, pretty tasty!",
    "You found one of Taylor Swift's ex boyfriends.",
    "You slipped on a banana peel!",
    "You found an adult cat! Too bad we want to find kittens.",
    "It's a copy of Earthbound for the Super Famicom.",
    "This is a Dungeons and Dragons rulebook. It's covered in cheeto dust."
]
KITTEN_DESCRIPTION = "Hooray! You've found the Kitten. Congratulations!"
GAME_OVER_TEXT = "GAME OVER. You ran out of turns :("
WELCOME_MESSAGE = "Welcome! You are the #. Use WASD to find the kitten! Press q at any time to quit"
ROBOT_GRAPHIC = '#'
ROBOT_COLOR = 8
VISITED_COLOR = 9
KITTEN_COLOR = 10
KEY_UP = 'w'
KEY_DOWN = 's'
KEY_LEFT = 'a'
KEY_RIGHT = 'd'

DEBUG = False
DEBUG_KITTEN_X = 1
DEBUG_KITTEN_Y = 1

# Important game-state globals, do not change!
CHOSEN_POSITIONS = []
NUM_COLORS = 1


# |-----------------------------------------------------------------------------------------------------------------|
class GameObject:
    x = 0
    y = 0
    is_kitten = False
    description = ""
    character = ''
    color = random.randint(1,NUM_COLORS)
    def __init__(self, pos_x, pos_y, is_kitten_input, description_input, character_input, color_input):
        self.x = pos_x
        self.y = pos_y
        self.is_kitten = is_kitten_input
        self.description = description_input
        self.character = character_input
        self.color = color_input
    
    def debug_report(self):
        if DEBUG == True:
            print(f"X = {self.x}, Y = {self.y}, character = {self.character}, is_kitten = {self.is_kitten}, color = {self.color}")
            print(f"Display Message: {self.description}\n")
    
    def get_interaction(self):
        return(self.description, self.is_kitten, self.x, self.y, self.character)


# |-----------------------------------------------------------------------------------------------------------------|
class Player:
    x = 0
    y = 0
    def __init__(self):
        result = find_valid_coordinate()
        self.x = result[0]
        self.y = result[1]

    def move_player(self, key_pressed):
        temp_x = self.x
        temp_y = self.y
        if key_pressed == ord(KEY_UP):
            temp_y -= 1
        elif key_pressed == ord(KEY_DOWN):
            temp_y += 1
        elif key_pressed == ord(KEY_LEFT):
            temp_x -= 1
        elif key_pressed == ord(KEY_RIGHT):
            temp_x += 1

        # Check for oob
        if temp_x < 1:
            temp_x = 1
        elif temp_x > BOARD_X - 1:
            temp_x = BOARD_X - 1
        if temp_y < 1:
            temp_y = 1
        elif temp_y > BOARD_Y:
            temp_y = BOARD_Y

        # Check for object collision
        result = collision_check(temp_x, temp_y)
        if not result[0]:
            self.x = temp_x
            self.y = temp_y
        else:
            interaction = result[1].get_interaction()
            return interaction


# |-----------------------------------------------------------------------------------------------------------------|
def generate_objects():
    # Generate random objects
    for x in range(NUM_OBJECTS):
        new_position = find_valid_coordinate()
        description = random.choice(DESCRIPTIONS)
        DESCRIPTIONS.remove(description)
        GAME_OBJECTS.append(GameObject(new_position[0], new_position[1], False, description, generate_graphic(), random.randint(1,6)))

    # Add Kitten
    if DEBUG == True:
        GAME_OBJECTS.append(GameObject(DEBUG_KITTEN_X, DEBUG_KITTEN_Y, True, KITTEN_DESCRIPTION, "K", random.randint(1,6)))
    else:
        new_position = find_valid_coordinate()
        GAME_OBJECTS.append(GameObject(new_position[0], new_position[1], True, KITTEN_DESCRIPTION, generate_graphic(), random.randint(1,6)))


# TODO: Ensure that control characters cannot be selected
def generate_graphic():
    # rand = random.randint(0, 10000)
    # return chr(rand)
    return 'O'


def find_valid_coordinate():
    while True:
        temp_x = random.randint(1, BOARD_X -1)
        temp_y = random.randint(1, BOARD_Y - 1)
        if (temp_x, temp_y) not in CHOSEN_POSITIONS:
            if DEBUG and temp_x == DEBUG_KITTEN_X and temp_y == DEBUG_KITTEN_Y:
                continue
            CHOSEN_POSITIONS.append((temp_x, temp_y))
            return (temp_x, temp_y)


# |-----------------------------------------------------------------------------------------------------------------|
def gameloop(stdscr, game_window, title_window, player):
    game_on = True
    turns_left = MAX_TURNS

    # Set up the UI and the game board
    update_message(title_window, WELCOME_MESSAGE, turns_left)
    draw_board(game_window)
    game_window.addch(player.y, player.x, ROBOT_GRAPHIC, curses.color_pair(ROBOT_COLOR))

    while game_on:
        p_input = game_window.getch()
        prev_x = player.x
        prev_y = player.y

        # Either we're quitting...
        if p_input == ord('q'):
            game_on = False
        # Or it's a new turn!
        else:
            update_message(title_window, "", turns_left)
            # Move the player, update the graphic behind them
            result = player.move_player(p_input)
            game_window.addch(prev_y, prev_x, '.')
            game_window.addch(player.y, player.x, ROBOT_GRAPHIC, curses.color_pair(ROBOT_COLOR))

            # If we have collided with something, display the message
            if result is not None:
                # If the kitten was found, you win!
                if result[1] == True:
                    update_message(title_window, result[0], turns_left, 2)
                    draw_win(game_window, result[2], result[3])
                    game_window.refresh()
                    curses.napms(4000)
                    game_on = False
                else:
                    # Change the object's graphic to a visited one
                    update_message(title_window, result[0], turns_left)
                    game_window.addch(result[3], result[2], 'x', curses.color_pair(VISITED_COLOR))

            # Decrement Turn counter and check for game over
            turns_left -= 1
            if turns_left < 0:
                update_message(title_window, GAME_OVER_TEXT, 0, 7)
                curses.napms(4000)
                game_on = False
        game_window.refresh()


def draw_win(game_window, pos_x, pos_y):
    top = pos_y + 1
    bottom = pos_y - 1
    right = pos_x + 1
    left = pos_x - 1

    if top > BOARD_Y:
        top = pos_y
    if right > BOARD_X:
        right = pos_x
    if bottom < 0:
        bottom = 0
    if left < 0:
        left = 0

    game_window.addch(pos_y, pos_x, 'O', curses.color_pair(KITTEN_COLOR))
    game_window.addch(top, pos_x, 'O', curses.color_pair(KITTEN_COLOR))
    game_window.addch(bottom, pos_x, 'O', curses.color_pair(KITTEN_COLOR))
    game_window.addch(pos_y, right, 'O', curses.color_pair(KITTEN_COLOR))
    game_window.addch(pos_y, left, 'O', curses.color_pair(KITTEN_COLOR))


def draw_board(game_window):
    game_window.erase()
    game_window.border('|', '|', '-', '-', '+', '+', '+', '+')
    for i in range(1, BOARD_Y + 1):
        for j in range(1, BOARD_X):
            # check for object at coord
            found = False
            for obj in GAME_OBJECTS:
                if obj.x == j and obj.y == i:
                    game_window.addch(i,j, obj.character, curses.color_pair(obj.color))
                    found = True
                    break
            if found == False:
                game_window.addch(i, j, '.')

    game_window.refresh()


def update_message(title_window, string, turns_left, color=1):
    title_window.erase()
    title_window.addstr(0,0, f"Robot Finds Kitten. Turns left [{turns_left}]")
    title_window.addstr(1,0, string, curses.color_pair(color))
    title_window.refresh()


def collision_check(x, y):
    for obj in GAME_OBJECTS:
        if obj.x == x and obj.y == y:
            obj.debug_report()
            return (True, obj)
    return (False, None)

def setup_colors():
    curses.start_color()
    # 0:black, 1:red, 2:green, 3:yellow, 4:blue, 5:magenta, 6:cyan, and 7:white
    # We do 1 less because color 8 is reserved for the robot
    NUM_COLORS = 7
    ROBOT_COLOR = 8
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_RED, curses.COLOR_BLACK)
    # Color pair for the Robot graphic
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_CYAN)
    # Color pair for visited objects
    curses.init_pair(9, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # Color pair for kitten
    curses.init_pair(10, curses.COLOR_BLUE, curses.COLOR_GREEN)


# |-----------------------------------------------------------------------------------------------------------------|
def main(stdscr):
    if NUM_OBJECTS > len(DESCRIPTIONS):
        print("Error! Too many objects and not enough descriptions. Either reduce NUM_OBJECTS or add more descriptions to DESCRIPTIONS")
        return
    # Setup  
    player = Player()
    setup_colors()
    generate_objects()
    curses.curs_set(0)
    title_window = curses.newwin(2, MAX_X, 0, 0)
    game_window = curses.newwin(MAX_Y, BOARD_X+1, 2, 0)
    gameloop(stdscr, game_window, title_window, player)
    curses.endwin()

curses.wrapper(main)