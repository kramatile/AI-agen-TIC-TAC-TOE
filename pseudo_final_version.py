import pygame
import numpy as np
from algorithm import check_win, check_terminal, minimax
class Button:
    def __init__(self, x, y, width, height, text, button_color, text_color, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 32)
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.button_color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()
                    print(grid)
                    PLAYER = 'X'
                    pygame.time.delay(500)

NUMBERGRIDS = 3
BLACK = (0,0,0)
WHITE = (255,255,255)
SCREENWIDTH = 500
MARGIN = 10
WIDTH = HEIGHT = (SCREENWIDTH-(MARGIN*(NUMBERGRIDS+1)))/NUMBERGRIDS
PLAYER = 'X'
STATE = "CHOOSING" # CHOOSING , WIN , PLAYING
HUMAN = None


def generate_grid():
    for i in range(NUMBERGRIDS):
        for j in range(NUMBERGRIDS):
            grid[i][j] = 0

grid = []
for i in range(NUMBERGRIDS):
    grid.append([])
    for j in range(NUMBERGRIDS):
        grid[i].append(0)



pygame.init()
pygame.font.init()
font = pygame.font.Font("./MadimiOne-Regular.ttf", 64)
def draw_board():
    for i in range(NUMBERGRIDS):
            for j in range(NUMBERGRIDS):
                pygame.draw.rect(win,WHITE,(MARGIN+i*(WIDTH+MARGIN),MARGIN+j*(HEIGHT+MARGIN),WIDTH,HEIGHT))
                if(grid[i][j] == 1):
                    draw_X(i,j) 
                elif grid[i][j] == -1:
                    draw_O(i,j)
    if(grid[0][2] == 1):
        draw_X(0,2)
    if(grid[0][1] == 1):
        draw_X(0,1)
    if(grid[1][2] == 1):
        draw_X(1,2)
    if(grid[0][2] == -1):
        draw_O(0,2)
    if(grid[0][1] == -1):
        draw_O(0,1)
    if(grid[1][2] == -1):
        draw_O(1,2)

def draw_X(row, col):
    text_surface = font.render("X", True, BLACK)
    text_rect = text_surface.get_rect(center=((MARGIN + col * (WIDTH + MARGIN) + WIDTH // 2),
                                               (MARGIN + row * (WIDTH + MARGIN) + WIDTH // 2)))
    win.blit(text_surface, text_rect)

def draw_text(text, color, surface, x, y):
  """
  Draws text onto a surface at a given position.
  """
  text_surface = font.render(text, True, color)
  text_rect = text_surface.get_rect(center=(x, y))
  surface.blit(text_surface, text_rect)

def draw_O(row, col):
    text_surface = font.render("O", True, BLACK)
    text_rect = text_surface.get_rect(center=((MARGIN + col * (WIDTH + MARGIN) + WIDTH // 2),
                                               (MARGIN + row * (WIDTH + MARGIN) + WIDTH // 2)))
    win.blit(text_surface, text_rect)
def button_event_X():
    global STATE, HUMAN
    STATE = "PLAYING"
    HUMAN = "X"

def button_event_o():
    global STATE, HUMAN
    STATE = "PLAYING"
    HUMAN = "O"

win = pygame.display.set_mode((SCREENWIDTH,SCREENWIDTH))

XPlayer = Button(SCREENWIDTH  // 2 -200, SCREENWIDTH  // 2-50, 150, 100, "PLAY AS X", WHITE, BLACK,button_event_X)
YPlayer = Button(SCREENWIDTH  // 2 + 50, SCREENWIDTH  // 2 -50, 150, 100, "PLAY AS O",WHITE, BLACK,button_event_o)
restart = Button(SCREENWIDTH  // 2 , SCREENWIDTH  // 2 + 50, 100, 100, "restart", WHITE, BLACK,generate_grid)
pygame.display.set_caption("TIK TAK TOE")
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            y_cor = min(max(0, pos[0] // (WIDTH + MARGIN)), NUMBERGRIDS - 1)
            x_cor = min(max(0, pos[1] // (HEIGHT + MARGIN)), NUMBERGRIDS - 1)

            if grid[int(x_cor)][int(y_cor)] == 0 and STATE == "PLAYING":
                if PLAYER == 'X':
                    if HUMAN == "X":
                        grid[int(x_cor)][int(y_cor)] = 1
                        if not check_terminal(grid):
                            PLAYER = 'O'
                            # AI's turn
                            position = minimax(grid,-np.inf,np.inf, False)[1]
                            pygame.time.delay(200)
                            grid[position[0]][position[1]] = -1
                            PLAYER = 'X'
                            # Optional: Add a delay here to make AI's move more noticeable
                            pygame.time.delay(200)
                    elif HUMAN == "O":
                        # AI's turn
                        position = minimax(grid,-np.inf,np.inf, True)[1]
                        pygame.time.delay(200)
                        grid[position[0]][position[1]] = 1
                        PLAYER = 'O'
                        # Optional: Add a delay here to make AI's move more noticeable
                        pygame.time.delay(200)
                elif PLAYER == 'O':
                    if HUMAN == "O":
                        grid[int(x_cor)][int(y_cor)] = -1
                        if not check_terminal(grid):
                            PLAYER = 'X'
                            # AI's turn
                            position = minimax(grid,-np.inf,np.inf, True)[1]
                            pygame.time.delay(200)
                            grid[position[0]][position[1]] = 1
                            PLAYER = 'O'
                            # Optional: Add a delay here to make AI's move more noticeable
                            pygame.time.delay(200)
                    elif HUMAN == "X":
                        # AI's turn
                        position = minimax(grid,-np.inf,np.inf, False)[1]
                        pygame.time.delay(200)
                        grid[position[0]][position[1]] = 1
                        PLAYER = 'X'
                        # Optional: Add a delay here to make AI's move more noticeable
                        pygame.time.delay(200)
            print(" vous venez de clicker sur la colonne : "+str(int(y_cor))+" et la ligne : "+str(int(x_cor)))
        if(check_terminal(grid)== True):
            restart.handle_event(event)
            STATE = "CHOOSING"
        if STATE == "CHOOSING":
            XPlayer.handle_event(event)
            YPlayer.handle_event(event)
    win.fill(BLACK)
    if check_terminal(grid)==True:
        STATE = "WIN"
    if(check_terminal(grid) == False and STATE == "PLAYING")  :      
        draw_board()
    elif STATE == "WIN": 
        if check_win(grid) == None:
            draw_text("its a draw!",WHITE, win, SCREENWIDTH // 2, SCREENWIDTH//2)
            restart.draw(win)
        elif check_win(grid)==1 :
            draw_text("Player " + "X"+ " Wins!",WHITE, win, SCREENWIDTH  // 2, SCREENWIDTH //2)
            restart.draw(win)
        else:
            print(grid)
            draw_text("Player " + "O"+ " Wins!",WHITE, win, SCREENWIDTH  // 2, SCREENWIDTH //2)
            restart.draw(win)
    else :
        XPlayer.draw(win)
        YPlayer.draw(win)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()