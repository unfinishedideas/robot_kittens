import curses

ex = None

def main(stdscr):
    curses.curs_set(0)
    field = curses.newwin(21, 41, 1, 1)
    field.box()
    field.addstr(1, 1, "Hello, world!", curses.A_REVERSE) 
    field.refresh()
    field.getch()

curses.wrapper(main)
