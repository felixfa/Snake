import pygame
from pygame.locals import *
import time
import random

SIZE=40
BACKGROUND_COLOR = (110, 110, 5)

class Apple:
    def __init__(self, surface):
        self.parent_screen = surface
        self.block = pygame.image.load("resources/apple.jpg").convert()
        self.x = SIZE*5
        self.y = SIZE*4
    
    def draw(self):
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0,19) * SIZE
        self.y = random.randint(0,19) * SIZE


class Snake:
    def __init__(self, surface,length):
        self.length=length
        self.parent_screen = surface
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [SIZE]*length
        self.y = [SIZE]*length
        self.direction = 'down'

    def increase_size(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
        

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):

        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]


        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()


    def draw(self):
        self.parent_screen.fill(BACKGROUND_COLOR)

        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((800 ,800))
        self.snake = Snake(self.surface, 7)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def display_score(self):
        font = pygame.font.SysFont('arial',40)
        score = font.render(f"Score: {self.snake.length - 1}", True, (0,0,0))
        self.surface.blit(score,(630,10))

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True
        return False
    

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        #snake colliding with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.apple.move()
            self.snake.increase_size()

        #snake colliding with itself
        for i in range(3,self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game over"
    
    def show_game_over(self):
        self.surface.fill((110, 110, 5))
        font = pygame.font.SysFont('arial',40)
        line1 = font.render(f"GAME OVER! Your score is {self.snake.length - 1}", True, (0,0,0))
        self.surface.blit(line1,(100,200))
        pygame.display.flip()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
            
            time.sleep(.2)
    

if __name__ == '__main__':
    game = Game()
    game.run()

 