import sys, pygame

#INICIALIZAR PYGAME, SETEAR TAMAÑO VENTANA, L5 Y L6
pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego chelo")

width, height = 800, 600
speed  = [0,0]
white  = 255, 255, 255

ball            = pygame.image.load("ball.png")
ball            = pygame.transform.scale(ball, (100, 100))
rectanguloCapa  = ball.get_rect()
plataforma      = pygame.image.load("ball.png")
#plataforma      = pygame.transform.scale(plataforma, (300, 300))
plataformaRect  = plataforma.get_rect()
# bucle juego iniciado
run = True
while run:
    pygame.time.delay(4)
    pygame.key.set_repeat(3)
    movingRight = True
    if rectanguloCapa.bottom < height:
        rectanguloCapa = rectanguloCapa.move(0,1)
    else:
        rectanguloCapa = rectanguloCapa.move(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rectanguloCapa = rectanguloCapa.move(-1,0)
            if event.key == pygame.K_RIGHT:
                rectanguloCapa = rectanguloCapa.move(1,0)
            if event.key == pygame.K_UP:
                rectanguloCapa = rectanguloCapa.move(0,-1)
                if movingRight and rectanguloCapa.bottom > height:
                    speed[0] = 1
                else:
                    speed[0] = 0
            if event.key == pygame.K_DOWN:
                rectanguloCapa = rectanguloCapa.move(0,1)
#    if plataformaRect.colliderect(plataformaRect):
#        speed[0] = - speed[0]

    screen.fill(white)
    screen.blit(ball, rectanguloCapa)
    pygame.display.update()
pygame.quit()
