import pygame
pygame.init()
window = pygame.display.set_mode([490, 390])

font = pygame.font.Font('freesansbold.ttf', 32)

text = font.render('Hello World', True, (0, 255, 0), (0, 0, 128))
textRect = text.get_rect()
textRect.center = (490//2, 390//2)


playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    window.fill((255, 255, 255))
    window.blit(text, textRect)
    pygame.display.update()

pygame.quit()