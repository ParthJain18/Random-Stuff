import pygame
pygame.init()

screen=pygame.display.set_mode((900,500))
pygame.display.set_caption('IDK')
pygame.display.set_icon(pygame.image.load('Assets/ufo.png'))

playerX=100
playerY=400
player_changeX=0

def player(x,y):
    screen.blit('Assets/player.png',(x,y))


def main():
    running=True
    screen.fill((100,100,200))
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        
             

        player(playerX,playerY)
        pygame.display.update()
    pygame.quit()
    
if __name__=='__main__':
    main()