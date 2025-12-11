import pygame

from pygame.locals import(
    K_RSHIFT,
    K_LSHIFT
)

pygame.init()
screen = pygame.display.set_mode(
    (1280, 720),
    pygame.SCALED | pygame.DOUBLEBUF,
    vsync=1
)

clock = pygame.time.Clock()
running = True
dt = 0
shore = pygame.image.load("assets/images/shore.png")
water = pygame.image.load("assets/images/water.png")
flipped_shore = pygame.transform.flip(shore, True, False)
left_shore_pos_x = 208
right_shore_pos_x = left_shore_pos_x + 32 +800
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
water_offset_y = 0
water_speed = 100

class Rock:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = image.get_rect(center=(x, y))

while running:
    #check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(color=(168, 229, 24))
    dt = clock.tick() / 1000 #limits FPS to 60

     #water tile movement
    water_offset_y += water_speed * dt
    water_offset_y = water_offset_y % 64

    #water tiles
    for row in range(13): #vertical
        for col in range(1, 26): #horizontal (water columns)
            result_x = left_shore_pos_x + col * 32
            result_y = row * 64 + water_offset_y - 64
            screen.blit(water, (result_x, int(result_y)))


    #draw in shoreline columns left 
    for y in range(23):
        left_shore_pos_y = y * 32
        screen.blit(shore, (left_shore_pos_x, left_shore_pos_y))

    #right shore
    for y in range(23):
        right_shore_pos_y = y * 32
        screen.blit(flipped_shore, (right_shore_pos_x, right_shore_pos_y))

    
    #draw raft
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RSHIFT]:
        player_pos.x += 300 * dt
    if keys[pygame.K_LSHIFT]:
        player_pos.x -= 300 * dt


    #Rendering:

    #flip() puts work on screen
    pygame.display.flip()


pygame.quit()