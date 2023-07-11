# Robot Finds Kitten, Peter Wells

## CS-510, Computer Game Design, Homework #1

## 2023/07/09

---

## About

This is a simple Robot Finds Kitten style terminal game written in Python using the Curses library.

## Controls

Use W,A,S,D to move, and try to find the kitten! Press q to quit

## Setup / Running

This is a game designed to run in the command prompt / terminal. In order to play this game, you will need both Python and the Curses library installed on your machine.

First, download the latest [Python distribution](https://www.python.org/downloads/) and install it on your machine.

On some systems this is all the setup you need. On Windows, however, Python does not natively support the required `curses` library by default. If you are on a machine that already has the python curses library installed, then you should be able to skip this step. If you are on Windows, however, you will need to install windows-curses by doing the following:

- run `pip install -r requirements.txt` from the command line inside the directory OR
- run `pip install windows-curses`

Once ready, run the program with `python .\robot_kitten.py`

## Homework Questions

### ***Question 1: Pick a player experience and feeling to target for this simple game. For example, you might want to make it energizing instead of zenlike, make it a hard grind or a quick jaunt, etc.***

For the player experience I was going for a fairly faithful adaptation of the original but with an added sense of urgency and strategy. I wanted to make sure I kept some of the goofy charm of finding random objects but create a strategic element to the game.

<br>

---

### ***Question 2: What choices can you make in objects to enhance this experience? This could include the object's symbol as well as its description***

I decided to add variation in the colors displayed for the objects to entice players to seek out the objects. In addition, I decided to add a unique "visited" color and graphic so players can tell which objects they have visited and visualize their progress through the game. (with the added benefit that they will not waste their time going back to previously seen objects)

<br>

---

### ***Question 3: What one small and simple enhancement to the game mechanics might enhance the experience you are trying to provide?***

To increase the stakes a bit and add to the strategic element I was going for; I decided to add a turn counter and a limited number of turns. This means that players will have to strategize so that they have enough turns left to find the kitten. It also adds the potential for a game over which should incentivize them to play more strategically.

<br>

---

### ***Question 4: How confident are you that your game is (relatively) bug-free?***

I am semi-confident that the game is mostly (critical) bug free based on my testing. Though there are a few undesired behaviors such as turns decrementing when visiting the same object twice. I also believe the game was also not created in a way that is not the most efficient but that's mainly due to my inexperience with the curses api and game programming in general. More testing is required to push the limits of the game though.

<br>

---

### ***Question 5: What was the playtester's experience? Did it match your expectations?***

The playtesters I showed the game to enjoyed their time. I could tell that adding the timer created a little bit of tension as they searched for the kitten. But they also found the various object descriptions funny which I think matched the goofy yet tense experience that I was going for. Though I did observe some mild confusion with starting a game as they weren't sure which character they were and they took a minute to understand the controls (Controls are WASD so I think the confusion was mainly due to the fact they do not play many computer games). Things like this that I take for granted as the sole person working on this game helped to demonstrate the value of playtesting.

<br>

---

### ***Question 6: How does all this correlate with what you've read so far in The Book?***

I found it interesting to look at the idea of individual experiences in terms of game design. In the book, they talk about how everyone will have a different experience with your game and that part of the process is to take their experience and the desired experience and then bridge the gap between them. For this game, I think I was able to reach the playtesters with the desired experience. Though I also felt that it was watered down due to the limitations of the presentation style. I imagine if I had time to playtest with a broader range of players the gap in experiences between what I was trying to achieve and what the players experienced would become clearer. As is, while the experience I was going for was there, it is not quite vivid enough and could have been further emphasized with graphics, sound, and the game design decisions that come with that. I quite enjoyed viewing their reactions to my game and am looking forward to utilizing playtesting more often to really hone in on specific experiences in game design.

<br>

---

### ***Question 7: What would a "AAA" version of your game look like? Is what you have done here helpful in visualizing that? Is the playtesting you've done relevant?***

A AAA version of this game would look quite a bit different I imagine. Instead of simply having different text descriptions of the objects I imagine they would have full 3D graphics and interesting level design as well as real-time controls and timers. They would be able to sprinkle clues throughout the environment to point the player in the right direction and maybe even include a fog of war. Done well I think it could be a fun game; especially if they are able to keep the randomized levels. The core gameplay of finding goofy items on your search for the kitten is there but I think there would be a lot of ways to enhance the experience for the player in a AAA title. I feel like the playtesting done for this project may be helpful in some ways, but the experience would be so much richer in a AAA title that the testing here would overall not be relevant to that version of the game.

<br>

---

## Potential Future Developments

- Hide the objects and map from player so they have to search in the dark (fog of war)
- Add ASCII art kitty win screen


## References

- [Python Curses](https://docs.python.org/3/howto/curses.html)
- [Curses Programming in Python](https://www.devdungeon.com/content/curses-programming-python)
- [NCurses Programming HOWTO](http://www.ibiblio.org/pub/Linux/docs/HOWTO/other-formats/html_single/NCURSES-Programming-HOWTO.html#WHATIS)
