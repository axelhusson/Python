# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import random
import pygame
import pickle
import pathlib

pygame.init()
pygame.font.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()

Nb_Col = 30
Nb_Row = 40
Cell_Size = 32

screen = pygame.display.set_mode(size=(Nb_Col * Cell_Size, Nb_Row * Cell_Size))
timer = pygame.time.Clock()


class Game:
    def __init__(self):
        self.point = 0
        self.FPS = 60 + (int(self.point / 10))
        self.fond = pygame.image.load("images/background.png")
        self.fond = pygame.transform.scale(self.fond, (960, 1280))
        self.rond_rouge = pygame.image.load("images/Rond_rouge.png")
        self.rond_rouge = pygame.transform.scale(self.rond_rouge, (Cell_Size, Cell_Size))
        self.rond_orange = pygame.image.load("images/cercle-orange-fond-transparent.png")
        self.rond_orange = pygame.transform.scale(self.rond_orange, (Cell_Size, Cell_Size))
        self.rond_vert = pygame.image.load("images/cercle-vert-fond-transparent.png")
        self.rond_vert = pygame.transform.scale(self.rond_vert, (Cell_Size, Cell_Size))
        self.Vaisseau = Vaisseau()
        self.Laser = Laser()
        self.Laser_Alienb = Laser_Alienb()
        self.Alien = Alien()
        self.Alienb = Alienb()
        self.Bouclier = Bouclier()
        self.move_Alien = False
        self.pop_Alien = False
        self.pop_Alienb = False
        self.Laser_alien = Laser_alien()
        self.pop_Laser_Alien = False
        self.pop_Laser = False
        self.pop_Bouclier = False
        self.draw_Bouclier = False
        self.ecran_accueil = True
        self.chauffe = 0

    def draw_indicateur(self):
        if self.chauffe == 0:
            screen.blit(self.rond_vert, (((Nb_Col - 1) * Cell_Size), ((Nb_Row - 1) * Cell_Size)))
        elif self.chauffe >= game.Vaisseau.chauffe_max:
            screen.blit(self.rond_rouge, (((Nb_Col - 1) * Cell_Size), ((Nb_Row - 1) * Cell_Size)))
        else:
            screen.blit(self.rond_orange, (((Nb_Col - 1) * Cell_Size), ((Nb_Row - 1) * Cell_Size)))

    def update(self):
        pygame.time.set_timer(SCREEN_UPDATE, game.FPS)
        #if game.Vaisseau.Touche == 0:
        #    game.Vaisseau.image = pygame.image.load("./images/player.png")
        #else:
        #    game.Vaisseau.image = pygame.image.load("./images/explosion3.png")
        #    game.Vaisseau.Touche -= 1
        #game.Vaisseau.image = pygame.transform.scale(game.Vaisseau.image, (Cell_Size, Cell_Size))
        game.draw_indicateur()
        game.Vaisseau.move_vaisseau()
        if self.pop_Laser:
            game.Laser.new_laser()
        game.Vaisseau.draw_vaisseau()
        game.Laser.draw_laser()
        game.Laser_alien.draw_laser()
        game.Laser_Alienb.draw_laser()
        if self.pop_Bouclier:
            game.Bouclier.new_bouclier()
            self.pop_Bouclier = False
            self.draw_Bouclier = True
        game.Bouclier.draw_bouclier()
        if self.pop_Alien:
            iteration = 1
            while iteration <= game.Alien.level:
                game.Alien.new_alien()
                self.point += 10
                iteration += 1
            self.pop_Alien = False
        if self.pop_Alienb:
            game.Alienb.new_alien()
            self.pop_Alienb = False
        game.Alien.draw_alien()
        game.Alienb.draw_alien()
        game.Laser.move_laser()
        if self.move_Alien:
            game.Alien.move_alien()
            game.Alienb.move_alien()
            self.move_Alien = False
        if self.pop_Laser_Alien:
            game.Laser_alien.new_laser()
            game.Laser_Alienb.new_laser()
            self.pop_Laser_Alien = False
        game.Laser_alien.move_laser()
        game.Laser_Alienb.move_laser()
        game.check_colision_laser()
        game.check_colision_laserb()
        game.check_colision_laser_alien()
        game.check_colision_laser_alienb()


    def check_colision_laser(self):
        self.iteration_laser = 0
        self.laser_block_count = len(game.Laser.body)
        self.iter_max_laser = self.laser_block_count - 1
        if game.Laser.body:
            while self.iteration_laser <= self.iter_max_laser:
                if game.Alien.body:
                    self.iteration_alien = 0
                    self.alien_block_count = len(game.Alien.body)
                    self.iter_max_alien = self.alien_block_count - 1
                    while self.iteration_alien <= self.iter_max_alien:
                        alien = game.Alien.body[self.iteration_alien]
                        laser = game.Laser.body[self.iteration_laser]
                        if alien.x == laser.x and alien.y == laser.y:
                            game.Alien.body.__delitem__(self.iteration_alien)
                            self.point += 50
                            break
                        self.iteration_alien += 1
                self.iteration_laser += 1

    def check_colision_laserb(self):
        self.iteration_laser = 0
        self.laser_block_count = len(game.Laser.body)
        self.iter_max_laser = self.laser_block_count - 1
        if game.Laser.body:
            while self.iteration_laser <= self.iter_max_laser:
                if game.Alienb.body:
                    self.iteration_Alienb = 0
                    self.Alienb_block_count = len(game.Alienb.body)
                    self.iter_max_Alienb = self.Alienb_block_count - 1
                    while self.iteration_Alienb <= self.iter_max_Alienb:
                        Alienb = game.Alienb.body[self.iteration_Alienb]
                        laser = game.Laser.body[self.iteration_laser]
                        if Alienb.x == laser.x and Alienb.y == laser.y:
                            game.Alienb.body.__delitem__(self.iteration_Alienb)
                            self.point += 50
                            break
                        self.iteration_Alienb += 1
                self.iteration_laser += 1

    def check_colision_laser_alien(self):
        iteration = 0
        laser_length = len(game.Laser_alien.body)
        for blockb in game.Bouclier.body:
            self.xb = blockb.x
            self.yb = blockb.y
        for block in game.Vaisseau.body:
            self.x = block.x
            self.y = block.y
        for laser in game.Laser_alien.body[0:laser_length]:
            if game.draw_Bouclier and laser.x == self.xb and laser.y == self.yb:
                game.Vaisseau.PVB -= 1
                if game.Vaisseau.PVB == 0:
                    game.Bouclier.body = []
                    game.draw_Bouclier = False
                game.Laser_alien.body.__delitem__(iteration)
            elif laser.x == self.x and laser.y == self.y:
                game.Vaisseau.PV -= 1
                game.Vaisseau.Touche = 10
                if game.Vaisseau.PV == 0:
                    self.game_over()
            iteration += 1

    def check_colision_laser_alienb(self):
        iteration = 0
        laser_length = len(game.Laser_Alienb.body)
        for blockb in game.Bouclier.body:
            self.xb = blockb.x
            self.yb = blockb.y
        for block in game.Vaisseau.body:
            self.x = block.x
            self.y = block.y
        for laser in game.Laser_Alienb.body[0:laser_length]:
            if game.draw_Bouclier and laser.x == self.xb and laser.y == self.yb:
                game.Vaisseau.PVB -= 1
                if game.Vaisseau.PVB == 0:
                    game.Bouclier.body = []
                    game.draw_Bouclier = False
                game.Laser_Alienb.body.__delitem__(iteration)
            elif laser.x == self.x and laser.y == self.y:
                game.Vaisseau.PV -= 1
                game.Vaisseau.Touche = 10
                if game.Vaisseau.PV == 0:
                    self.game_over()
            iteration += 1

    def game_over(self):
        if self.Vaisseau.Highscore < self.point:
            self.Vaisseau.Highscore = self.point
        self.Vaisseau.argent += int(self.point / 10)
        self.sauvegarde()
        self.point = 0
        game.Alien.body = []
        game.Alienb.body = []
        game.Vaisseau.body = [Block(15, 37)]
        game.Laser.body = []
        game.Laser_alien.body = []
        game.Laser_Alienb.body = []
        game.Alien.level = 1
        game.Vaisseau.PV = game.Vaisseau.PV_Max
        self.ecran_accueil = True

    def sauvegarde(self):
        player = {"Highscore":self.Vaisseau.Highscore,
                  "Argent":self.Vaisseau.argent,
                  "PV_Max":self.Vaisseau.PV_Max,
                  "BOUC_MAX":self.Vaisseau.LVL_BOUCLIER,
                  "LVL_CANON":self.Vaisseau.LVL_canon,
                  "LVL_CANON2":self.Vaisseau.LVL_canon2,
                  "LVL_VAISSEAU":self.Vaisseau.Level}
        fichierSauvegarde = open("save/sauvegarde.json", "wb")
        pickle.dump(player, fichierSauvegarde)
        fichierSauvegarde.close()

    def chargement(self):
        fichierSauvegarde = open("save/sauvegarde.json", "rb")
        variables = pickle.load(fichierSauvegarde)
        fichierSauvegarde.close()
        self.Vaisseau.Highscore = variables["Highscore"]
        self.Vaisseau.argent = variables["Argent"]
        self.Vaisseau.PV_Max = variables["PV_Max"]
        self.Vaisseau.LVL_BOUCLIER = variables["BOUC_MAX"]
        self.Vaisseau.LVL_canon = variables["LVL_CANON"]
        self.Vaisseau.LVL_canon2 = variables["LVL_CANON2"]
        self.Vaisseau.Level = variables["LVL_VAISSEAU"]
        game.Vaisseau.chauffe_max = (10 * self.Vaisseau.LVL_canon)

    def affichage_menu(self):
        self.font = pygame.font.Font(None, 25)
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.Argent_Player = self.myfont.render("Argent Disponible : " + str(self.Vaisseau.argent), True, pygame.Color("Black"))
        self.Argent_Player_center = self.Argent_Player.get_rect(center=((Nb_Col * Cell_Size) / 2, (Nb_Row * Cell_Size) - 90))
        self.Meilleur_Score = self.myfont.render("Meilleur Score : " + str(self.Vaisseau.Highscore), True, pygame.Color("Black"))
        self.Meilleur_Score_center = self.Meilleur_Score.get_rect(center=((Nb_Col * Cell_Size) / 2, (Nb_Row * Cell_Size) - 60))
        self.Score_Actuel = self.myfont.render("Score Actuel : " + str(self .point), True, pygame.Color("Black"))
        self.Score_Actuel_center= self.Score_Actuel.get_rect(center=((Nb_Col * Cell_Size)/2, (Nb_Row * Cell_Size)-30))
        self.image = pygame.image.load("images/menu.png")
        self.image = pygame.transform.scale(self.image, (30*Cell_Size, 25*Cell_Size))
        if game.Vaisseau.LVL_BOUCLIER < (5 * game.Vaisseau.Level):
            self.Prix_BC = (500*game.Vaisseau.LVL_BOUCLIER**2)
        else:
            self.Prix_BC = "MaX"
        if game.Vaisseau.PV_Max < (5 * game.Vaisseau.Level):
            self.Prix_PV = (500*game.Vaisseau.PV_Max**2)
        else:
            self.Prix_PV = "Max"
        if game.Vaisseau.LVL_canon < (5 * game.Vaisseau.Level):
            self.Prix_CANON = (500*game.Vaisseau.LVL_canon**2)
        else:
            self.Prix_CANON = "Max"
        if game.Vaisseau.LVL_canon2 < (5 * game.Vaisseau.Level):
            self.Prix_CANON2 = (500*game.Vaisseau.LVL_canon2**2)
        else:
            self.Prix_CANON2 = "Max"

        if game.Vaisseau.Level < (5 * game.Vaisseau.Level):
            self.Prix_VAISSEAU = (500*game.Vaisseau.Level**3)
        else:
            self.Prix_VAISSEAU = "Max"

        screen.fill(pygame.Color("White"))
        screen.blit(self.image, (0, -180))
        screen.blit(self.Score_Actuel, self.Score_Actuel_center)
        screen.blit(self.Meilleur_Score, self.Meilleur_Score_center)
        screen.blit(self.Argent_Player, self.Argent_Player_center)

        self.PV_rect = pygame.Rect(10, (Cell_Size * 15), (6 * Cell_Size), (2 * Cell_Size))
        pygame.draw.rect(screen, pygame.Color("Grey"), self.PV_rect)
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        PV_MAX = myfont.render('PV MAX : ' + str(game.Vaisseau.PV_Max), False, (255, 255, 255))
        self.PV_rect_plus = pygame.Rect((20 + (Cell_Size * 6)), (Cell_Size * 15), (2 * Cell_Size), (2 * Cell_Size))
        pygame.draw.rect(screen, pygame.Color("Grey"), self.PV_rect_plus)
        PV_plus = myfont.render(" + ", False, (255, 255, 255))
        self.PV_rect_prix = pygame.Rect((30 + (Cell_Size * 8)), (Cell_Size * 15), (4 * Cell_Size), (2 * Cell_Size))
        pygame.draw.rect(screen, pygame.Color("Grey"), self.PV_rect_prix)
        PV_prix = myfont.render(str(self.Prix_PV), False, (255, 255, 255))
        screen.blit(PV_MAX, self.PV_rect)
        screen.blit(PV_plus, self.PV_rect_plus)
        screen.blit(PV_prix, self.PV_rect_prix)

        self.BC_rect = pygame.Rect(10, (Cell_Size * 17), (6 * Cell_Size), (2 * Cell_Size))
        LVL_BOUCLIER = myfont.render('Lvl Bouc : ' + str(game.Vaisseau.LVL_BOUCLIER), False, (255, 255, 255))
        self.BC_rect_plus = pygame.Rect((20 + (Cell_Size * 6)), (Cell_Size * 17), (2 * Cell_Size), (2 * Cell_Size))
        BC_plus = myfont.render(" + ", False, (255, 255, 255))
        self.BC_rect_prix = pygame.Rect((30 + (Cell_Size * 8)), (Cell_Size * 17), (4 * Cell_Size), (2 * Cell_Size))
        BC_prix = myfont.render(str(self.Prix_BC), False, (255, 255, 255))
        if game.Vaisseau.PV_Max >= 2:
            pygame.draw.rect(screen, pygame.Color("Grey"), self.BC_rect)
            screen.blit(LVL_BOUCLIER, self.BC_rect)
            pygame.draw.rect(screen, pygame.Color("Grey"), self.BC_rect_plus)
            screen.blit(BC_plus, self.BC_rect_plus)
            pygame.draw.rect(screen, pygame.Color("Grey"), self.BC_rect_prix)
            screen.blit(BC_prix, self.BC_rect_prix)

        self.CANON_rect = pygame.Rect(10, (Cell_Size * 19), (6 * Cell_Size), (2 * Cell_Size))
        LVL_CANON = myfont.render('Lvl Canon : ' + str(game.Vaisseau.LVL_canon), False, (255, 255, 255))
        self.CANON_rect_plus = pygame.Rect((20 + (Cell_Size * 6)), (Cell_Size * 19), (2 * Cell_Size), (2 * Cell_Size))
        CANON_plus = myfont.render(" + ", False, (255, 255, 255))
        self.CANON_rect_prix = pygame.Rect((30 + (Cell_Size * 8)), (Cell_Size * 19), (4 * Cell_Size), (2 * Cell_Size))
        CANON_prix = myfont.render(str(self.Prix_CANON), False, (255, 255, 255))
        if game.Vaisseau.LVL_BOUCLIER >=2:
            pygame.draw.rect(screen, pygame.Color("Grey"), self.CANON_rect)
            screen.blit(LVL_CANON, self.CANON_rect)
            pygame.draw.rect(screen, pygame.Color("Grey"), self.CANON_rect_plus)
            screen.blit(CANON_plus, self.CANON_rect_plus)
            pygame.draw.rect(screen, pygame.Color("Grey"), self.CANON_rect_prix)
            screen.blit(CANON_prix, self.CANON_rect_prix)

        self.VAISSEAU_rect = pygame.Rect(((Nb_Col - 12) * Cell_Size) - 30, (Cell_Size * 15), (6 * Cell_Size), (2 * Cell_Size))
        LVL_VAISSEAU = myfont.render('Lvl VAIS. : ' + str(game.Vaisseau.Level), False, (255, 255, 255))
        self.VAISSEAU_rect_plus = pygame.Rect(((Nb_Col - 6) * Cell_Size) - 20, (Cell_Size * 15), (2 * Cell_Size), (2 * Cell_Size))
        VAISSEAU_plus = myfont.render(" + ", False, (255, 255, 255))
        self.VAISSEAU_rect_prix = pygame.Rect(((Nb_Col - 4) * Cell_Size) - 10, (Cell_Size * 15), (4 * Cell_Size), (2 * Cell_Size))
        VAISSEAU_prix = myfont.render(str(self.Prix_VAISSEAU), False, (255, 255, 255))
        if game.Vaisseau.LVL_BOUCLIER >= 5 and game.Vaisseau.PV_Max >= 5 and game.Vaisseau.LVL_canon >= 5:
            pygame.draw.rect(screen, pygame.Color("Grey"), self.VAISSEAU_rect)
            screen.blit(LVL_VAISSEAU, self.VAISSEAU_rect)
            pygame.draw.rect(screen, pygame.Color("Grey"), self.VAISSEAU_rect_plus)
            screen.blit(VAISSEAU_plus, self.VAISSEAU_rect_plus)
            pygame.draw.rect(screen, pygame.Color("Grey"), self.VAISSEAU_rect_prix)
            screen.blit(VAISSEAU_prix, self.VAISSEAU_rect_prix)

        self.CANON2_rect = pygame.Rect(10, (Cell_Size * 21), (9 * Cell_Size), (2 * Cell_Size))
        LVL_CANON2 = myfont.render('Lvl Mega canon : ' + str(game.Vaisseau.LVL_canon2), False, (255, 255, 255))
        self.CANON2_rect_plus = pygame.Rect((20 + (Cell_Size * 9)), (Cell_Size * 21), (2 * Cell_Size), (2 * Cell_Size))
        CANON2_plus = myfont.render(" + ", False, (255, 255, 255))
        self.CANON2_rect_prix = pygame.Rect((30 + (Cell_Size * 11)), (Cell_Size * 21), (4 * Cell_Size), (2 * Cell_Size))
        CANON2_prix = myfont.render(str(self.Prix_CANON2), False, (255, 255, 255))
        if game.Vaisseau.Level >= 2:
            pygame.draw.rect(screen, pygame.Color("Grey"), self.CANON2_rect)
            screen.blit(LVL_CANON2, self.CANON2_rect)
            pygame.draw.rect(screen, pygame.Color("Grey"), self.CANON2_rect_plus)
            screen.blit(CANON2_plus, self.CANON2_rect_plus)
            pygame.draw.rect(screen, pygame.Color("Grey"), self.CANON2_rect_prix)
            screen.blit(CANON2_prix, self.CANON2_rect_prix)


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.PV_rect_plus.collidepoint(pygame.mouse.get_pos()) and game.Vaisseau.PV_Max < (5 * game.Vaisseau.Level) and game.Prix_PV < game.Vaisseau.argent:
                    game.Vaisseau.PV_Max += 1
                    game.Vaisseau.argent -= game.Prix_PV
                if self.BC_rect_plus.collidepoint(pygame.mouse.get_pos()) and game.Vaisseau.LVL_BOUCLIER < (5 * game.Vaisseau.Level) and game.Prix_BC < game.Vaisseau.argent:
                    game.Vaisseau.LVL_BOUCLIER += 1
                    game.Vaisseau.argent -= game.Prix_BC
                if self.CANON_rect_plus.collidepoint(pygame.mouse.get_pos()) and game.Vaisseau.LVL_canon < (5 * game.Vaisseau.Level) and game.Prix_CANON < game.Vaisseau.argent:
                    game.Vaisseau.LVL_canon += 1
                    game.Vaisseau.argent -= game.Prix_CANON
                if self.VAISSEAU_rect_plus.collidepoint(pygame.mouse.get_pos()) and game.Vaisseau.Level < (5 * game.Vaisseau.Level) and game.Prix_VAISSEAU < game.Vaisseau.argent:
                    game.Vaisseau.Level += 1
                    game.Vaisseau.argent -= game.Prix_VAISSEAU
                if self.CANON2_rect_plus.collidepoint(pygame.mouse.get_pos()) and game.Vaisseau.Level < (5 * game.Vaisseau.Level) and game.Prix_CANON2 < game.Vaisseau.argent:
                    game.Vaisseau.LVL_canon2 += 1
                    game.Vaisseau.argent -= game.Prix_CANON2

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.ecran_accueil = False
                    game.Vaisseau.PV = game.Vaisseau.PV_Max
                if event.key == pygame.K_s:
                    self.sauvegarde()

class Vaisseau:
    def __init__(self):
        self.body = [Block(15, 37)]
        self.direction = ""
        self.new_head = ""
        self.Touche = 0
        if self.Touche == 0:
            self.image = pygame.image.load("images/player.png")
        else:
            self.image = pygame.image.load("images/explosion3.png")
            self.Touche -= 1
        self.image = pygame.transform.scale(self.image, (Cell_Size, Cell_Size))
        self.argent = 0
        self.Highscore = 0
        self.PV_Max = 1
        self.LVL_BOUCLIER = 1
        self.LVL_canon = 1
        self.PV = self.PV_Max
        self.chauffe_max = (10 * self.LVL_canon)
        self.PVB = 0
        self.Level = 1
        self.LVL_canon2 = 1

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
    

class Bouclier:
    def __init__(self):
        self.body = []
        self.image = pygame.image.load("images/bouclier.png")
        self.image = pygame.transform.scale(self.image, (Cell_Size, Cell_Size))
        self.Vaisseau = Vaisseau()

    def draw_bouclier(self):
        if game.Bouclier.body:
            for block in self.body:
                x_coord = block.x * Cell_Size
                y_coord = block.y * Cell_Size
                screen.blit(self.image,(x_coord, y_coord))

    def new_bouclier(self):
        self.body = []
        if game.Vaisseau.body:
            for block in game.Vaisseau.body:
                self.x_coord: int = block.x
                self.y_coord: int = (block.y - 1)
                self.Nbouclier = Block(self.x_coord, self.y_coord)
                self.body.append(self.Nbouclier)

class Laser_alien:
    def __init__(self):
        self.Alien = Alien()
        self.body = []
        self.image = pygame.image.load("images/laser2.png")
        self.image = pygame.transform.scale(self.image, (Cell_Size, Cell_Size))

    def draw_laser(self):
        if game.Laser_alien.body:
            for block in self.body:
                x_coord = block.x * Cell_Size
                y_coord = block.y * Cell_Size
                screen.blit(self.image,(x_coord, y_coord))

    def new_laser(self):
        if game.Alien.body:
            for block in game.Alien.body:
                self.x_coord: int = block.x
                self.y_coord: int = (block.y + 1)
                self.Nlaser = Block(self.x_coord, self.y_coord)
                self.body.append(self.Nlaser)

    def move_laser(self):
        self.iteration = 0
        self.laser_block_count = len(self.body)
        self.iter_max = self.laser_block_count - 1
        if self.laser_block_count > 0:
            while self.iteration <= self.iter_max:
                self.old_pos = self.body[self.iteration]
                self.new_pos = Block(self.old_pos.x, self.old_pos.y + 1)
                if self.old_pos.y + 1 == 41:
                    self.body.__delitem__(self.iteration)
                    break
                else:
                    self.body[self.iteration] = self.new_pos
                self.iteration += 1

class Laser_Alienb:
    def __init__(self):
        self.Alienb = Alienb()
        self.body = []
        self.image = pygame.image.load("images/laser2.png")
        self.image = pygame.transform.scale(self.image, (Cell_Size, Cell_Size))

    def draw_laser(self):
        if game.Laser_Alienb.body:
            for block in self.body:
                x_coord = block.x * Cell_Size
                y_coord = block.y * Cell_Size
                screen.blit(self.image,(x_coord, y_coord))

    def new_laser(self):
        if game.Alienb.body:
            for block in game.Alienb.body:
                self.x_coord: int = block.x
                self.y_coord: int = (block.y + 1)
                self.Nlaser = Block(self.x_coord, self.y_coord)
                self.body.append(self.Nlaser)

    def move_laser(self):
        self.iteration = 0
        self.laser_block_count = len(self.body)
        self.iter_max = self.laser_block_count - 1
        if self.laser_block_count > 0:
            while self.iteration <= self.iter_max:
                self.old_pos = self.body[self.iteration]
                self.new_pos = Block(self.old_pos.x, self.old_pos.y + 1)
                if self.old_pos.y + 1 == 41:
                    self.body.__delitem__(self.iteration)
                    break
                else:
                    self.body[self.iteration] = self.new_pos
                self.iteration += 1

class Laser:
    def __init__(self):
        self.Vaisseau = Vaisseau()
        self.body = []
        self.image = pygame.image.load("images/laser1.png")
        self.image = pygame.transform.scale(self.image, (Cell_Size, Cell_Size))
        self.cooldown = 100


    def draw_laser(self):
        for block in self.body:
            x_coord = block.x * Cell_Size
            y_coord = block.y * Cell_Size
            screen.blit(self.image,(x_coord, y_coord))

    def new_laser(self):
        self.cooldown -= (5 * game.Vaisseau.LVL_canon2)
        Vaisseau_pos = game.Vaisseau.body[0]
        self.y: int = Vaisseau_pos.y - 1
        self.x: int = Vaisseau_pos.x
        self.Nlaser = Block(self.x, self.y)
        self.body.append(self.Nlaser)
        print(self.cooldown)
        if self.cooldown <= 0 and game.Vaisseau.Level >= 2:
            self.xg: int = Vaisseau_pos.x - 1
            self.xd: int = Vaisseau_pos.x + 1
            self.Nlaser2 = Block(self.xg, self.y)
            self.body.append(self.Nlaser2)
            self.Nlaser3 = Block(self.xd, self.y)
            self.body.append(self.Nlaser3)
            self.cooldown = 100
            print("Triple")
        game.chauffe += 3
        if game.chauffe >= game.Vaisseau.chauffe_max:
            game.pop_Laser = False

    def move_laser(self):
        self.iteration = 0
        self.laser_block_count = len(self.body)
        self.iter_max = self.laser_block_count - 1
        if self.laser_block_count > 0:
            while self.iteration <= self.iter_max:
                self.old_pos = self.body[self.iteration]
                self.new_pos = Block(self.old_pos.x, self.old_pos.y - 1)
                if self.old_pos.y - 1 == -1:
                    self.body.__delitem__(self.iteration)
                    break
                else:
                    self.body[self.iteration] = self.new_pos
                self.iteration += 1


class Alien:
    def __init__(self):
        self.body = []
        self.image = pygame.image.load("images/alien1.png")
        self.image = pygame.transform.scale(self.image, (Cell_Size, Cell_Size))
        self.level = 1

    def new_alien(self):
        self.y: int = 0
        self.x: int = random.randint(0, Nb_Col - 1)
        self.Nalien = Block(self.x, self.y)
        self.body.append(self.Nalien)

    def draw_alien(self):
        self.interation = 0
        self.alien_block_count = len(self.body)
        self.iter_max = self.alien_block_count - 1
        if self.body:
            for block in self.body:
                self.x_coord = block.x * Cell_Size
                self.y_coord = block.y * Cell_Size
                screen.blit(self.image,(self.x_coord, self.y_coord))

    def move_alien(self):
        self.iteration = 0
        self.alien_block_count = len(self.body)
        self.iter_max = self.alien_block_count - 1
        if game.Alien.body:
            while self.iteration <= self.iter_max:
                self.old_pos = self.body[self.iteration]
                if self.old_pos.x == 0:
                    self.direction = random.randint(0, 1)
                    self.x = self.old_pos.x + self.direction
                elif self.old_pos.x == 29:
                    self.direction = random.randint(-1, 0)
                    self.x = self.old_pos.x + self.direction
                else:
                    self.direction = random.randint(-1, 1)
                    self.x = self.old_pos.x + self.direction
                self.new_pos = Block(self.x, self.old_pos.y + 1)
                if self.old_pos.y == 41:
                    self.body.__delitem__(self.iteration)
                    break
                else:
                    self.body[self.iteration] = self.new_pos
                self.iteration += 1

class Alienb:
    def __init__(self):
        self.body = []
        self.image = pygame.image.load("images/alien1.png")
        self.image = pygame.transform.scale(self.image, (Cell_Size, Cell_Size))
        self.level = 1

    def new_alien(self):
        self.y: int = random.randint(0, Nb_Col / 2)
        self.x: int = 0
        self.Nalien = Block(self.x, self.y)
        self.body.append(self.Nalien)

    def draw_alien(self):
        self.interation = 0
        self.alien_block_count = len(self.body)
        self.iter_max = self.alien_block_count - 1
        if self.body:
            for block in self.body:
                self.x_coord = block.x * Cell_Size
                self.y_coord = block.y * Cell_Size
                screen.blit(self.image,(self.x_coord, self.y_coord))

    def move_alien(self):
        self.iteration = 0
        self.alien_block_count = len(self.body)
        self.iter_max = self.alien_block_count - 1
        if game.Alienb.body:
            while self.iteration <= self.iter_max:
                self.old_pos = self.body[self.iteration]
                self.new_pos = Block(self.old_pos.x +1, self.old_pos.y)
                if self.old_pos.x == 31:
                    self.body.__delitem__(self.iteration)
                    break
                else:
                    self.body[self.iteration] = self.new_pos
                self.iteration += 1

class Block:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos


game_on = True

game = Game()
Sound = pygame.mixer.Sound('sound/Electronika.wav')
#Sound.play(loops=-1, maxtime=0, fade_ms=0)

chemin = pathlib.Path(__file__).parent
file = pathlib.Path(chemin / "save" / "sauvegarde.json")
if file.is_file():
    game.chargement()

SCREEN_UPDATE = pygame.USEREVENT

pygame.time.set_timer(SCREEN_UPDATE, game.FPS)
boucle = 0
bouclier = 0


while game_on:
    while game.ecran_accueil:
        game.affichage_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.Vaisseau.direction != "TOP":
                    game.Vaisseau.direction = "TOP"
            if event.key == pygame.K_DOWN:
                if game.Vaisseau.direction != "DOWN":
                    game.Vaisseau.direction = "DOWN"
            if event.key == pygame.K_LEFT:
                if game.Vaisseau.direction != "LEFT":
                    game.Vaisseau.direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                if game.Vaisseau.direction != "RIGHT":
                    game.Vaisseau.direction = "RIGHT"
            if event.key == pygame.K_SPACE:
                if game.chauffe < game.Vaisseau.chauffe_max:
                    game.pop_Laser = True
            if event.key == pygame.K_b:
                if game.Vaisseau.PVB == 0:
                    game.pop_Bouclier = True
                    game.Vaisseau.PVB = game.Vaisseau.LVL_BOUCLIER
                    bouclier = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                game.pop_Laser = False


    screen.fill(pygame.Color("blue"))
    screen.blit(game.fond, (0, 0))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    Score = myfont.render('Score : ' + str(game.point), False, (255, 255, 255))
    HScore = myfont.render('Meilleur Score : ' + str(game.Vaisseau.Highscore), False, (255, 255, 255))
    PV = myfont.render('Vie : ' + str(game.Vaisseau.PV), False, (255, 255, 255))
    BC = myfont.render('Bouclier : ' + str(game.Vaisseau.PVB), False, (255, 255, 255))
    screen.blit(Score, (0, 0))
    screen.blit(HScore, (0, 40))
    screen.blit(PV, (0, (Cell_Size*(Nb_Row -1))-10))
    screen.blit(BC, ((Cell_Size * 8), (Cell_Size * (Nb_Row - 1)) - 10))
    if game.Alien.level < 2:
        if game.point > (game.Alien.level * 500):
            game.Alien.level += 1
    else:
        if game.point > (game.Alien.level * 1000):
            game.Alien.level += 1
    if boucle % 20 == 0:
        if game.chauffe > 0:
            game.chauffe -= 2 * game.Vaisseau.LVL_canon
    if boucle % 300 == 0:
        game.pop_Laser_Alien = True
    if boucle % 200 == 0:
        game.pop_Alien = True
    if boucle % 600 == 0:
        game.pop_Alienb = True
    if boucle % 100 == 0:
        game.move_Alien = True
    #if bouclier == (150*game.Vaisseau.LVL_BOUCLIER):
    #    game.draw_Bouclier = False
    #    game.Bouclier.body = []
    game.update()
    pygame.display.update()
    boucle += 1
    bouclier += 1
    game.FPS = 60 + (int(game.point / 10))
    timer.tick(game.FPS)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
