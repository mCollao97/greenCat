import sys, pygame, random, time
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
ballrect.center
ballrect.size   = [40,40]


enemyBall       = pygame.image.load("ball.png")
enemyBall       = pygame.transform.scale(enemyBall, (100, 100))

enemyrect       = enemyBall.get_rect()
enemyrect.center
enemyrect.size  = [40,40]


enemyBall2      = pygame.image.load("ball.png")
enemyBall2      = pygame.transform.scale(enemyBall2, (100, 100))

enemyrect2      = enemyBall2.get_rect()
enemyrect2.center
enemyrect2.size  = [40,40]

enemyBall3      = pygame.image.load("ball.png")
enemyBall3      = pygame.transform.scale(enemyBall3, (100, 100))

enemyrect3      = enemyBall3.get_rect()
enemyrect3.center
enemyrect3.size  = [40,40]
enemyrect.move_ip(random.randint(10,700),random.randint(10,500))
enemyrect2.move_ip(random.randint(10,700),random.randint(10,500))
enemyrect3.move_ip(random.randint(10,700),random.randint(10,500))

run             = True

while run:
    pygame.time.delay(1)
    pygame.key.set_repeat(3)


    enemyrect   = enemyrect.move(speedBall1)
    enemyrect2  = enemyrect2.move(speedBall2)
    enemyrect3  = enemyrect3.move(speedBall3)

    if enemyrect.left <= -80 or enemyrect.right >= (width - 90):
        speedBall1[0] = -(speedBall1[0])
    elif enemyrect.top <= -80 or enemyrect.bottom >= (height - 90):
        speedBall1[1] = -(speedBall1[1])

    if enemyrect2.left <= 0 or enemyrect2.right >= width:
        speedBall2[0] = -(speedBall2[0])
    elif enemyrect2.top <= 0 or enemyrect2.bottom >= height:
        speedBall2[1] = -(speedBall2[1])
    if enemyrect3.left <= 0 or enemyrect3.right >= width:
        speedBall3[0] = -(speedBall3[0])
    elif enemyrect3.top <= 0 or enemyrect3.bottom >= height:
        speedBall3[1] = -(speedBall3[1])

    if ballrect.colliderect(enemyrect) or ballrect.colliderect(enemyrect2) or ballrect.colliderect(enemyrect3):
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballrect = ballrect.move(-3,0)
            if event.key == pygame.K_RIGHT:
                ballrect = ballrect.move(3,0)
            if event.key == pygame.K_UP:
                ballrect = ballrect.move(0,-3)
            if event.key == pygame.K_DOWN:
                ballrect = ballrect.move(0,3)

    pantalla.fill(white)

    pantalla.blit(ball, ballrect)

    pantalla.blit(enemyBall, enemyrect)
    pantalla.blit(enemyBall2, enemyrect2)
    pantalla.blit(enemyBall3, enemyrect3)

    pygame.display.flip()

    pygame.display.update(enemyrect)
    pygame.display.update(enemyrect2)
    pygame.display.update(enemyrect3)
pygame.quit()
