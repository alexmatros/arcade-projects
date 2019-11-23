import arcade

WIDTH = 640
HEIGHT = 480

window = arcade.open_window(WIDTH, HEIGHT, "Landscape")


def setup():
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    pass


@window.event
def on_draw():
    arcade.start_render()

    # draw the ground
    arcade.draw_lrtb_rectangle_filled(0, WIDTH, 100, 0, arcade.color.GREEN)

    # draw the sun
    arcade.draw_circle_filled(WIDTH - 100, HEIGHT - 100, 50,
                              arcade.color.YELLOW)

    draw_tree(175, 160)
    draw_tree(WIDTH-200, 160)
    draw_tree(WIDTH-125, 160)


def draw_tree(x: int, y: int):
    tree_height = 150

    # draw the tree leaves
    leaves_width = 80 / 2
    leaves_height = 75
    arcade.draw_triangle_filled(x - leaves_width, y,
                                x, y + leaves_height,
                                x + leaves_width, y,
                                arcade.color.DARK_GREEN)

    # draw the tree trunk
    trunk_width = 20
    trunk_height = tree_height - leaves_height
    arcade.draw_xywh_rectangle_filled(x - trunk_width/2, y - trunk_height,
                                      trunk_width, trunk_height,
                                      arcade.color.BROWN)


if __name__ == '__main__':
    setup()
