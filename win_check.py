import constants as c


class Wincheck:
    def __init__(self, win_row, start_x, end_x, start_y, end_y, gap_x, gap_y):
        self.win_row = win_row
        self.start_x = start_x
        self.end_x = end_x
        self.start_y = start_y
        self.end_y = end_y
        self.gap_x = gap_x
        self.gap_y = gap_y
    
    def check_win(self, coordinates, stones):

        player_x = coordinates[0]
        player_y = coordinates[1]
        
        count1 = 1
        count2 = 1
        count3 = 1
        count4 = 1

        if c.game_mode == c.DIFFICULTY[0]:
            block_line = self.win_row - 1
        elif c.game_mode == c.DIFFICULTY[1]:
            block_line = (self.win_row//2) + 1
        elif c.game_mode == c.DIFFICULTY[2]:
            block_line = self.win_row//2

        # Check vertical
        check_x, check_y = player_x, player_y - self.gap_y
        while (check_x, check_y) in stones:
            count1 += 1
            check_y -= self.gap_y

        check_x, check_y = player_x, player_y + self.gap_y
        while (check_x, check_y) in stones:
            count1 += 1
            check_y += self.gap_y

        if count1 >= self.win_row:
            if stones == c.ai_stone:
                c.BWIN = True
            elif stones == c.player_stone:
                c.WWIN = True

        # Check horizontal
        check_x, check_y = player_x + self.gap_x, player_y
        while (check_x, check_y) in stones:
            count2 += 1
            check_x += self.gap_x

        check_x, check_y = player_x - self.gap_x, player_y
        while (check_x, check_y) in stones:
            count2 += 1
            check_x -= self.gap_x

        if count2 >= self.win_row:
            if stones == c.ai_stone:
                c.BWIN = True
            elif stones == c.player_stone:
                c.WWIN = True

        # Check slash 
        check_x, check_y = player_x + self.gap_x, player_y - self.gap_y
        while (check_x, check_y) in stones:
            count3 += 1
            check_x += self.gap_x
            check_y -= self.gap_y

        check_x, check_y = player_x - self.gap_x, player_y + self.gap_y
        while (check_x, check_y) in stones:
            count3 += 1
            check_x -= self.gap_x
            check_y += self.gap_y
            
        if count3 >= self.win_row:
            if stones == c.ai_stone:
                c.BWIN = True
            elif stones == c.player_stone:
                c.WWIN = True

        # Check back slash
        check_x, check_y = player_x - self.gap_x, player_y - self.gap_y
        while (check_x, check_y) in stones:
            count4 += 1
            check_x -= self.gap_x
            check_y -= self.gap_y

        check_x, check_y = player_x + self.gap_x, player_y + self.gap_y
        while (check_x, check_y) in stones:
            count4 += 1
            check_x += self.gap_x
            check_y += self.gap_y

        if count4 >= self.win_row:
            if stones == c.ai_stone:
                c.BWIN = True
            elif stones == c.player_stone:
                c.WWIN = True

        if stones == c.player_stone:
            max_count = max(count1, count2, count3, count4)

            if max_count >= block_line:
                if count1 == max_count:
                    c.winning = c.WIN_STATUS[0]
                    c.winning_coord = coordinates
                elif count2 == max_count:
                    c.winning = c.WIN_STATUS[1]
                    c.winning_coord = coordinates
                elif count3 == max_count:
                    c.winning = c.WIN_STATUS[2]
                    c.winning_coord = coordinates
                elif count4 == max_count:
                    c.winning = c.WIN_STATUS[3]
                    c.winning_coord = coordinates
