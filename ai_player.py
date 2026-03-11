import constants as c
import random
from math import sqrt
from win_check import Wincheck


wincheck = Wincheck


def calculate_ai_move():
    block = None
    
    if not c.ai_stone:
        block = random.choice(list(c.coords - c.player_stone - c.ai_stone))
    elif c.game_mode == c.DIFFICULTY[2]:
        block = find_best_move()
    elif c.winning:
        block = block_threat()
    else:
        block = offensive_move()
    
    if block is None:
        block = random.choice(list(c.coords - c.player_stone - c.ai_stone))
    
    c.move_stone_x = c.BOARD_SIZE[0] // 2
    c.move_stone_y = 0
    c.placed = False
    return block


def find_best_move():
    available = list(c.coords - c.player_stone - c.ai_stone)
    
    for pos in available:
        test_ai = c.ai_stone | {pos}
        if check_position_wins(pos, test_ai):
            return pos
    
    for pos in available:
        test_player = c.player_stone | {pos}
        if check_position_wins(pos, test_player):
            return pos
    
    best_move = None
    best_score = 0
    
    for pos in available:
        score = evaluate_position(pos)
        if score > best_score:
            best_score = score
            best_move = pos
    
    return best_move


def check_position_wins(coord, stones):
    x, y = coord
    
    count = 1
    cy = y - c.gap_y
    while (x, cy) in stones:
        count += 1
        cy -= c.gap_y
    cy = y + c.gap_y
    while (x, cy) in stones:
        count += 1
        cy += c.gap_y
    if count >= c.WIN_ROW:
        return True
    
    count = 1
    cx = x - c.gap_x
    while (cx, y) in stones:
        count += 1
        cx -= c.gap_x
    cx = x + c.gap_x
    while (cx, y) in stones:
        count += 1
        cx += c.gap_x
    if count >= c.WIN_ROW:
        return True
    
    count = 1
    cx, cy = x - c.gap_x, y - c.gap_y
    while (cx, cy) in stones:
        count += 1
        cx -= c.gap_x
        cy -= c.gap_y
    cx, cy = x + c.gap_x, y + c.gap_y
    while (cx, cy) in stones:
        count += 1
        cx += c.gap_x
        cy += c.gap_y
    if count >= c.WIN_ROW:
        return True
    
    count = 1
    cx, cy = x + c.gap_x, y - c.gap_y
    while (cx, cy) in stones:
        count += 1
        cx += c.gap_x
        cy -= c.gap_y
    cx, cy = x - c.gap_x, y + c.gap_y
    while (cx, cy) in stones:
        count += 1
        cx -= c.gap_x
        cy += c.gap_y
    if count >= c.WIN_ROW:
        return True
    
    return False


def evaluate_position(coord):
    x, y = coord
    score = 0
    
    directions = [
        (0, c.gap_y),
        (c.gap_x, 0),
        (c.gap_x, c.gap_y),
        (c.gap_x, -c.gap_y)
    ]
    
    for dx, dy in directions:
        ai_count = 1
        
        cx, cy = x - dx, y - dy
        temp_ai = 0
        blocked = False
        while (cx, cy) in c.coords:
            if (cx, cy) in c.ai_stone:
                temp_ai += 1
            elif (cx, cy) in c.player_stone:
                blocked = True
                break
            else:
                break
            cx -= dx
            cy -= dy
        
        cx, cy = x + dx, y + dy
        while (cx, cy) in c.coords:
            if (cx, cy) in c.ai_stone:
                temp_ai += 1
            elif (cx, cy) in c.player_stone:
                blocked = True
                break
            else:
                break
            cx += dx
            cy += dy
        
        ai_count += temp_ai
        
        if not blocked:
            if ai_count == 4:
                score += 10000
            elif ai_count == 3:
                score += 1000
            elif ai_count == 2:
                score += 100
    
    center_x = (c.start_x + c.end_x) // 2
    center_y = (c.start_y + c.end_y) // 2
    dist = abs(x - center_x) + abs(y - center_y)
    score += 10 - (dist / c.gap_x)
    
    return score


def block_threat():
    if c.winning == c.WIN_STATUS[0]:
        return block_vertical()
    elif c.winning == c.WIN_STATUS[1]:
        return block_horizontal()
    elif c.winning == c.WIN_STATUS[2]:
        return block_slash()
    elif c.winning == c.WIN_STATUS[3]:
        return block_backslash()
    return None

def block_vertical():
    up = (c.winning_coord[0], c.winning_coord[1] - c.gap_y)
    down = (c.winning_coord[0], c.winning_coord[1] + c.gap_y)
    if (up[1] >= c.start_y and up not in c.player_stone and up not in c.ai_stone):
        return up
    elif (down[1] <= c.end_y and down not in c.player_stone and down not in c.ai_stone):
        return down
    return None

def block_horizontal():
    left = (c.winning_coord[0] - c.gap_x, c.winning_coord[1])
    right = (c.winning_coord[0] + c.gap_x, c.winning_coord[1])
    if (left[0] >= c.start_x and left not in c.player_stone and left not in c.ai_stone):
        return left
    elif (right[0] <= c.end_x and right not in c.player_stone and right not in c.ai_stone):
        return right
    return None

def block_slash():
    upper_right = (c.winning_coord[0] + c.gap_x, c.winning_coord[1] - c.gap_y)
    lower_left = (c.winning_coord[0] - c.gap_x, c.winning_coord[1] + c.gap_y)
    if (upper_right[0] <= c.end_x and upper_right[1] >= c.start_y and
        upper_right not in c.player_stone and upper_right not in c.ai_stone):
        return upper_right
    elif (lower_left[0] >= c.start_x and lower_left[1] <= c.end_y and
          lower_left not in c.player_stone and lower_left not in c.ai_stone):
        return lower_left
    return None

def block_backslash():
    upper_left = (c.winning_coord[0] - c.gap_x, c.winning_coord[1] - c.gap_y)
    lower_right = (c.winning_coord[0] + c.gap_x, c.winning_coord[1] + c.gap_y)
    if (upper_left[0] >= c.start_x and upper_left[1] >= c.start_y and
        upper_left not in c.player_stone and upper_left not in c.ai_stone):
        return upper_left
    elif (lower_right[0] <= c.end_x and lower_right[1] <= c.end_y and
          lower_right not in c.player_stone and lower_right not in c.ai_stone):
        return lower_right
    return None

def offensive_move():
    available = c.coords - c.player_stone - c.ai_stone
    
    directions = [
        (c.gap_x, 0), (-c.gap_x, 0),
        (0, c.gap_y), (0, -c.gap_y),
        (c.gap_x, c.gap_y), (-c.gap_x, -c.gap_y),
        (c.gap_x, -c.gap_y), (-c.gap_x, c.gap_y)
    ]
    
    for attempt in range(20):
        start_point = random.choice(list(c.ai_stone))
        random.shuffle(directions)
        
        for dx, dy in directions:
            check_step = (start_point[0] + dx, start_point[1] + dy)
            if check_step in available:
                return check_step
    
    return None

def animate_white_stone(block):
    speed = 25
    dx = block[0] - c.move_stone_x
    dy = block[1] - c.move_stone_y
    distance = sqrt(dx**2 + dy**2)
    transparancy = 150
    fill(255, 255, 255, transparancy)
    ellipse(c.move_stone_x, c.move_stone_y, c.stone_x, c.stone_y)
    if distance < speed:
        c.move_stone_x = block[0]
        c.move_stone_y = block[1]
        c.placed = True
    else:
        c.move_stone_x += dx / distance * speed
        c.move_stone_y += dy / distance * speed

def place_ai_stone(block, wincheck):
    c.ai_stone.add(block)
    wincheck.check_win(block, c.ai_stone)
    c.player1 = True
    c.player2 = False
