import constants as c


def draw_frame():
    interX = 120 // c.GRIDS
    interY = 120 // c.GRIDS
    background(186, 140, 99)
    stroke(0)
    strokeWeight(40 // c.GRIDS)

    for gx in c.grid_x:
        line(gx, c.start_y, gx, c.grid_y[-1])
    for gy in c.grid_y:
        line(c.start_x, gy, c.grid_x[-1], gy)

    fill(0)
    noStroke()
    for i in c.coords:
        ellipse(i[0], i[1], interX, interY)


def show_stones():
    for p in c.player_stone:
        fill(0, 0, 0)
        strokeWeight(3)
        ellipse(p[0], p[1], c.stone_x, c.stone_y)

    for a in c.ai_stone:
        fill(255, 255, 255)
        ellipse(a[0], a[1], c.stone_x, c.stone_y)