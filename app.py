
"""
Pyweek 31 practice project
"""
import arcade
from core.enemies import Enemy


SCREEN_TITLE = "Pyweek 31"

# Size of screen to show, in pixels
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameWindow(arcade.Window):
    """ Main Window """

    def __init__(self, width, height, title):
        """ Create the variables """

        # Init the parent class
        super().__init__(width, height, title)

        # Sprite Lists
        self.tower_list = None
        self.enemy_list = None
        self.bullet_list = None

        self.base_sprite = None

        self.physics_engine = None

    def setup(self):
        """ Set up everything with the game """

        self.tower_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.base_sprite = arcade.Sprite()

        self.physics_engine = arcade.PymunkPhysicsEngine()
        self.physics_engine.add_sprite_list(
            self.enemy_list,
            collision_type="enemy",
            friction=1.0,
            mass=2.0,
            moment=arcade.PymunkPhysicsEngine.MOMENT_INF,
            body_type=arcade.PymunkPhysicsEngine.DYNAMIC

        )
        enemy = Enemy(400, 600)
        self.enemy_list.append(enemy)
        self.physics_engine.add_sprite(enemy)
        self.physics_engine.set_velocity(enemy, (0, -100))
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        pass

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        print(x, y)

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.physics_engine.step(delta_time=delta_time)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.enemy_list.draw()

def main():
    """ Main method """
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
