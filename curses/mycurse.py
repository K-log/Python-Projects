import curses
from random import choice, randrange
from time import sleep, time

class Obstacle():
    obstacle_chars = ['V', 'Y']
    off_win = False


    def __init__(self, window):
        self.window = window
        self.row = 0
        self.col = randrange(0, window.getmaxyx()[1])
        self.obj_char = choice(self.obstacle_chars)
        self.max_win = window.getmaxyx()

    def _move(self):
        """Move the Obstacle down one row."""
        self.row += 1
        if self.row >= self.max_win[0]: 
            return True

        return False
    
    def _draw(self):
        """Draw the obstacle to the screen."""
        try:
            self.window.addch(self.row, self.col, self.obj_char)
        except Exception:
            pass

    def update(self, window):
#        if self.window != window:
#            self.window = window
        
        self.off_win = self._move()
        if not self.off_win:
            self._draw()

    def get_col(self):
        return self.col

    def get_row(self):
        return self.row

    def get_char(self):
        return self.obj_char

    def get_offwin(self):
        return self.off_win



class Player():
    projectiles = {}

    def __init__(self, window):
        self.window = window
        self.row = window.getmaxyx()[0] - 1
        self.col = window.getmaxyx()[1]//2 - 1
        self.char = '^'
        self.wait_time = time()
        self.max_win = window.getmaxyx() 

    def _move(self, k):
        if k == ord('a') and self.col > 1:
            self.col -= 1
        if k == ord('d') and self.col < self.max_win[1] - 1:
            self.col += 1
            
        if (time() - self.wait_time) > 1.0:
            self.wait_time = time()
            if k == ord('s'):
                self._shoot()

    def _draw(self):
       self.window.addch(self.row, self.col, self.char)

    def _shoot(self):
        col = self.col
        row = self.max_win[0] - 1
        proj = 'I'
        self.projectiles[(row, col)] = proj
    
    def update(self, window, k):
#        if self.window != window():
#            self.window = window

        self._move(k)
        self._draw()

        new = {}
        for (row, col), obj in self.projectiles.items():
            new_row = row-1
            if obj != "Del":
                if new_row <= 0:
                    self.projectiles[(row, col)] = "Del"
                new[(new_row, col)] = obj
                try:
                    self.window.addch(new_row, col, obj)
                except:                
                    self.projectiles[(row, col)] = "Del"

        self.projectiles = new 



class Game():
    obstacles = {}

    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.game_win = curses.newwin(0, 0)
        self.hud_win = curses.newwin(3, 11, 0, 0)
        self.score = 0
        self.wait_time = time()
        self.player = Player(self.game_win)
        self.game_win.nodelay(True)
        self.hud_win.nodelay(True)

    def _hud(self):
        self.game_win.clear()
        self.hud_win.border()
        self.hud_win.addstr(1, 1, "Score: " + str(self.score))
        
    def game_over(self):
        self.game_win.clear()

        go_msg = "GAME OVER!"
        score_msg = "You Score: " + str(self.get_score())
        replay_msg = "Press R to play again or Q to quit."

        go_w_pos = self.get_gwWidth()//2 - len(go_msg)//2
        go_h_pos = self.get_gwHeight()//2 - int(self.get_gwHeight() * 0.15)
        score_w_pos = self.get_gwWidth()//2 - len(score_msg)//2 
        score_h_pos = self.get_gwHeight()//2 #+ int(self.get_gwHeight())
        replay_w_pos = self.get_gwWidth()//2 - len(replay_msg)//2
        replay_h_pos = self.get_gwHeight()//2 + int(self.get_gwHeight() * 0.30)

        self.game_win.addstr(go_h_pos, go_w_pos, go_msg)
        self.game_win.addstr(score_h_pos, score_w_pos, score_msg)
        self.game_win.addstr(replay_h_pos, replay_w_pos, replay_msg)
        self.game_win.refresh()


    def update(self):
        self.game_win.clear()
        self._hud()
        
        k = self.game_win.getch()
        
        if k == "Err": 
            k = ""
       # TODO: Find some way to handle obstacle calculations in parallel 
        if (time() - self.wait_time) > 1.0:
            self.wait_time = time()
            n_obj = Obstacle(self.game_win)
            self.obstacles[(n_obj.get_row, n_obj.get_col)] = n_obj

        for (row, col), obj in self.obstacles.items():
            if obj != "Del":
                obj.update(self.game_win)
                if obj.off_win:
                    self.obstacles[(row, col)] = "Del"
                    self.score -= 1
        
        self.player.update(self.game_win, k)
        self.game_win.refresh()
        self.hud_win.refresh()


    def get_score(self):
        return self.score

    def get_gwHeight(self):
        return self.game_win.getmaxyx()[0]

    def get_gwWidth(self):
        return self.game_win.getmaxyx()[1] 




def main(stdscr):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)      # Set the cursor to a default starting position
    game = Game(stdscr)
    while True:             # Main event loop
        if game.get_score() < -99:
            game.game_over()
            sleep(5)
            break
        game.update()
        sleep(0.1)

    curses.nocbreak()
    curses.echo()



if __name__ == "__main__":
   curses.wrapper(main)

