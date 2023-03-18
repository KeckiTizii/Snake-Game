import pygame
import random

 
pygame.init()
 

# Các màu
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
gray = (37, 38, 33)


window_width = 800
window_height = 600
 
gameDisplay = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption('Snake game')

over = pygame.image.load("assets/evaporate-disappear.gif").convert()
over = pygame.transform.scale(over, (800, 600))
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont(None, 30)
 
def display_score(score):
    message = font_style.render("Score: "+str(score), True, white)
    gameDisplay.blit(message, (0, 0))


def our_snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(gameDisplay, white, [x[0], x[1], snake_block, snake_block])
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    gameDisplay.blit(mesg, [window_width/6, window_height/3])

def gameLoop():
    game_over = False
    game_close = False
 
    x1 = window_width / 2
    y1 = window_height / 2
 
    x1_change = 0       
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            gameDisplay.fill(gray)
            gameDisplay.blit(over, (0, 0))
            mesg = font_style.render("You Lost! Press Q To Quit Or C To Play Again", True, white)
            mesg_rect = mesg.get_rect(center=(window_width / 2, window_height / 4))
            gameDisplay.blit(mesg, mesg_rect)
            pygame.display.update()
             
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
            
        x1 += x1_change
        y1 += y1_change
        gameDisplay.fill(gray)
        pygame.draw.rect(gameDisplay, red, [foodx, foody, snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)

        display_score(Length_of_snake-1)

        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
gameLoop()
