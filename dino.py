import arcade



class Dino(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture= arcade.load_texture("image\d1.png" ,mirrored= True)

        self.width = 120
        self.height = 120
        self.center_x = 50
        self.center_y = 150
        # self.change_x = 0
        self.score = 0
    
    