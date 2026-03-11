import constants as c

def draw_subtitle_rect(sub_x, sub_y):
    noStroke()
    fill(56, 140, 176)
    rect(sub_x, sub_y, c.subtitle_tolerance_x * 3, c.subtitle_tolerance_y * 3, 20)


def draw_title():
    background(95, 95, 95)
    create_title("GoMoKu")

    draw_subtitle_rect(c.x/2, c.y/1.96)
    fill(196, 245, 255)
    textSize(c.subtitle_size)
    text("GAME MODE", c.but2_x, c.but2_y)
    
    draw_subtitle_rect(c.x/2, c.y/1.48)
    fill(196, 245, 255)
    textSize(c.subtitle_size)
    text("LEADER BOARD", c.but3_x, c.but3_y)
    
    fill(0)
    textSize(c.subtitle_size//2)
    text("Gomoku V.3 By Chang Chi (Ethan) Hua ", c.copyright_x, c.copyright_y)


def draw_gamemode():
    background(95, 95, 95)
    draw_back_button()

    draw_subtitle_rect(c.x/2, c.y/2.92)
    fill(196, 245, 255)
    textSize(c.subtitle_size)
    text("NOOB", c.but1_x, c.but1_y)

    if abs(mouseX - c.but1_x) <= c.subtitle_tolerance_x and \
       abs(mouseY - c.but1_y) <= c.subtitle_tolerance_y:
        fill(196, 245, 255)
        textSize(c.button_size * 1.5)
        text("Perfect for someone who's", c.x/2, c.x/8)
        text("playing GoMoKu for the first time", c.x/2, c.x/5.5)

    draw_subtitle_rect(c.x/2, c.y/1.96)
    fill(196, 245, 255)
    textSize(c.subtitle_size)
    text("BEGINNER", c.but2_x, c.but2_y)

    if abs(mouseX - c.but2_x) <= c.subtitle_tolerance_x and \
       abs(mouseY - c.but2_y) <= c.subtitle_tolerance_y:
        fill(196, 245, 255)
        textSize(c.button_size * 1.5)
        text("Perfect for someone who already", c.x/2, c.x/8)
        text("has basic knoledge of GoMoKu", c.x/2, c.x/5.5)

    draw_subtitle_rect(c.x/2, c.y/1.48)
    fill(196, 245, 255)
    textSize(c.subtitle_size)
    text("MASTER", c.but3_x, c.but3_y)

    if abs(mouseX - c.but3_x) <= c.subtitle_tolerance_x and \
       abs(mouseY - c.but3_y) <= c.subtitle_tolerance_y:
        fill(196, 245, 255)
        textSize(c.button_size * 1.5)
        text("Perfect for someone who's on their way", c.x/2, c.x/8)
        text("of becomming the next GrandMaster", c.x/2, c.x/5.5)


def draw_leaderboard(scores):
    background(125, 12, 0)
    fill(255)
    noStroke()
    # rect(c.start_x, 0, c.x//60, c.y * 2)
    # rect(c.end_x, 0, c.x//60, c.y * 2)
    
    # fill(255, 200, 0)
    # rect(c.x/8, c.y/8.2, c.x * 2, c.y/8)
    fill(0)
    textSize(c.subtitle_size*2)
    text("LEADERBOARD", c.x/1.97, c.y/9.5)

    fill(255, 215, 0)
    textSize(c.subtitle_size*2)
    text("LEADERBOARD", c.x/2, c.y/10)

    draw_back_button()

    if not scores:
        fill(196, 245, 255)
        textSize(c.subtitle_size)
        text("No scores yet!", c.x/2, c.y/2)
    else:
        fill(255)
        textSize(c.button_size * 1.25)
        textAlign(LEFT, CENTER)
        start_y = c.y/4
        for i, (name, score) in enumerate(scores[:10]):
            text(str(i+1) + '.' + " " + name + ':' + " " + str(score), c.x/2.6, start_y + i * 40)
        textAlign(CENTER, CENTER)

def create_title(word, color=(196, 245, 255)):
    fill(67, 145, 161)
    textSize(c.title_size)
    text(word, c.x//1.94, c.y/3.9)
    fill(*color)
    textSize(c.title_size)
    text(word, c.x//2, c.y//4)

def draw_back_button():
    fill(196, 245, 255)
    textSize(c.button_size)
    text("BACK TO TITLE", c.back_x, c.back_y)


def reset_game():
    c.ai_stone = set()
    c.player_stone = set()
    c.WWIN = False
    c.BWIN = False
    c.player1 = True
    c.player2 = False
    c.main_title = True
    c.game_select = False
    c.show_leaderboard = False
    c.game_start = False
    c.game_over = False
    c.winning = None
    c.placed = False
