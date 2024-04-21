import pygame
from pygame.constants import KEYDOWN, KEYUP
pygame.init()
screen=pygame.display.set_mode((800,600))
surface1=pygame.Surface([800,600])
pygame.display.set_caption('PingPong')
pygame.display.set_icon(pygame.image.load('Assets/PingPong.png.png'))

run = True
speed_player=0
opponent_speed=0
x=3
y=3
diff=2.5

bar1=pygame.image.load('Assets/newbar.png')
bar_rect=bar1.get_rect(topleft=(10,300))
opponent=bar1.get_rect(topright=(790,300))

ball=pygame.image.load('Assets/pongball.png')
ball_rect=ball.get_rect(center=(400,300))

   
    

while run:
    pygame.time.Clock().tick(60)
    speed1=0

    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            run=False

        if event.type==KEYDOWN:
            if event.key==pygame.K_w:
                speed1 -= 5
            if event.key==pygame.K_s:
                speed1 += 5
        if event.type==KEYUP:
            if event.key==pygame.K_w:
                speed1 += 5
            if event.key==pygame.K_s:
                speed1 -= 5    
    
    screen.fill((255,255,255))
    

    if bar_rect.top<=0:
        bar_rect.top=0
    if bar_rect.bottom>=600:
        bar_rect.bottom=600    


    if ball_rect.bottom>=600:
        y-=(2*y)
    elif ball_rect.top<=0:
        y-=(2*y)

    if ball_rect.colliderect(bar_rect):
        x=-x
    if ball_rect.colliderect(opponent):
        x=-x

    

    ball_rect.x+=x
    ball_rect.y-=y
    if ball_rect.left>200:
        if ball_rect.bottom>=opponent.bottom:
            opponent_speed=diff
        if ball_rect.top<=opponent.top:
            opponent_speed=-diff
        opponent.y+=opponent_speed
    
    speed_player += speed1
    bar_rect.top += speed_player

    screen.blit(bar1,bar_rect)
    screen.blit(bar1,opponent)
    screen.blit(ball,ball_rect)
    
    
  

    
    

    pygame.display.flip()
pygame.quit()