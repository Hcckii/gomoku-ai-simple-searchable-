import constants as c


def draw_black_stone():
    transparancy = 150
    fill(0, 0, 0, transparancy)
    ellipse(mouseX, mouseY, c.stone_x, c.stone_y)


def handle_player_click():
    for coord in c.coords:
        cx, cy = coord[0], coord[1]
        if (abs(cx - mouseX) <= c.tolerance and 
            abs(cy - mouseY) <= c.tolerance and 
            coord not in c.ai_stone and
            coord not in c.player_stone):
            
            c.player_stone.add(coord)
            return coord
    return None
