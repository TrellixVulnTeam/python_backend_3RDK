import pygame
pygame.init()
window = pygame.display.set_mode([850, 850])
pygame.display.set_caption("Drawing Shapes")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


window.fill(white)

pygame.draw.polygon(window, black, [(146, 0), (291, 106), (236, 277), (56, 277), (0,106)])
pygame.draw.line(window, green, (65, 350), (120, 350), 4)
pygame.draw.circle(window, red, (550, 550), 100, 4)
pygame.draw.ellipse(window, blue, (300, 250, 200, 100), 4)
pygame.draw.rect(window, black, (150, 300, 100, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()