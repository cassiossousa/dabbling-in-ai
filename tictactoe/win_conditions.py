#
# Checks winning conditions for a 3x3 tic-tac-toe board.
#


# Check for null entries

def not_null_at(game_grid, x, y):
    return game_grid[x][y] is not None


# Diagonal winning conditions

def win_main_diagonal(game_grid):
    return not_null_at(game_grid, 0, 0) and not_null_at(game_grid, 1, 1) and not_null_at(game_grid, 2, 2) and (
        game_grid[0][0] == game_grid[1][1] and game_grid[1][1] == game_grid[2][2])


def win_second_diagonal(game_grid):
    return not_null_at(game_grid, 0, 2) and not_null_at(game_grid, 1, 1) and not_null_at(game_grid, 2, 0) and (
        game_grid[0][2] == game_grid[1][1] and game_grid[1][1] == game_grid[2][0])


def win_diagonal(game_grid):
    return win_main_diagonal(game_grid) or win_second_diagonal(game_grid)


# Vertical winning conditions

def win_vertical_at(game_grid, y):
    return not_null_at(game_grid, 0, y) and not_null_at(game_grid, 1, y) and not_null_at(game_grid, 2, y) and (
        game_grid[0][y] == game_grid[1][y] and game_grid[1][y] == game_grid[2][y])


def win_vertical(game_grid):
    return win_vertical_at(game_grid, 0) or win_vertical_at(game_grid, 1) or win_vertical_at(game_grid, 2)


# Vertical winning conditions

def win_horizontal_at(game_grid, x):
    return not_null_at(game_grid, x, 0) and not_null_at(game_grid, x, 1) and not_null_at(game_grid, x, 2) and (
        game_grid[x][0] == game_grid[x][1] and game_grid[x][1] == game_grid[x][2])


def win_horizontal(game_grid):
    return win_horizontal_at(game_grid, 0) or win_horizontal_at(game_grid, 1) or win_horizontal_at(game_grid, 2)


# All winning conditions combined

def win(game_grid):
    return win_horizontal(game_grid) or win_vertical(game_grid) or win_diagonal(game_grid)


# Check if every tile of the grid is filled

def grid_filled(game_grid):
    rows = len(game_grid)
    cols = len(game_grid[0])
    for x in range(rows):
        for y in range(cols):
            if game_grid[x][y] is None:
                return False
    return True


# Draw

def draw(game_grid):
    return grid_filled(game_grid) and not win(game_grid)
