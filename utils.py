import pygame

SAND_COLOR = (191, 166, 116)


def convert(x, y, cell_size):
    return (x//cell_size, y//cell_size)
def draw_sand(row, col, window, cell_size):
    pygame.draw.rect(window, SAND_COLOR, pygame.Rect(col*cell_size, row*cell_size, cell_size, cell_size))

class Grid():
    def __init__(self, w, h, cell_size):
        self.height = h
        self.width = w
        self.cell_size = cell_size
        self.grid = [[0 for i in range(w)] for j in range(h)]
        self.functional_particles = []
    def draw(self, window):
        for el in self.functional_particles:
            r, c = el
            draw_sand(r, c, window, self.cell_size)
    def convert_to_sand(self, i, j):
        if self.grid[i][j] != 1:
            self.grid[i][j] = 1
            self.functional_particles.append((i, j))
    def convert_to_hole(self, i, j):
        if self.grid[i][j] != 0:
            self.grid[i][j] = 0
            if (i, j) in self.functional_particles:
                self.functional_particles.remove((i, j))
    def update(self):
        for i in range(len(self.functional_particles)):
            particle = self.functional_particles[i]
            row, col = particle
            if row+1 >= self.height or self.grid[row+1][col] == 1:
                continue
            self.grid[row][col] = 0
            self.grid[row+1][col] = 1
            self.functional_particles[i] = (row+1, col)