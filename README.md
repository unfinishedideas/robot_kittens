# Homework #1 Robot Finds Kitten

## Peter Wells, CS-510, Computer Game Design

## 2023/07/09

---

## About

This is a simple Robot Finds Kitten style game written in Python using the Curses library.

## Controls

Use W,A,S,D to move, and try to find the kitten! Press q to quit

## Setup

Unfortunately, the Windows version of Python does not support the required `curses` library by default. If you are on Windows, you will need to install windows-curses to do so simply do the following:

- run `pip install -r requirements.txt` from the command line inside the directory OR
- Just run `pip install windows-curses`

## Potential DLC

- Hide the objects and map from player so they have to search in the dark
- Add ASCII art kitty win screen

## Homework Questions

### ***Question 1: Pick a player experience and feeling to target for this simple game. For example, you might want to make it energizing instead of zenlike, make it a hard grind or a quick jaunt, etc.***

For the player experience I was going for a fairly faithful adaptation of the original but with an added sense of urgency and strategy. I wanted to make sure I kept some of the goofy charm of finding random objects but create a strategic element to the game.

<br>

---

### ***Question 2: What choices can you make in objects to enhance this experience? This could include the object's symbol as well as its description***

For objects I decided to add variation in the colors displayed to give players a way to remember which objects they have already interacted with. In addition, I decided to add dynamic colors so players can tell which objects they have visited to not waste time going back to them.

<br>

---

### ***Question 3: What one small and simple enhancement to the game mechanics might enhance the experience you are trying to provide?***

To increase the stakes a bit and add to the strategic element I was going for; adding a turn counter is a good way to go. This means that players will have to strategize so that they have enough turns left to find the kitten.

<br>

---

### ***Question 4: How confident are you that your game is (relatively) bug-free?***

I am fairly certain it is mostly bug free based on my testing. Though I do believe it is created in a way that is not the most efficient.

<br>

---

### ***Question 5: What was the playtester's experience? Did it match your expectations?***



<br>

---

### ***Question 6: How does all this correlate with what you've read so far in The Book?***



<br>

---

### ***Question 7: What would a "AAA" version of your game look like? Is what you have done here helpful in visualizing that? Is the playtesting you've done relevant?***



<br>

---

## References

- [Python Curses](https://docs.python.org/3/howto/curses.html)
- [NCurses](http://www.ibiblio.org/pub/Linux/docs/HOWTO/other-formats/html_single/NCURSES-Programming-HOWTO.html#WHATIS)
- [Curses Programming in Python](https://www.devdungeon.com/content/curses-programming-python)
