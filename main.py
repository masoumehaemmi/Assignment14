from ground import Ground
from dino import Dino
from bird import Bird
import random
import time
import arcade


class Game(arcade.Window):
    def __init__(self):
        self.w = 1000
        self.h = 500
        self.gravity = 0.5
        super().__init__(self.w,self.h, "T_Rex Game Saeideh")
        
        # self.background_image_day = arcade.load_texture("image\disert d.jpg")
        self.background_image_night = arcade.load_texture("image\disert n.jpg")
        self.background_time = time.time()
        
        self.night = True
        
        self.ground_list = arcade.SpriteList()
        self.ground_list.append(Ground(100,80))
        self.dino = Dino()
        
        self.bird_speed = -5
        self.startplay_time = time.time()

        self.bird_list = arcade.SpriteList()
        
        for i in range(self.w,self.h):
            bird = Bird(i, 400)
            self.bird_list.append(bird)

        self.cloud = arcade.Sprite("image\c1.png")
        self.cloud.center_x = 800
        self.cloud.center_y = 450
        self.cloud.width = 100
        self.cloud.height = 100
        
        self.kaktos = arcade.Sprite("image\c1 copy.png")
        self.kaktos.center_x = 400
        self.kaktos.center_y = 100
        self.kaktos.width = 100
        self.kaktos.height = 100

        self.physics_engine = arcade.PhysicsEnginePlatformer( self.dino,self.ground_list, self.gravity)

    def on_draw(self):
        self.t1 = time.time()

        arcade.start_render()

        if self.night == False:
            arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image_day)
        else:
                
            arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.background_image_night)


        arcade.draw_text(f"score: {self.dino.score}", 850, 450, arcade.color.WHITE, 30)
        
        self.dino.draw()
        
        self.cloud.draw()

        self.kaktos.draw()

        for ground in self.ground_list:
                ground.draw()   
        
        for bird in self.bird_list:
            if self.dino.score > 1000:

                bird.draw()

    def on_update(self,delta_time:float):
        self.t2 = time.time()
        # self.dino.update()
        self.physics_engine.update()

        if self.startplay_time == 1:
            if self.t2 - self.background_time >20 and self.night == True:
                self.background_image_day = arcade.load_texture("image\disert d.jpg")
                self.night = False
                self.background_time = time.time()
        # for kaktos in self.kaktos_list:
        #         kaktos.update()
        #         if kaktos.center_x < 0 :
        #             self.tree_list.remove(kaktos)
        

        for i in range(0,self.width,80):
            for ground in self.ground_list:
                ground.update_animation()
                ground.update()
                # if ground.center_x < 0:
                # self.ground_list.remove(ground)
                self.ground_list.append(Ground(i,80))

        for bird in self.bird_list:
            bird.update_animation()
            bird.update()

        # r = random.randint(self.t1 , self.t2)

        # if r in 

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.startplay_time = 1

        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.dino.change_y = 10
                self.dino.score += 1

        if key == arcade.key.DOWN:
            self.dino.texture = arcade.load_texture('')       

    def on_key_release(self, key, modifiers):
            pass

game= Game()
arcade.run()
