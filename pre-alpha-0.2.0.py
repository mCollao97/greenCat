import pygame, sys, random

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('###### PRE_ALPHA 0.2 ######')
width, height   =   800, 600
screen  = pygame.display.set_mode((width, height),0,32)

backgroundImage = pygame.image.load("backgroundImg.png")

font    = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu():
    click    = False
    while True:

        screen.blit(backgroundImage,(0,0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        playButton      =   pygame.image.load("play.png")
        playButton      =   pygame.transform.scale(playButton, (350, 120))
        button_1        =   playButton.get_rect()
        button_1.move_ip(230,150)
        quitButton      =   pygame.image.load("quit.png")
        quitButton      =   pygame.transform.scale(quitButton, (350, 120))
        button_2        =   quitButton.get_rect()
        button_2.move_ip(230,350)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
        screen.blit(playButton,button_1)
        screen.blit(quitButton, button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)
def game():
    #VARIABLE NAME TALKS BY ITSELF

    lifeAux         = 50
    lifeBar         =   pygame.image.load("lifeBar.png")
    lifeBar         =   pygame.transform.scale(lifeBar,(lifeAux,10))
    lifeBaRect      =   lifeBar.get_rect()

    #PRINCIPAL SPRITE
    sprite          =   pygame.image.load("smallSize.png")
    sprite          =   pygame.transform.scale(sprite, (100, 100))
    spriteRect      =   sprite.get_rect()

    #SET POSITION OF THE MAIN CHARACTER
    spriteRect.move_ip((width/2), (height-100))
    spriteLife      =   1000

    #VARIABLE NAME TALKS BY ITSELF
    enemy           =   pygame.image.load("smallEnemy.png")
    enemy           =   pygame.transform.scale(enemy, (130,130))
    enemyrect       =   enemy.get_rect()

    #ALIGN BULLET TO POSITION OF MAIN CHARACTER
    centerBullet    =   spriteRect.left+50
    alignBullet     =   spriteRect.bottom

    #AUXILIAR VARIABLE USED TO RANDOMIZE ENEMY POSITION ONCE HE KILL US, WE KILL HIM OR WE CRASH
    varAux          =   random.randint(20,width)
    enemyrect.move_ip(varAux, 0)
    lifeBaRect.move_ip(spriteRect.left-10,spriteRect.top+10)

    bullet          =   pygame.image.load("bullet.png")
    bulletrect      =   bullet.get_rect()

    bulletrect.move_ip(centerBullet,alignBullet)
    bulletSpeed     =   -25
    shooting        = False

    varAux          =   0
    running = True
    while running:
        enemyrect = enemyrect.move(0,1)

        pygame.time.delay(4)
        pygame.key.set_repeat(3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False
            elif event.type == pygame.KEYDOWN:
                #SHOOT AND MOVING
                if event.key == pygame.K_LEFT and event.key == pygame.K_SPACE:
                    spriteRect  = spriteRect.move(-3,0)
                    lifeBaRect  = lifeBaRect.move(-3,0)
                    bulletrect  = bulletrect.move(-3,0)
                    shooting    = True
                #ONLY MOVING
                if event.key == pygame.K_LEFT:
                    spriteRect  = spriteRect.move(-3,0)
                    lifeBaRect  = lifeBaRect.move(-3,0)
                    bulletrect  = bulletrect.move(-3,0)
                if event.key == pygame.K_RIGHT and event.key == pygame.K_SPACE:
                    spriteRect  = spriteRect.move(3,0)
                    lifeBaRect  = lifeBaRect.move(3,0)
                    bulletrect  = bulletrect.move(3,0)
                    shooting    =   True
                if event.key == pygame.K_RIGHT:
                    spriteRect  = spriteRect.move(3,0)
                    lifeBaRect  = lifeBaRect.move(3,0)
                    bulletrect  = bulletrect.move(3,0)
                if event.key == pygame.K_UP and event.key == pygame.K_SPACE:
                    spriteRect  = spriteRect.move(0,-3)
                    lifeBaRect  = lifeBaRect.move(0,-3)
                    bulletrect  = bulletrect.move(0,-3)
                    shooting    = True
                if event.key == pygame.K_UP:
                    spriteRect  = spriteRect.move(0,-3)
                    lifeBaRect  = lifeBaRect.move(0,-3)
                    bulletrect  = bulletrect.move(0,-3)
                if event.key == pygame.K_DOWN and event.key == pygame.K_SPACE:
                    spriteRect  = spriteRect.move(0,3)
                    lifeBaRect  = lifeBaRect.move(0,3)
                    bulletrect  = bulletrect.move(0,3)
                    shooting    = True
                if event.key == pygame.K_DOWN:
                    spriteRect  = spriteRect.move(0,3)
                    lifeBaRect  = lifeBaRect.move(0,3)
                    bulletrect  = bulletrect.move(0,3)
                if event.key == pygame.K_SPACE:
                    shooting = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

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
        mainClock.tick(0)
main_menu()
