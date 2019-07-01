import curses
import random
import time


def update(win_col, k, player):
    if k == ord("a") and player[2] >= 1:
        player[2] -= 1
    if k == ord("d") and player[2] <= win_col:
        player[2] += 1
    if k == ord("s"):
        player[3] = True

    return player

def draw_man(win, chances):
    parts = [(3,2), (3,0), (1,2), (1,0), (0,1)]
    man = [
        " O  ",
        "/|\\",
        " |  ",
        u"\u2143 L"
        ]
    
    for char in man:
        char[parts] = " "
        win.addstr(50, 50, char)


def main(stdscr):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    chances = 5

    game_win = curses.newwin(0, 0)
    #game_win.nodelay(True)
    board_win = curses.newwin(game_win.getmaxyx()[0]/2, game_win.getmaxyx()[1], 0, 0)
    board_win.border()
    #hud_win.nodelay(True)
    
    # Player = [Char, Y, X, Shoot]
    #player = ['^', game_win_max[0]-1, game_win_max[1]//2, False]


    while True:
        game_win.clear()
        board_win.clear()

        k = game_win.getch()

        game_win.refresh()
        board_win.refresh()
        time.sleep(0.1)
    
    curses.nocbreak()
    curses.echo()



if __name__ == "__main__":
    curses.wrapper(main)        


