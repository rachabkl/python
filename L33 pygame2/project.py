import pygame

pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Sprite")

clock = pygame.time.Clock()

# Sprite position
x = 375
y = 275

# Sprite size
width = 50
height = 50

# Game loop
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which keys are pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 5

    if keys[pygame.K_RIGHT]:
        x += 5

    if keys[pygame.K_UP]:
        y -= 5

    if keys[pygame.K_DOWN]:
        y += 5

    # Keep the sprite inside the screen
    x = max(0, min(x, 800 - width))
    y = max(0, min(y, 600 - height))

    # Change color based on position
    if x < 250:
        color = (255, 0, 0)
    elif x < 550:
        color = (0, 255, 0)
    else:
        color = (0, 0, 255)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the rectangle
    pygame.draw.rect(screen, color, (x, y, width, height))

    # Draw an outlined rectangle
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), 3)

    # Update the screen
    pygame.display.flip()

    # 60 frames per second
    clock.tick(60)

pygame.quit()