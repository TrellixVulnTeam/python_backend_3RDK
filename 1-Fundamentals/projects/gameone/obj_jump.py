import pygame
pygame.init()
window = pygame.display.set_mode([850, 850])
pygame.display.set_caption("Jumping Tutorial")

x = 250
y = 250

width = 30
height = 30

velocity = 5
mass = 1

jumping = False

playing = True

while playing:
    window.fill([255, 255, 255])

    pygame.draw.rect(window, [255, 0, 0], [x, y, width, height])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if jumping == False:
        if keys[pygame.K_SPACE]:
            jumping = True

    if jumping:
        force = (1/2) * mass * (velocity**2)
        y -= force

        velocity = velocity - 1

        if y == 400:
            jumping = False
        if velocity < 0:
            mass =- 1
        if velocity == -6:
            jumping = False
            velocity = 5
            mass = 1

    pygame.time.delay(10)
    pygame.display.update()