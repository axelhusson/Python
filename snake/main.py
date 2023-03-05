# This is a sample Python script.

import random
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys

import pygame


class Block:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos


class Food:
    def __init__(self):
        x = random.randint(0, Nb_Col - 1)
        y = random.randint(0, Nb_Row - 1)
        self.block = Block(x, y)

    def draw_food(self):
        rect = pygame.Rect(self.block.x * Cell_Size, self.block.y * Cell_Size, Cell_Size, Cell_Size)
        pygame.draw.rect(screen, pygame.Color("green"), rect)

class Baie:
    def __init__(self):
        self.body = []

    def draw_baie(self):
        for block in self.body:
            x_coord = block.x * Cell_Size
            y_coord = block.y * Cell_Size
            baie_rect = pygame.Rect(x_coord, y_coord, Cell_Size, Cell_Size)
            pygame.draw.rect(screen, pygame.Color("red"), baie_rect)

    def new_baie(self):
        self.y: int = random.randint(0, Nb_Row - 1)
        self.x: int = random.randint(0, Nb_Col - 1)
        self.Nbaie = Block(self.x, self.y)
        self.body.append(self.Nbaie)

    def reset_baie(self):
        self.body = []

class Mur:
    def __init__(self):
        self.body = [Block(3, 12)]

    def draw_mur(self):
        for block in self.body:
            x_coord = block.x * Cell_Size
            y_coord = block.y * Cell_Size
            mur_rect = pygame.Rect(x_coord, y_coord, Cell_Size, Cell_Size)
            pygame.draw.rect(screen, pygame.Color("black"), mur_rect)

    def new_mur(self):
        self.y: int = random.randint(0, Nb_Row - 1)
        self.x: int = random.randint(0, Nb_Col - 1)
        self.new_mure = Block(self.x, self.y)
        self.body.append(self.new_mure)

    def reset_mur(self):
        self.body = [Block(3, 12)]


class Snake:
    def __init__(self):
        self.body = [Block(2, 6), Block(3, 6), Block(4, 6)]
        self.direction = "RIGHT"
        self.new_head = []

    def draw_snake(self):
        for block in self.body:
            x_coord = block.x * Cell_Size
            y_coord = block.y * Cell_Size
            block_rect = pygame.Rect(x_coord, y_coord, Cell_Size, Cell_Size)
            pygame.draw.rect(screen, pygame.Color("blue"), block_rect)

    def move_snake(self):

        snake_block_count = len(self.body)
        old_head = self.body[snake_block_count - 1]

        if self.direction == "RIGHT":
            self.new_head = Block(old_head.x + 1, old_head.y)
        elif self.direction == "LEFT":
            self.new_head = Block(old_head.x - 1, old_head.y)
        elif self.direction == "TOP":
            self.new_head = Block(old_head.x, old_head.y - 1)
        elif self.direction == "DOWN":
            self.new_head = Block(old_head.x, old_head.y + 1)

        self.body.append(self.new_head)

    def reset_snake(self):
        self.body = [Block(2, 6), Block(3, 6), Block(4, 6)]
        self.direction = "RIGHT"


class Game:
    def __init__(self):
        self.FPS = 150
        self.point = 0
        self.HScore = 0
        self.snake = Snake()
        self.food = Food()
        self.mur = Mur()
        self.baie = Baie()
        self.generate_food()
        self.ecran_accueil = True

    def update(self):
        print(self.FPS)
        pygame.time.set_timer(SCREEN_UPDATE, game.FPS)
        self.snake.move_snake()
        self.check_head_on_baie()
        self.check_head_on_food()
        self.game_over()

    def draw_game_element(self):
        self.food.draw_food()
        self.snake.draw_snake()
        self.mur.draw_mur()
        self.baie.draw_baie()

    def check_head_on_food(self):
        snake_length = len(self.snake.body)
        snake_head_block = self.snake.body[snake_length - 1]
        food_block = self.food.block

        if snake_head_block.x == food_block.x and snake_head_block.y == food_block.y:
            self.generate_food()
            self.mur.new_mur()
            self.point += 1
            self.FPS -= 2
            if (self.point % 5) == 0:
                self.baie.new_baie()
                self.FPS -= 3
        else:
            self.snake.body.pop(0)

    def check_head_on_baie(self):
        snake_length = len(self.snake.body)
        snake_head = self.snake.body[snake_length - 1]
        baie_length = len(self.baie.body)
        iteration = 0
        for i in self.baie.body[0:baie_length]:
            if i.x == snake_head.x and i.y == snake_head.y:
                self.snake.body.pop(0)
                self.snake.body.pop(0)
                self.baie.body.pop(int(iteration))
            iteration += 1



    def generate_food(self):
        should_generate_food = True
        while should_generate_food:
            count = 0
            self.food = Food()
            for block in self.snake.body:
                if block.x == self.food.block.x and block.y == self.food.block.y:
                    count += 1
            for block in self.mur.body:
                if block.x == self.food.block.x and block.y == self.food.block.y:
                    count += 1
            for block in self.baie.body:
                if block.x == self.food.block.x and block.y == self.food.block.y:
                    count += 1
            if count == 0:
                should_generate_food = False


    def game_over(self):
        snake_length = len(self.snake.body)
        mur_length = len(self.mur.body)
        snake_head = self.snake.body[snake_length - 1]
        if (snake_head.x not in range(0, Nb_Col)) or (snake_head.y not in range(0, Nb_Row)):
            self.snake.reset_snake()
            self.mur.reset_mur()
            self.baie.reset_baie()
            if self.point > self.HScore:
                self.HScore = self.point
            self.point = 0
            self.FPS = 150
            self.ecran_accueil = True
        for block in self.snake.body[0:snake_length - 1]:
            if block.x == snake_head.x and block.y == snake_head.y:
                self.snake.reset_snake()
                self.mur.reset_mur()
                self.baie.reset_baie()
                if self.point > self.HScore:
                    self.HScore = self.point
                self.point = 0
                self.FPS = 150
                self.ecran_accueil = True
        for block in self.mur.body[0:mur_length]:
            if block.x == snake_head.x and block.y == snake_head.y:
                self.snake.reset_snake()
                self.mur.reset_mur()
                self.baie.reset_baie()
                if self.point > self.HScore:
                    self.HScore = self.point
                self.point = 0
                self.FPS = 150
                self.ecran_accueil = True

    def affichage_menu(self):
        self.font = pygame.font.Font(None, 25)
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.Meilleur_Score = self.myfont.render("Meilleur Score : " + str(self.HScore), True, pygame.Color("Black"))
        self.Meilleur_Score_center = self.Meilleur_Score.get_rect(center=((Nb_Col * Cell_Size) / 2, (Nb_Row * Cell_Size) - 60))
        self.Score_Actuel = self.myfont.render("Score Actuel : " + str(self.point), True, pygame.Color("Black"))
        self.Score_Actuel_center= self.Score_Actuel.get_rect(center=((Nb_Col * Cell_Size)/2, (Nb_Row * Cell_Size)-30))
        self.image = pygame.image.load("images/Snake_2021.png")
        screen.fill(pygame.Color("Grey"))
        screen.blit(self.image, (0, 0))
        screen.blit(self.Score_Actuel, self.Score_Actuel_center)
        screen.blit(self.Meilleur_Score, self.Meilleur_Score_center)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.ecran_accueil = False


pygame.init()
pygame.font.init()

Nb_Col = 40
Nb_Row = 60
Cell_Size = 10

screen = pygame.display.set_mode(size=(Nb_Col * Cell_Size, Nb_Row * Cell_Size))
timer = pygame.time.Clock()

game_on = True

game = Game()


SCREEN_UPDATE = pygame.USEREVENT

pygame.time.set_timer(SCREEN_UPDATE, game.FPS)


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
                if game.snake.direction != "DOWN":
                    game.snake.direction = "TOP"
            if event.key == pygame.K_DOWN:
                if game.snake.direction != "TOP":
                    game.snake.direction = "DOWN"
            if event.key == pygame.K_LEFT:
                if game.snake.direction != "RIGHT":
                    game.snake.direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                if game.snake.direction != "LEFT":
                    game.snake.direction = "RIGHT"
            if event.key == pygame.K_p:
                game.ecran_accueil = True

    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    Score = myfont.render('Score : ' + str(game.point), False, (0, 0, 0))
    screen.fill(pygame.Color("grey"))
    screen.blit(Score, (0, 0))
    game.draw_game_element()
    pygame.display.update()
    timer.tick(60)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
