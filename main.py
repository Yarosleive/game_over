import pygame

pygame.init()
pygame.display.set_caption('Герой двигается')
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
sprite = pygame.sprite.Sprite()
sprite = pygame.image.load('data/gameover.png')
screen.fill((0, 0, 255))
running = True
clock = pygame.time.Clock()
sprite_rect = sprite.get_rect()
sprite_rect_x = -width
sprite_rect_y = 0
move = True
pygame.transform.scale(sprite, (width, height))
v = 200
right = True
while running:
    screen.fill((0, 0, 255))
    screen.blit(sprite, (sprite_rect_x, sprite_rect_y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if sprite_rect_x + width >= width and move:
        move = False
    if sprite_rect_x + width < width and move:
        sprite_rect_x += v * clock.tick() / 1000
    pygame.display.flip()
pygame.quit()