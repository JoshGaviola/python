import pygame

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the snake
SNAKE_COLOR = (0, 255, 0)  # Green
SNAKE_SIZE = 20
snake_position = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]  # Center of the screen

# Set up the initial direction of the snake
snake_direction = 'right'

# Set up the snake movement speed
SNAKE_SPEED = 5

# Create a clock object
clock = pygame.time.Clock()

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_direction = 'left'
            elif event.key == pygame.K_RIGHT:
                snake_direction = 'right'
            elif event.key == pygame.K_UP:
                snake_direction = 'up'
            elif event.key == pygame.K_DOWN:
                snake_direction = 'down'

    # Move the snake
    if snake_direction == 'left':
        snake_position[0] -= SNAKE_SPEED
    elif snake_direction == 'right':
        snake_position[0] += SNAKE_SPEED
    elif snake_direction == 'up':
        snake_position[1] -= SNAKE_SPEED
    elif snake_direction == 'down':
        snake_position[1] += SNAKE_SPEED

    # Draw the snake
    pygame.draw.rect(screen, SNAKE_COLOR, (snake_position[0], snake_position[1], SNAKE_SIZE, SNAKE_SIZE))

    # Update the screen
    pygame.display.flip()

    # Control the game speed
    clock.tick(30)

# Quit Pygame
pygame.quit()
