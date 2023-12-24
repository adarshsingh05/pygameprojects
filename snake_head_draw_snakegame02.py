import pygame
pygame.init()
screen_width=1000
screen_height=600

# colors
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,255,0)

# setting title

pygame.display.set_caption("Snakes")
gameWindow=pygame.display.set_mode(( screen_width,screen_height))

pygame.display.update()

# defining variables

exit_game=False
game_over=False
snake_x=150
snake_y=100
l=20
w=20

# creating loop and handaling events

while not exit_game:
    for event in pygame.event.get():
        print(event)
    if event.type==pygame.QUIT:
        exit_game=True

    gameWindow.fill(white)

    # creating the head of the snake
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,l,w])
    pygame.display.update()


# quiting the game
pygame.quit()
quit()