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
NUM_OBJECTS = 5
GAME_OBJECTS = []
DESCRIPTIONS = [
    "Hi there, I'm an object of some kind", 
    "You found a D20!", 
    "That's a bar of soap", 
    "Golly Gee that's Mr T!", 
    "This is a very expensive microphone", 
    "That's a drumset. Ba-dum tish!", 
    "Congratulations, you've found yourself :)", 
    "Oh no, the Flying Spaghetti Monster! RUN!", 
    "This block contains a lawsuit from Nintendo of America", 
    "It's Radioactive Man. Up and atom!"
]
KITTEN_DESCRIPTION = "Hooray! You've found the Kitten. Congratulations on completing the game successfully"
ROBOT_GRAPHIC = '#'
KEY_UP = 'w'
KEY_DOWN = 's'
KEY_LEFT = 'a'
KEY_RIGHT = 'd'
DEBUG = True

# Important game-state globals, do not change!
CHOSEN_POSITIONS = []


# |-----------------------------------------------------------------------------------------------------------------|
class GameObject:
    x = 0
    y = 0
    is_kitten = False
    description = ""
    character = ''
    color = 0
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
        return(self.description, self.is_kitten)


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
        elif temp_y > BOARD_Y -1:
            temp_y = BOARD_Y - 1

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
    new_position = find_valid_coordinate()
    if DEBUG == True:
        GAME_OBJECTS.append(GameObject(new_position[0], new_position[1], True, KITTEN_DESCRIPTION, "K", random.randint(1,6)))
    else:
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
            CHOSEN_POSITIONS.append((temp_x, temp_y))
            return (temp_x, temp_y)


# |-----------------------------------------------------------------------------------------------------------------|
def gameloop(stdscr, game_window, title_window, player):
    game_on = True
    # game_window.refresh()
    # title_window.refresh()
    # draw_board(game_window, player)
    while game_on == True:
        input = stdscr.getch()
        if input == ord('q'):
            game_on = False
        else:
            update_message(title_window, "")
            result = player.move_player(input)
            if result is not None:
                update_message(title_window, result[0])
                # If kitten found, you win!
                if result[1] == True:
                    curses.napms(4000)
                    game_on = False

            draw_board(game_window, player)


def update_message(title_window, string):
    title_window.clear()
    title_window.addstr(0,0, "Robot Finds Kitten")
    title_window.addstr(1,0, string)
    title_window.refresh()


def draw_board(game_window, player):
    for i in range(1, BOARD_Y):
        for j in range(1, BOARD_X):
            # check for player at coord
            if player.x == j and player.y == i:
                game_window.addstr(i,j,ROBOT_GRAPHIC, curses.A_BLINK)
            else:
                # check for object at coord
                found = False
                for obj in GAME_OBJECTS:
                    if obj.x == j and obj.y == i:
                        game_window.addstr(i,j, obj.character)
                        found = True
                        break
                if found == False:
                    game_window.addstr(i, j, '.')
    game_window.refresh()


def collision_check(x, y):
    for obj in GAME_OBJECTS:
        if obj.x == x and obj.y == y:
            obj.debug_report()
            return (True, obj)
    return (False, None)


# |-----------------------------------------------------------------------------------------------------------------|
def main(stdscr):
    if NUM_OBJECTS > len(DESCRIPTIONS):
        print("Error! Too many objects and not enough descriptions. Either reduce NUM_OBJECTS or add more descriptions to DESCRIPTIONS")
        return
    # Setup  
    player = Player()
    generate_objects()
    curses.curs_set(0)
    title_window = curses.newwin(2, MAX_X,0,0)
    game_window = curses.newwin(MAX_Y, BOARD_X+1,2,0)
    game_window.border('|', '|', '-', '-', '+', '+', '+', '+')
    update_message(title_window, "")
    gameloop(stdscr, game_window, title_window, player)
    curses.endwin()

curses.wrapper(main)