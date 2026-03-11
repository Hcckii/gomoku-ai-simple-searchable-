import constants as c
import board
import player
import ai_player
import ui
from win_check import Wincheck


block = None
wincheck = Wincheck(c.WIN_ROW, c.start_x, c.end_x, c.start_y, c.end_y, c.gap_x, c.gap_y)
game_over_delay = 0


def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def save_score(winner_name):
    scores = {}

    try:
        with open('scores.txt', 'r') as f:
            for line in f:
                parts = line.strip().rsplit(' ', 1)
                if len(parts) == 2:
                    name = parts[0]
                    score = int(parts[1])
                    scores[name] = score
    except:
        pass

    if winner_name in scores:
        scores[winner_name] += 1
    else:
        scores[winner_name] = 1

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    with open('scores.txt', 'w') as f:
        for name, score in sorted_scores:
            f.write(str(name)+" "+str(score)+"\n")


def load_scores():
    scores = []
    try:
        with open('scores.txt', 'r') as f:
            for line in f:
                parts = line.strip().rsplit(' ', 1)
                if len(parts) == 2:
                    name = parts[0]
                    score = int(parts[1])
                    scores.append((name, score))
    except (FileNotFoundError, IOError, ValueError):
        pass
    return scores


def setup():
    size(c.x, c.y)
    textAlign(CENTER, CENTER)
    rectMode(CENTER)


def draw():
    global game_over_delay
    
    if c.main_title:
        ui.draw_title()
    elif c.game_select:
        ui.draw_gamemode()
    elif c.show_leaderboard:
        scores = load_scores()
        ui.draw_leaderboard(scores)
    elif c.game_start:
        board.draw_frame()
        board.show_stones()

        if c.WWIN:
            ui.create_title("You Win!")
            if not c.game_over:
                c.game_over = True
                game_over_delay = 0
            elif game_over_delay < 30:
                game_over_delay += 1
            elif game_over_delay == 30:
                game_over_delay += 1
                winner_name = input("Enter your name:")
                if winner_name:
                    save_score(winner_name)

        elif c.BWIN:
            ui.create_title("You Lost!")
            if not c.game_over:
                c.game_over = True

        elif len(c.ai_stone) + len(c.player_stone) < len(c.coords) and not c.BWIN and not c.WWIN:
            if c.player1:
                player.draw_black_stone()

            elif c.player2:
                if c.placed:
                    ai_player.place_ai_stone(block, wincheck)
                else:
                    ai_player.animate_white_stone(block)       

        elif len(c.ai_stone) + len(c.player_stone) == len(c.coords):
            fill(100, 100, 100)
            textSize(c.x//5)
            text("DRAW", c.x//2, c.y//2)
            c.game_over = True

        if c.game_over:
            ui.draw_back_button()

def mouseClicked():
    global block

    if c.main_title:
        if abs(mouseX - c.but2_x) <= c.subtitle_tolerance_x and abs(mouseY - c.but2_y) <= c.subtitle_tolerance_y:
            c.main_title = False
            c.game_select = True
        elif abs(mouseX - c.but3_x) <= c.subtitle_tolerance_x and abs(mouseY - c.but3_y) <= c.subtitle_tolerance_y:
            c.main_title = False
            c.show_leaderboard = True

    elif c.game_select:
        if abs(mouseX - c.but1_x) <= c.subtitle_tolerance_x and abs(mouseY - c.but1_y) <= c.subtitle_tolerance_y:
            c.game_mode = c.DIFFICULTY[0]
            c.game_select = False
            c.game_start = True
        elif abs(mouseX - c.but2_x) <= c.subtitle_tolerance_x and abs(mouseY - c.but2_y) <= c.subtitle_tolerance_y:
            c.game_mode = c.DIFFICULTY[1]
            c.game_select = False
            c.game_start = True
        elif abs(mouseX - c.but3_x) <= c.subtitle_tolerance_x and abs(mouseY - c.but3_y) <= c.subtitle_tolerance_y:
            c.game_mode = c.DIFFICULTY[2]
            c.game_select = False
            c.game_start = True
        elif abs(mouseX - c.back_x) <= c.subtitle_tolerance_x and abs(mouseY - c.back_y) <= c.subtitle_tolerance_y:
            ui.reset_game()

    elif c.show_leaderboard:
        if abs(mouseX - c.back_x) <= c.subtitle_tolerance_x and abs(mouseY - c.back_y) <= c.subtitle_tolerance_y:
            ui.reset_game()

    elif c.game_start:
        if c.player1:
            coord = player.handle_player_click()
            if coord:
                wincheck.check_win(coord, c.player_stone)
                block = ai_player.calculate_ai_move()
                c.player2 = True
                c.player1 = False

        if c.game_over:
            if abs(mouseX - c.back_x) <= c.subtitle_tolerance_x and abs(mouseY - c.back_y) <= c.subtitle_tolerance_y:
                ui.reset_game()
