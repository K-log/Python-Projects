import curses
import os
import subprocess
from curses.textpad import Textbox, rectangle
from time import sleep

def get_command(stdscr, win):
    win.border()
    win.overlay(stdscr)
    k = ">"
    win.addch(1, 1, k)
    col = 2
    row = 1
    command = ""
    MAX_ROW = win.getmaxyx()[0] - 2
    MAX_COL = win.getmaxyx()[1] - 2
    while k != "\n":
        win.refresh()
        k = win.getch()
        k = chr(k)
        # Handle deleting characters
        if k == chr(127) and col > 1:
            col -= 1
            if col < 1:
                row -= 1
            win.delch(row, col)
        else:
            win.addch(row, col, k)
            command += k
            col += 1
        # Make sure we don't go out of the window bounds
        if col > MAX_COL:   
            col = 1
            row += 1
        if row > MAX_ROW:
            break
    win.clear()
    return command[:-1]



def main(stdscr):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(2)      # Set the cursor to a default starting position
    stdscr.addstr(0, 0, "Enter command: (hit ENTER to send)")
    y_max = stdscr.getmaxyx()[0]
    x_max = stdscr.getmaxyx()[1]
    y_2 = int(y_max/2)
    x_2 = int(x_max/2)
    y_4 = int(y_max/4)
    x_4 = int(x_max/4)
    y_8 = int(y_max/8)
    x_8 = int(x_max/8)
    command_win = curses.newwin(3, 30, y_8, x_2-15)
    command_win.border()
    command_win.overlay(stdscr)
    while True:             # Main event loop
        stdscr.clear()
        cmd = get_command(stdscr, command_win)
        stdscr.addstr(y_max-10, 1, cmd)
        result = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE)
        stdscr.addstr(y_max-11, 1, result.stdout)
        stdscr.refresh()
        sleep(1)

    curses.nocbreak()
    curses.echo()



if __name__ == "__main__":
   curses.wrapper(main)

