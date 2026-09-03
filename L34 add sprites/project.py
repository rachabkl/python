import pygame

pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sprite Game")

clock = pygame.time.Clock()


# Create a Sprite class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Create the image
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 100, 255))

        # Create the Rect
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)

        # Create velocity
        self.velocity = pygame.Vector2(3, 0)

    # Update the sprite
    def update(self):
        self.rect.x += self.velocity.x

        # Keep the sprite on the screen
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.velocity.x *= -1


# Create the sprite
player = Player()

# Create a sprite group
sprites = pygame.sprite.Group()
sprites.add(player)


# Create a custom event
MOVE_EVENT = pygame.USEREVENT + 1

# Post the event every 2 seconds
pygame.time.set_timer(MOVE_EVENT, 2000)


# Main game loop
running = True

while running:

    for event in pygame.event.get():

        # Close the game
        if event.type == pygame.QUIT:
            running = False

        # Handle the custom event
        if event.type == MOVE_EVENT:
            print("Custom event!")

            # Change the direction
            player.velocity.x *= -1

    # Update the sprites
    sprites.update()

    # Draw everything
    screen.fill((255, 255, 255))
    sprites.draw(screen)

    # Update the screen
    pygame.display.flip()

    # 60 FPS
    clock.tick(60)

pygame.quit()