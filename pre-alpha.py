import pygame, random, sys, time
from pygame.locals import *
pygame.init()

width, height   =   800, 600
resolution      =   width, height
screen          =   pygame.display.set_mode(resolution)

pygame.display.set_caption("------- PRE ALPHA VERSION 0.1 -------")

lifeAux = 50

backgroundImage = pygame.image.load("backgroundImg.png")

lifeBar         =   pygame.image.load("lifeBar.png")
lifeBar         =   pygame.transform.scale(lifeBar,(lifeAux,10))
lifeBaRect      =   lifeBar.get_rect()

sprite          =   pygame.image.load("smallSize.png")
sprite          =   pygame.transform.scale(sprite, (100, 100))
spriteRect      =   sprite.get_rect()

spriteRect.move_ip((width/2), (height-100))
spriteLife      =   1000

enemy           =   pygame.image.load("smallEnemy.png")
enemy           =   pygame.transform.scale(enemy, (130,130))
enemyrect       =   enemy.get_rect()

centerBullet    =   spriteRect.left+50
alignBullet     =   spriteRect.bottom

varAux          =   random.randint(20,width)
enemyrect.move_ip(varAux, 0)
lifeBaRect.move_ip(spriteRect.left-10,spriteRect.top+10)

bullet          =   pygame.image.load("bullet.png")
bulletrect      =   bullet.get_rect()

bulletrect.move_ip(centerBullet,alignBullet)
bulletSpeed     =   -25
shooting        = False

run             =   True
varAux          =   0

while run:

    enemyrect = enemyrect.move(0,1)

    pygame.time.delay(4)
    pygame.key.set_repeat(3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spriteRect = spriteRect.move(-3,0)
                lifeBaRect = lifeBaRect.move(-3,0)
                bulletrect = bulletrect.move(-3,0)
            if event.key == pygame.K_RIGHT:
                spriteRect = spriteRect.move(3,0)
                lifeBaRect = lifeBaRect.move(3,0)
                bulletrect = bulletrect.move(3,0)
            if event.key == pygame.K_UP:
                spriteRect = spriteRect.move(0,-3)
                lifeBaRect = lifeBaRect.move(0,-3)
                bulletrect = bulletrect.move(0,-3)
            if event.key == pygame.K_DOWN:
                spriteRect = spriteRect.move(0,3)
                lifeBaRect = lifeBaRect.move(0,3)
                bulletrect = bulletrect.move(0,3)
            if event.key == pygame.K_SPACE:
                shooting = True

    if spriteRect.colliderect(enemyrect):

        enemyrect.move_ip(-enemyrect.left, 0)
        varAux = random.randint(20,width)
        enemyrect.move_ip(varAux,-spriteRect.top)
        lifeBar = pygame.transform.scale(lifeBar,((lifeAux-10),10))
        lifeAux -= 9

        if spriteLife > 0:
            spriteLife -= 200
        else:
            run = False

    if bulletrect.colliderect(enemyrect):
        enemyrect.move_ip(-enemyrect.left, 0)
        varAux = random.randint(20,width)
        enemyrect.move_ip(varAux,-spriteRect.top)

    if enemyrect.top > height:
        enemyrect.move_ip(-enemyrect.left, 0)
        varAux = random.randint(20,width)
        enemyrect.move_ip(varAux,-600)
        screen.blit(enemy,enemyrect)


    screen.blit(backgroundImage,(0,0))
    screen.blit(sprite, spriteRect)
    screen.blit(enemy,enemyrect)
    screen.blit(lifeBar, lifeBaRect)

    if shooting:
        screen.blit(bullet, bulletrect)
        bulletrect  =   bulletrect.move(0,bulletSpeed)
    if bulletrect.bottom < 0:
        shooting = False
        bulletrect = bulletrect.move(0,0)
        bulletrect.move_ip(-abs(bulletrect.left-spriteRect.left)+50,spriteRect.bottom)

    pygame.display.flip()

pygame.quit()
