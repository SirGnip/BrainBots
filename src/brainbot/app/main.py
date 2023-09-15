import brainbot.common.util
import brainbot.app.window
import arcade

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_TITLE = 'BrainBot'


def run() -> None:
    game = brainbot.app.window.BrainBotWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == '__main__':
    run()
