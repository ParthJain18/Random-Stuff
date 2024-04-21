import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake')

snake_block=pygame.image.load('Assets/green_square.png')
snake_rect=snake_block.get_rect(topleft=(20,20))

run=True
direction=0

class snake:
    def lenght():
        pass
    def movement():
        pass

while run:
    pygame.time.Clock().tick(3)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    


    screen.fill((100,100,200))
    direction += 20
    snake_rect.top = direction

    screen.blit(snake_block, snake_rect)
    pygame.display.update()


pygame.quit()