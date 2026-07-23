import pygame 
pygame.init()

screen = pygame.display.set_mode((400,500))

done = False

while not done :
    for event in pygame.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.flip()
    