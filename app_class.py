import pygame
import sys

from settings import *


class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sudoku Game by jutencs")
        self.running = True
        self.grid = testboard
        self.selected = None
        self.mousePos = None
        self.state = "playing"

    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
        pygame.quit()
        sys.exit()

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouseOnGrid()
                if selected:
                    print(selected)
                    self.selected = selected
                else:
                    print("Nicht auf dem Feld")
                    self.selected = None

    def playing_update(self):
        self.mousePos = pygame.mouse.get_pos()

    def playing_draw(self):
        self.window.fill(WHITE)
        if self.selected:
            self.drawselection(self.window, self.selected)
        self.drawgrid(self.window)
        pygame.display.update()


    def drawselection(self, window, pos):
        pygame.draw.rect(window, BLUE, ((pos[0]*cellSize)+gridPos[0], (pos[1]*cellSize)+gridPos[1], cellSize, cellSize))

    def drawgrid(self, window):
        pygame.draw.rect(window, BLACK, (gridPos[0], gridPos[1], WIDTH-150, HEIGHT-150), 2)
        for x in range(9):
            if x % 3 == 0:
                pygame.draw.line(window, BLACK, (gridPos[0]+(x*cellSize), gridPos[1]), (gridPos[0]+(x*cellSize), gridPos[1]+450), 2)
                pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1]+(x * cellSize)), (gridPos[0]+450, gridPos[1]+(x * cellSize)), 2)
            pygame.draw.line(window, BLACK, (gridPos[0] + (x * cellSize), gridPos[1]), (gridPos[0] + (x * cellSize), gridPos[1] + 450))
            pygame.draw.line(window, BLACK, (gridPos[0], gridPos[1] + (x * cellSize)), (gridPos[0] + 450, gridPos[1] + (x * cellSize)))

    def mouseOnGrid(self):
        if self.mousePos[0] < gridPos[0] or self.mousePos[1] < gridPos[1]:
            return False
        elif self.mousePos[0] > gridPos[0]+gridSize or self.mousePos[1] > gridPos[1]+gridSize:
            return False
        return ((self.mousePos[0]-gridPos[0])//cellSize, (self.mousePos[1]-gridPos[1])//cellSize)