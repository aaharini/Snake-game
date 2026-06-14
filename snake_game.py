import pygame
import time
import random

soft_blue = "#A6D8FF"
green = "#45AE55"
dark_blue = "#343E98"
red = "#FF5151"
white = "#F1F1F1"
black = "#000000"

pygame.init()   ## initializing environment

box_len = 900       ## game screen length
box_height = 600    ## game screen height

caption = pygame.display.set_mode((box_len, box_height))
pygame.display.set_caption("SNAKE GAME")      ## in the box add title to display

timer = pygame.time.Clock() ## time for appearing next food

snake_block = 10 ## size of the snake after eating one food
snake_speed = 10 ## speed of the snake

## Font initialization 
display_style= pygame.font.SysFont("arial",30,"bold")
score_font = pygame.font.SysFont("arial",50,"bold")

## score increcing function
def final_score(score):
    value = score_font.render("Enjoy The Game.  Your score is: "+ str(score),True,dark_blue)
    caption.blit(value,[0,0])

## For making snake
def make_snake(snake_block,list_snake):
    for x in list_snake:
        pygame.draw.rect(caption,green, [x[0], x[1], snake_block,snake_block])

## disply after game over
def display_msg (msg, color):
    mssg = display_style.render(msg, True, color)
    caption.blit(mssg, [box_len/6, box_height/3])         

def game_start():
    game_over = False
    game_close = False

    value_x1 = box_len/2
    value_y1 = box_height/2

    new_x1 = 0
    new_y1 = 0

    list_snake = []
    snake_len = 1

    foodx_pos = round(random.randrange(0, box_len-snake_block) /10.0)* 10.0
    foody_pos = round(random.randrange(0, box_height-snake_block)/10.0)* 10.0

    while not game_over:
    
        while game_close == True:
            caption.fill(soft_blue)
            display_msg("You Lost! Want To Play Again Press C or Else Press Q", black)
            final_score(snake_len-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_start()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_x1 = -snake_block
                    new_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    new_x1 = snake_block
                    new_y1 = 0
                elif event.key == pygame.K_UP:
                    new_y1 = -snake_block
                    new_x1 = 0  
                elif event.key == pygame.K_DOWN:
                    new_y1 = snake_block
                    new_x1 = 0      

        if value_x1>=box_len or value_x1<0 or value_y1>=box_height or value_y1<0:              
            game_close =True            

        ## to update score            
        value_x1 = value_x1+new_x1
        value_y1 = value_y1+new_y1
        caption.fill(soft_blue)
        pygame.draw.rect(caption,red, [foodx_pos,foody_pos,snake_block,snake_block])
        snake_head =[]
        snake_head.append(value_x1)
        snake_head.append(value_y1)
        list_snake.append(snake_head)
        if len(list_snake) > snake_len:
            del list_snake[0]

        for x in list_snake [:-1]:
            if x==snake_head:
                game_close = True

        make_snake(snake_block,list_snake)
        final_score(snake_len-1)            
        
        pygame.display.update()

        if value_x1 == foodx_pos and value_y1 == foody_pos:
            foodx_pos = round(random.randrange(0,box_len-snake_block)/10.0)*10.0
            foody_pos = round(random.randrange(0,box_height-snake_block)/10.0)*10.0
            snake_len = snake_len+1
        timer.tick(snake_speed)

    pygame.quit()
    quit()

game_start()
