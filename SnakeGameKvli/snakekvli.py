import pygame
import random

pygame.init()

pygame.display.set_caption('SnakeGame')
screen = pygame.display.set_mode((800, 600))


backgroundimage=pygame.image.load('background.jpg')
foodimage=pygame.image.load('food.png')
endImage=pygame.image.load('endgame.jpg')


class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.radius = 10
        self.dx = 5 
        self.dy = 0
        self.is_add = False
        self.score=0
        self.color=(255,255,255)

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (self.color), element, self.radius)

    def move(self):
        if self.is_add:
            self.size += 1
            self.elements.append([0, 0])
            self.is_add = False

        for i in range(len(self.elements) - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy
    

class Food:
    def __init__(self):
        self.x=random.randint(30,740)
        self.y=random.randint(30,540)
    def draw(self):
        screen.blit(foodimage, (self.x, self.y))    
def Collision():
     if (food.x>= snake.elements[0][0]-20 and food.x<snake.elements[0][0]+20) and  (food.y >= snake.elements[0][1] -20 and food.y<snake.elements[0][1] +20):
        snake.is_add = True  
        if snake.is_add == True:
            snake.score +=1
            food.x = random.randint(10, 750)
            food.y = random.randint(10, 550)
def Scores():
    font = pygame.font.SysFont("Calibri", 30)
    score = font.render("Score: " + str(snake.score), True, (255,0,0))
    screen.blit(score, (630, 17))
def border():
        if snake.elements[0][0]>=780 or snake.elements[0][0]<=20 or snake.elements[0][1]<=20 or snake.elements[0][1]>=580:
            return True
        return False    
def Suicide():
    for block in snake.elements[1:]:
        if snake.elements[0][0] == block[0] and snake.elements[0][1] == block[1]:
            return True
    return False
def the_end():
    snake.dx=0
    snake.dy=0
    snake.radius=0
snake = Snake()
food=Food()
running = True
score=0
d = 3


FPS = 30


clock = pygame.time.Clock()

while running:
        mill = clock.tick(FPS) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    running = False 
                if event.key == pygame.K_RIGHT: 
                    snake.dx = d 
                    snake.dy = 0 
                if event.key == pygame.K_LEFT: 
                    snake.dx = -d 
                    snake.dy = 0 
                if event.key == pygame.K_UP: 
                    snake.dx = 0 
                    snake.dy = -d 
                if event.key == pygame.K_DOWN: 
                    snake.dx = 0 
                    snake.dy = d 
        if border() or Suicide():
            the_end()
            backgroundimage=endImage
        screen.blit(backgroundimage, (0, 0))  

        snake.move()
        Collision()
        food.draw()
        snake.draw()
        Scores()
        
        pygame.display.flip()