WIDTH = 600
HEIGHT = 600

# colours
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (96, 216, 232)

#boards
testboard = []
for x in range(9):
    testboard.append([0 for x in range(9)])

#positions and sizes
gridPos = (75, 100)
cellSize = 50
gridSize = cellSize*9
