import pygame

pygame.init()

# Create the window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wildlife Game")

# Load the images
background = pygame.image.load("background.jpg")
wildlife = pygame.image.load("animal.png")

# Scale the images
background = pygame.transform.scale(background, (800, 600))
wildlife = pygame.transform.scale(wildlife, (200, 200))

# Set positions
wildlife_x = 300
wildlife_y = 250

# Create the font
font = pygame.font.Font(None, 40)

# Create the text
text = font.render("Welcome to the Wildlife Game!", True, (255, 255, 255))

# Create the clock
clock = pygame.time.Clock()

# Game loop
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the wildlife image
    screen.blit(wildlife, (wildlife_x, wildlife_y))

    # Draw the text
    screen.blit(text, (150, 50))

    # Update the screen
    pygame.display.flip()

    # Keep the game at 60 FPS
    clock.tick(60)

pygame.quit()