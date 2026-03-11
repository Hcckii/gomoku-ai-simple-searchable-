# Board settings
BOARD_SIZE = (800, 800)
STONE_SIZE = 0.85
GRIDS = 15
WIN_ROW = 5

# Difficulty
DIFFICULTY = ['noob', 'beginner', 'master']
game_mode = DIFFICULTY[0]

# Screen states
main_title = True
game_select = False
show_leaderboard = False
game_start = False
game_over = False
prompt_for_name = False

# Player turns
player1 = True
player2 = False

# Stones
player_stone = set()
ai_stone = set()

# Win status
BWIN = False
WWIN = False
winning = None
WIN_STATUS = ['up down', 'left right', 'slash', 'back slash']
winning_coord = tuple()

# Animation
placed = False
move_stone_x = BOARD_SIZE[0] // 2
move_stone_y = 0

# Calculate board dimensions
x = BOARD_SIZE[0]
y = BOARD_SIZE[1]

shrink_scale = 7
if GRIDS <= shrink_scale:
    shrink = 0.16
else:
    shrink = 0.05

start_x = int(x * shrink)
start_y = int(y * shrink)
end_x = x - start_x
end_y = y - start_y

squares = GRIDS - 1
gap_x = int((end_x - start_x) / squares)
gap_y = int((end_y - start_y) / squares)

grid_x = [start_x + i*gap_x for i in range(GRIDS)]
grid_y = [start_y + i*gap_y for i in range(GRIDS)]

coords = set((i, j) for i in grid_x for j in grid_y)

# Stone settings
stone_x = gap_x * STONE_SIZE
stone_y = gap_y * STONE_SIZE
tolerance = stone_x // 2

# UI settings
title_size = x / 4.5
subtitle_size = x / 15
button_size = x / 30

# Button positions
but1_x, but1_y = x/2, y/3
but2_x, but2_y = x/2, y/2
but3_x, but3_y = x/2, y/1.5
back_x, back_y = x/2, end_y - gap_y
copyright_x, copyright_y = x/2, end_y

# Button tolerances
subtitle_tolerance_x = subtitle_size * 3
subtitle_tolerance_y = subtitle_size / 2