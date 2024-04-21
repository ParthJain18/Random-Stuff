import pygame
import math
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # creating a window

FPS = 60

pygame.display.set_caption('Parth vs Dhruv')


def draw_win():   # to organize we can create different funcs to clear main func
    screen.fill((100, 100, 200))  # the tupple represents rgb colors
    # pygame.display.update() # We need to update the display to see the changes
    pygame.display.set_icon(pygame.image.load('Assets/ufo.png'))
    






# player
player_img = pygame.image.load('Assets/player.png')
player_2_img = pygame.transform.flip(pygame.image.load('Assets/player.png'), True, True)
playerX = 450
playerY = 340
playerX_change = 0
playerY_change = 0
player2X = 700
player2Y = 340
player2X_change = 0
player2Y_change = 0
#bullet
bulletX = 400
bullet2X = 400
bulletY = 0
bullet2Y = 0
bulletX_change = 0
bullet2X_change = 0
bullet_shoot = False
bullet2_shoot = False
#score
score1 = 0
score2 = 0



def player(x, y):
    screen.blit(player_img, (x, y))


def player2(a, b):
    screen.blit(player_2_img, (a, b))


def bullet_p1(x1, y1):
    screen.blit(pygame.image.load('Assets/bullet.png'), (x1+16, y1+10))


def bullet_p2(x2, y2):
    screen.blit(pygame.image.load('Assets/bullet2.png'), (x2-16, y2+10))


def collision(dist1, dist2, dist3, dist4):
    if math.sqrt(((dist1-dist2)**2) + ((dist3-dist4)**2)) < 32:
        return True
    else:
        return False


def score(x,y):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text1 = font.render(('Score : '+str(score1) ),True,(255,255,255))
    screen.blit(text1,(x,y))
    text1 = font.render(('Score : '+str(score2) ),True,(255,255,255))
    screen.blit(text1,(665-x,y))

clock = pygame.time.Clock()

run = True
while run:  # loop for keeping the program running
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # quit event is when we close the window
            run = False
        # all the events should be in the game loop(while)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                playerY_change = 5
            elif event.key == pygame.K_w:
                playerY_change = -5
            elif event.key == pygame.K_d:
                playerX_change = 5
            elif event.key == pygame.K_a:
                playerX_change = -5
            if bullet_shoot == False:
                if event.key == pygame.K_SPACE:
                    bulletX = playerX
                    bulletY = playerY
                    bullet_p1(bulletX, playerY)
                    bullet_shoot = True

        if event.type == pygame.KEYUP:
            if event.key == (pygame.K_a):
                playerX_change = 0
            if event.key == (pygame.K_w):
                playerY_change = 0
            if event.key == (pygame.K_d):
                playerX_change = 0
            if event.key == (pygame.K_s):
                playerY_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player2Y_change = 5
            elif event.key == pygame.K_UP:
                player2Y_change = -5
            elif event.key == pygame.K_RIGHT:
                player2X_change = 5
            elif event.key == pygame.K_LEFT:
                player2X_change = -5
            if bullet2_shoot == False:
                if event.key == pygame.K_KP_ENTER:
                    bullet2X = player2X
                    bullet2Y = player2Y
                    bullet_p2(bullet2X, player2Y)
                    bullet2_shoot = True
        if event.type == pygame.KEYUP:
            if event.key == (pygame.K_LEFT):
                player2X_change = 0
            if event.key == (pygame.K_UP):
                player2Y_change = 0
            if event.key == (pygame.K_RIGHT):
                player2X_change = 0
            if event.key == (pygame.K_DOWN):
                player2Y_change = 0

    if 0 >= playerX:
        playerX = 1
    elif 190 <= playerX:
        playerX = 189.9
    elif 0 >= playerY:
        playerY = 0
    elif 536 <= playerY:
        playerY = 535

    if 550 >= player2X:
        player2X = 551
    elif 736 <= player2X:
        player2X = 735.9
    elif 0 >= player2Y:
        player2Y = 0
    elif 536 <= player2Y:
        player2Y = 535

    draw_win()

    screen.blit(pygame.image.load('Assets/background.png'), (0, 0))

    playerY += playerY_change
    playerX += playerX_change
    player2X += player2X_change
    player2Y += player2Y_change
    bulletX += bulletX_change
    bullet2X += bullet2X_change

    player2(player2X, player2Y)
    player(playerX, playerY)
    if bulletX >= 800:
        bulletX = 0
        bullet_shoot = False

    if bullet_shoot == True:
        bulletX_change = 20
        bullet_p1(bulletX, bulletY)

    if bullet2X <= 0:
        bullet2X = 800
        bullet2_shoot = False

    if bullet2_shoot == True:
        bullet2X_change = -20
        bullet_p2(bullet2X, bullet2Y)

    if collision(player2X, bulletX, player2Y, bulletY) == True:
        bulletX = 0
        bulletY =700
        bullet_shoot = False
        score1 += 1
    if collision(playerX, bullet2X, playerY, bullet2Y) == True:
        bullet2X = 800
        bullet2Y = 700
        bullet2_shoot = False
        score2 += 1

    if score2 == 3:
        screen.blit(pygame.image.load('Assets/dhruvwon.png'), (25, 200))
        bullet2X=800
        if event.type == pygame.KEYDOWN:
            pygame.quit()

    if score1 == 3:
        screen.blit(pygame.image.load('Assets/parthwon.png'), (25, 200))
        bulletX=0
        if event.type == pygame.KEYDOWN:
            pygame.quit()

    score(10,10)

    pygame.display.update()
pygame.quit()



