import pygame as pyg
import numpy as np
import time

WIDTH, HEIGHT = 1200, 600

COLUMNS, ROWS = 100, 50

white = (255, 255, 255)
gray = (20, 20, 20)
black = (0, 0, 0)
light_gray = (90, 90, 90)
lighter_gray = (60, 60, 60)
light_blue = (0, 200, 255)

FPS = 2

pyg.init()
screen = pyg.display.set_mode((WIDTH, HEIGHT))
pyg.display.set_caption('Conway\'s Game of Life')
clock = pyg.time.Clock()

matrix = np.zeros((ROWS, COLUMNS))

def randomizer():
    global matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i != 0 and j != 0 and i != matrix.shape[0] - 1 and j != matrix.shape[1] - 1:
                matrix[i, j] = np.random.randint(0, 2)
    
    
def game_of_life():
    global matrix

    matrix_rows, matrix_cols = matrix.shape

    neighbor_matrix = np.zeros((matrix_rows, matrix_cols))

    for row in range(matrix_rows):
        for column in range(matrix_cols):
            if row != 0  and column != 0 and row != matrix_rows - 1 and column != matrix_cols - 1:
                for i in range(-1,2):
                    for j in range(-1,2):
                        neighbor_matrix[row,column] += matrix[row + i, column + j]
                neighbor_matrix[row, column] -= matrix[row, column]

    print(neighbor_matrix)
            
    for row in range(matrix_rows):
        for column in range(matrix_cols):
            if neighbor_matrix[row, column] == 3:
                matrix[row, column] = 1
            elif neighbor_matrix[row, column] < 2 or neighbor_matrix[row, column] > 3:
                matrix[row, column] = 0

def grid():
    global matrix

    matrix_rows, matrix_cols = matrix.shape

    matrix_rows -= 2
    matrix_cols -= 2

    cell_width = (WIDTH - 20) // matrix_cols
    cell_height = (HEIGHT - 20) // matrix_rows

    for row in range(matrix_rows):
        for col in range(matrix_cols):
            # pyg.draw.rect(screen, lighter_gray, ((col * cell_width) + 11, (row * cell_height) + 11, cell_width, cell_height), 1)
            if matrix[1 + row, 1 + col] == 1:
                pyg.draw.rect(screen, light_blue, ((col * cell_width) + 10, (row * cell_height) + 10, cell_width - 0, cell_height - 0), 0)

def highlight_cell(x, y):
    global matrix

    cell_width = (WIDTH - 20) // (COLUMNS - 2)
    cell_height = (HEIGHT - 20) // (ROWS - 2)

    col = x // cell_width
    row = y // cell_height

    col += 1
    row += 1

    # matrix[row, col] = 1
    try:
        for i in range(-1,2):
            for j in range(-1,2):
                matrix[row + i, col + j] = 1
    except:
        pass

def game_loop():
    global matrix
    run = True
    pause = False
    mouse_down = False

    randomizer()

    while run:

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                run = False
            
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_SPACE:
                    pause = True
                elif event.key == pyg.K_r:
                    randomizer()
                elif event.key == pyg.K_c:
                    matrix = np.zeros((ROWS, COLUMNS))

            elif event.type == pyg.MOUSEBUTTONDOWN:
                mouse_down = True
                while(mouse_down):
                    for event in pyg.event.get():
                        if event.type == pyg.MOUSEBUTTONUP:
                            mouse_down = False
                        elif event.type == pyg.MOUSEMOTION:
                            x, y = event.pos
                            highlight_cell(x, y)
                        time.sleep(0.01)

        while(pause):
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pause = False
                    run = False
                    break
                
                if event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_SPACE:
                        pause = False
                    
        
        screen.fill(gray)
        pyg.draw.rect(screen, light_gray, (0, 0, WIDTH - 1, HEIGHT - 1), width=10)
        
        grid()

        game_of_life()

        clock.tick(FPS)

        pyg.display.flip()

    pyg.quit()

if __name__ == '__main__':
    game_loop()
