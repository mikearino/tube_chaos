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
shore = pygame.image.load("assets/images/shore.png")
water = pygame.image.load("assets/images/water.png")
flipped_shore = pygame.transform.flip(shore, True, False)
left_shore_pos_x = 208
right_shore_pos_x = left_shore_pos_x + 32 +800
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    #check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill screen with purple to wipe away last frame

    screen.fill(color=(168, 229, 24))
    
    #draw in shoreline columns left 
    for y in range(23):
        left_shore_pos_y = y * 32
        screen.blit(shore, (left_shore_pos_x, left_shore_pos_y))

    #right shore
    for y in range(23):
        right_shore_pos_y = y * 32
        screen.blit(flipped_shore, (right_shore_pos_x, right_shore_pos_y))

    for row in range(12): #vertical
        for col in range(1, 26): #horizontal (water columns)
            result_x = left_shore_pos_x + col * 32
            result_y = row * 64
            screen.blit(water, (result_x, result_y))


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