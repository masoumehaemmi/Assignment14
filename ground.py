import random
import arcade

class Ground(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()

        # self.walk_left_textures = [arcade.load_texture("image\g0.png"),
        #                            arcade.load_texture("image\g1.png"),
        #                            arcade.load_texture("image\g2.png")]

                                   
        self.pic_path =random.choice(["image\g.png ", "image\wp4285370.png"]) 
        self.texture = arcade.load_texture(self.pic_path)
        self.center_x = x
        self.center_y = y

        self.width = 80
        self.height = 80

        self.change_x = -1
        # self.change_y =0

        self.speed = 1

    # def move(self, speed):
    #     self.center_x += self.change_x * speed