import pygame
import random

# pygame setup
pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True


def generate_starting_position():
    position_range = (pixel_width // 2, screen_width - pixel_width // 2, pixel_width)
    return [random.randrange(*position_range), random.randrange(*position_range)]


def reset():
    target.center = generate_starting_position()
    snake_pixel.center = generate_starting_position()
    return snake_pixel.copy()

def isOutOfBounds():
    return snake_pixel.bottom > screen_width or snake_pixel.top < 0 or snake_pixel.left < 0 or snake_pixel.right > screen_width

#playground
pixel_width = 50

#snake
snake_pixel = pygame.rect.Rect([0, 0, pixel_width, pixel_width])
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]
snake_direction = (0, 0)
snake_length = 1

#target
target = pygame.rect.Rect([0, 0, pixel_width, pixel_width])
target.center = generate_starting_position()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #fill screen with a color to wipe anything on last frame
    screen.fill("black")

    #keybinds
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        snake_direction = (0, - pixel_width)
    if keys[pygame.K_s]:
        snake_direction = (0, pixel_width)
    if keys[pygame.K_a]:
        snake_direction = (- pixel_width, 0)
    if keys[pygame.K_d]:
        snake_direction = (pixel_width, 0)

    snake_pixel.move_ip(snake_direction)

    #RENDER YOUR GAME
    
    if isOutOfBounds():
        snake_length = 1
        snake = reset()

    if snake_pixel.center == target.center:
        target.center = generate_starting_position()
        snake_length += 1
        snake.append(snake_pixel.copy())

    
    pygame.draw.rect(screen, "purple", snake_pixel)
    
    pygame.draw.rect(screen, "red", target)

    snake_pixel.move_ip(snake_direction)
    snake.append(snake_pixel.copy())
    snake = snake[-snake_length:]


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(5)  #limits FPS

pygame.quit()