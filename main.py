import pygame

from pygame.locals import(
    K_RSHIFT,
    K_LSHIFT
)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 2)

while running:
    #check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill screen with purple to wipe away last frame

    screen.fill(color=(168, 229, 24))

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RSHIFT]:
        player_pos.x += 300 * dt
    if keys[pygame.K_LSHIFT]:
        player_pos.x -= 300 * dt


    #Rendering:

    #flip() puts work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 #limits FPS to 60

pygame.quit()