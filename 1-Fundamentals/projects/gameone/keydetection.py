import pygame
pygame.init()
window = pygame.display.set_mode([450, 450])

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
    if event.type in (pygame.KEYDOWN, pygame.KEYUP):
        key_name = pygame.key.name(event.key)
        key_name = key_name.upper()
        if event.type == pygame.KEYDOWN:
            print(f'{key_name}Key Pressed:\n')
        elif event.type == pygame.KEYUP:
            print(f'{key_name} Key Released:\n')

pygame.quit()