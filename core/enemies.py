'''
This file creates enemies.
'''

import arcade


class Enemy(arcade.Sprite):

    def __init__(self, x, y, *args):
        super().__init__(*args)
        self.texture = arcade.load_texture('resources/tiles/enemy_1.png')
        self.width = 100
        self.height = 100
        self.center_x = x
        self.center_y = y

    def on_update(self):
        pass
