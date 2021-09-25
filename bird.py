
import random
import arcade
class Bird(arcade.AnimatedWalkingSprite):
    def __init__(self, width, speed):
        super().__init__()
        self.walk_left_textures = [arcade.load_texture('image\drog0.png'),
                                   arcade.load_texture('image\drog1.png')]
        self.center_x = width
        self.center_y = random.randint(250, 450)
        self.change_x = speed 
        self.change_y = 0
        
        