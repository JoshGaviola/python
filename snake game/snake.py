import pygame

# Initialize Pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the snake
SNAKE_COLOR = (0, 255, 0)  # Green
snake_position = [320, 240]  # Center of the screen
SNAKE_SIZE = 20

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
            if event.key == pygame.K_LEFT and snake_direction != 'right':
                snake_direction = 'left'
            elif event.key == pygame.K_RIGHT and snake_direction != 'left':
                snake_direction = 'right'
            elif event.key == pygame.K_UP and snake_direction != 'down':
                snake_direction = 'up'
            elif event.key == pygame.K_DOWN and snake_direction != 'up':
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
