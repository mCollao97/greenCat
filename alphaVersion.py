import sys, pygame, random
pygame.init()

width, height   = 800, 600
resolucion      = width, height
pantalla        = pygame.display.set_mode(resolucion)

pygame.display.set_caption("Gravity")


speedBall1      = [1, 1]
speedBall2      = [1, 1]
speedBall3      = [1, 1]
white           = 112, 128, 144

ball            = pygame.image.load("ball.png")
ball            = pygame.transform.scale(ball, (100, 100))
ballrect        = ball.get_rect()

enemyBall       = pygame.image.load("ball.png")
enemyBall       = pygame.transform.scale(enemyBall, (150, 150))

enemyrect       = enemyBall.get_rect()

enemyBall2      = pygame.image.load("ball.png")
enemyBall2      = pygame.transform.scale(enemyBall2, (150, 150))

enemyrect2      = enemyBall2.get_rect()

enemyBall3      = pygame.image.load("ball.png")
enemyBall3      = pygame.transform.scale(enemyBall3, (150, 150))

enemyrect3      = enemyBall3.get_rect()

enemyrect.move_ip(100,100)
enemyrect2.move_ip(200,200)
enemyrect3.move_ip(300,300)

run             = True

while run:
    pygame.time.delay(0)
    pygame.key.set_repeat(3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballrect = ballrect.move(-2,0)
            if event.key == pygame.K_RIGHT:
                ballrect = ballrect.move(2,0)
            if event.key == pygame.K_UP:
                ballrect = ballrect.move(0,-2)
            if event.key == pygame.K_DOWN:
                ballrect = ballrect.move(0,2)

        enemyrect   = enemyrect.move(speedBall1)
        enemyrect2  = enemyrect2.move(speedBall2)
        enemyrect3  = enemyrect3.move(speedBall3)
        if enemyrect.left < 0 or enemyrect.right >= width:
            speedBall1[0] = -(speedBall1[0])
        elif enemyrect.top < 0 or enemyrect.bottom > height:
            speedBall1[1] = -(speedBall1[1])

        if enemyrect2.left < 0 or enemyrect2.right >= width:
            speedBall2[0] = -(speedBall2[0])
        elif enemyrect2.top < 0 or enemyrect2.bottom > height:
            speedBall2[1] = -(speedBall2[1])

        if enemyrect3.left < 0 or enemyrect3.right >= width:
            speedBall3[0] = -(speedBall3[0])
        elif enemyrect3.top < 0 or enemyrect3.bottom > height:
            speedBall3[1] = -(speedBall3[1])

    pantalla.fill(white)

    pantalla.blit(ball, ballrect)

    pantalla.blit(enemyBall, enemyrect)
    pantalla.blit(enemyBall2, enemyrect2)
    pantalla.blit(enemyBall3, enemyrect3)

    pygame.display.update()
pygame.quit()
