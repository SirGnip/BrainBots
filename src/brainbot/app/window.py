import importlib
from pathlib import Path
import asyncio
import arcade

BASE_BRAIN_PATH = 'src/brainbot/brain'
BASE_BRAIN_PACKAGE = 'brainbot.brain'


class BrainBotWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.sprites = arcade.SpriteList()
        char = arcade.Sprite(':resources:onscreen_controls/shaded_light/right.png', 0.5)
        self.sprites.append(char)

        char = arcade.Sprite(':resources:onscreen_controls/shaded_light/right.png', 0.5)
        char.center_x = self.width // 2
        char.center_y = self.height // 2
        char.angle = 0
        self.sprites.append(char)

        char = arcade.Sprite(':resources:onscreen_controls/shaded_light/right.png', 0.5)
        char.center_x = 150
        char.center_y = 450
        char.angle = 0
        self.sprites.append(char)

        self.modules = self.get_brains()

        self.async_loop = asyncio.get_event_loop()
        self.async_main_task = self.async_loop.create_task(self.async_main())

    @staticmethod
    def get_brains():
        """Enumerate all modules in the brain submodule and import them dynamically"""
        plugin_dir = Path(BASE_BRAIN_PATH)
        dirs = [d for d in plugin_dir.iterdir() if d.is_file() and d.stem != '__init__' and d.suffix == '.py']
        print('Loading brain plugins...')
        print('\n'.join([str(d) for d in dirs]))
        return [importlib.import_module('.' + d.stem, package=BASE_BRAIN_PACKAGE) for d in dirs]

    async def async_main(self):
        """Top level async task that owns all others"""
        asyncio.create_task(self.modules[0].think(self.sprites[0]))
        asyncio.create_task(self.modules[1].think(self.sprites[1]))
        asyncio.create_task(self.modules[2].think(self.sprites[2]))
        await asyncio.sleep(60*60*60*24)  # sleep forever, let the tasks run

    def on_draw(self):
        self.clear()
        self.sprites.draw()

    def on_update(self, delta_time):
        # Do one tick of the async event loop
        if not self.async_main_task.done():
            self.async_loop.call_soon(self.async_loop.stop)
            self.async_loop.run_forever()

        self.sprites.update()

    def on_key_press(self, key, key_modifiers):
        if key in (arcade.key.Q, arcade.key.ESCAPE):
            self.close()
