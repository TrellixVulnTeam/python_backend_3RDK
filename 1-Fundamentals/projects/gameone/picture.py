import pygame
pygame.init()
window = pygame.display.set_mode([490, 390])

image = pygame.image.load(r"C:\Users\jycmi\Documents\Devlopment\3.Nucamp\NucampFolder\Python\1-Fundamentals\projects\gameone\Images\lolcat-programmer.jpg")

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    window.fill((0, 0, 0))
    window.blit(image, (0, 0))
    pygame.display.update()

pygame.quit()