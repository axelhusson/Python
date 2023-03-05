class Vaisseau:
    def __init__(self):
        self.body = [Block(15, 37)]
        self.direction = ""
        self.new_head = ""
        self.image = pygame.image.load("./images/player.png")
        self.image = pygame.transform.scale(self.image, (Cell_Size, Cell_Size))
        self.argent = 0
        self.Highscore = 0
        self.PV_Max = 1
        self.LVL_BOUCLIER = 1
        self.LVL_canon = 1
        self.PV = self.PV_Max
        self.chauffe_max = 10 * self.LVL_canon

    def draw_vaisseau(self):
        for block in self.body:
            x_coord = block.x * Cell_Size
            y_coord = block.y * Cell_Size
        screen.blit(self.image,(x_coord, y_coord))

    def move_vaisseau(self):

        old_pos = self.body[0]
        self.new_head = old_pos

        if self.direction == "RIGHT":
            if old_pos.x == 29:
                self.new_head = old_pos
            else:
                self.new_head = Block(old_pos.x + 1, old_pos.y)
        elif self.direction == "LEFT":
            if old_pos.x == 0:
                self.new_head = old_pos
            else:
                self.new_head = Block(old_pos.x - 1, old_pos.y)
        elif self.direction == "TOP":
            if old_pos.y == 0:
                self.new_head = old_pos
            else:
                self.new_head = Block(old_pos.x, old_pos.y - 1)
        elif self.direction == "DOWN":
            if old_pos.y ==39:
                self.new_head = old_pos
            else:
                self.new_head = Block(old_pos.x, old_pos.y + 1)

        self.body.append(self.new_head)
        self.body.__delitem__(0)
        self.direction = ""

        if game.draw_Bouclier == True:
            game.Bouclier.body = []
            for block in self.body:
                self.x_coord: int = block.x
                self.y_coord: int = (block.y - 1)
                self.Nbouclier = Block(self.x_coord, self.y_coord)
                game.Bouclier.body.append(self.Nbouclier)
