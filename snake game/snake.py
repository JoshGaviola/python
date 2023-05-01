import random
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

# Set up the food
FOOD_COLOR = (255, 0, 0)  # Red
FOOD_SIZE = 20
food_position = [random.randint(
    0, SCREEN_WIDTH - FOOD_SIZE), random.randint(0, SCREEN_HEIGHT - FOOD_SIZE)]

# Set up the initial direction of the snake
snake_direction = 'right'

# Set up the snake movement speed
SNAKE_SPEED = 5

snake_length = 1

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

    # Move the snake's head
    if snake_direction == 'left':
        snake_position[0] -= SNAKE_SPEED
        if snake_position[0] < 0:  # If snake goes off the left side of the screen, wrap around to the right side
            snake_position[0] = SCREEN_WIDTH - SNAKE_SIZE
    elif snake_direction == 'right':
        snake_position[0] += SNAKE_SPEED
        if snake_position[0] > SCREEN_WIDTH - SNAKE_SIZE:  # If snake goes off the right side of the screen, wrap around to the left side
            snake_position[0] = 0
    elif snake_direction == 'up':
        snake_position[1] -= SNAKE_SPEED
        if snake_position[1] < 0:  # If snake goes off the top of the screen, wrap around to the bottom
            snake_position[1] = SCREEN_HEIGHT - SNAKE_SIZE
    elif snake_direction == 'down':
        snake_position[1] += SNAKE_SPEED
        if snake_position[1] > SCREEN_HEIGHT - SNAKE_SIZE:  # If snake goes off the bottom of the screen, wrap around to the top
            snake_position[1] = 0

    # Check if the snake has eaten the food
    if pygame.Rect(snake_position[0], snake_position[1], SNAKE_SIZE, SNAKE_SIZE).colliderect(pygame.Rect(food_position[0], food_position[1], FOOD_SIZE, FOOD_SIZE)):
        food_position = [random.randint(0, SCREEN_WIDTH - FOOD_SIZE), random.randint(0, SCREEN_HEIGHT - FOOD_SIZE)]
        snake_length += 1

    # Move the rest of the snake's body
    snake_positions = [snake_position.copy()]

    # Move the snake's head
    if snake_direction == 'left':
        snake_positions[0][0] -= SNAKE_SPEED
        if snake_positions[0][0] < 0:  # If snake goes off the left side of the screen, wrap around to the right side
            snake_positions[0][0] = SCREEN_WIDTH - SNAKE_SIZE
    elif snake_direction == 'right':
        snake_positions[0][0] += SNAKE_SPEED
        if snake_positions[0][0] > SCREEN_WIDTH - SNAKE_SIZE:  # If snake goes off the right side of the screen, wrap around to the left side
            snake_positions[0][0] = 0
    elif snake_direction == 'up':
        snake_positions[0][1] -= SNAKE_SPEED
        if snake_positions[0][1] < 0:  # If snake goes off the top of the screen, wrap around to the bottom
            snake_positions[0][1] = SCREEN_HEIGHT - SNAKE_SIZE
    elif snake_direction == 'down':
        snake_positions[0][1] += SNAKE_SPEED
        if snake_positions[0][1] > SCREEN_HEIGHT - SNAKE_SIZE:  # If snake goes off the bottom of the screen, wrap around to the top
            snake_positions[0][1] = 0

    # Move the rest of the snake's body
    for i in range(1, snake_length):
        if len(snake_positions) > i > 0:
            snake_positions[i], snake_positions[i-1] = snake_positions[i-1], snake_positions[i]


    # Draw the snake
    screen.fill((0, 0, 0))  # Clear the screen first
    for position in snake_positions:
        pygame.draw.rect(screen, SNAKE_COLOR,
                         (position[0], position[1], SNAKE_SIZE, SNAKE_SIZE))

    # Draw the food
    pygame.draw.rect(screen, FOOD_COLOR,
                     (food_position[0], food_position[1], FOOD_SIZE, FOOD_SIZE))

    # Update the screen
    pygame.display.flip()

    # Control the game speed
    clock.tick(30)

# Quit Pygame
pygame.quit()