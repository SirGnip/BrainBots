import arcade


class BrainBotWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.sprites = None

    def setup(self):
        """Call to re-start the game"""
        self.sprites = arcade.SpriteList()

        char = arcade.Sprite(':resources:onscreen_controls/shaded_light/up.png', 0.5)
        char.center_x = self.width//2
        char.center_y = self.height//2
        char.angle = 0
        self.sprites.append(char)

        char = arcade.Sprite(':resources:onscreen_controls/shaded_light/up.png', 0.5)
        char.center_x = 150
        char.center_y = 450
        char.angle = 0
        self.sprites.append(char)

    def on_draw(self):
        self.clear()
        self.sprites.draw()

    def on_update(self, delta_time):
        for s in self.sprites:
            s.angle += 0.5

    def on_key_press(self, key, key_modifiers):
        if key in (arcade.key.Q, arcade.key.ESCAPE):
            self.close()

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass


