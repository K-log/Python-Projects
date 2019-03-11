import curses
import random
import time



def hud(win, score):
    win.addstr(1, 1, "Score: " + str(score))

def update_player(win_col, k, player):
    if k == ord("a") and player[2] >= 1:
        player[2] -= 1
    if k == ord("d") and player[2] <= win_col:
        player[2] += 1
    if k == ord("s"):
        player[3] = True

    return player

def main(stdscr):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    score = 0

    game_win = curses.newwin(0, 0)
    game_win.nodelay(True)
    game_win_max = game_win.getmaxyx()
    hud_win = curses.newwin(3, 11, 0, 0)
    hud_win.border()
    hud_win.nodelay(True)

    hud(hud_win, score)
    
    # Player = [Char, Y, X, Shoot]
    player = \
        [ \
        '^', game_win_max[0]-1, game_win_max[1]//2, False     \
        ]


    while True:
        game_win.clear()
        hud_win.clear()

        hud(hud_win, score)
       
        player[3] = False

        k = game_win.getch()
        
        if k == "Err":
            k = ""

        player = update_player(game_win_max[1], k, player)    
        
        game_win.addch(player[1], player[2], player[0])
        

        game_win.refresh()
        hud_win.refresh()
        time.sleep(0.1)
    
    curses.nocbreak()
    curses.echo()



if __name__ == "__main__":
    curses.wrapper(main)        


