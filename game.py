import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 50)  # Define a font for displaying the score

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize game variables
snake = [(5, 5)]
apple = (10, 10)
direction = (1, 0)
next_direction = (1, 0)
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input for direction change
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1):
        next_direction = (0, -1)
    elif keys[pygame.K_DOWN] and direction != (0, -1):
        next_direction = (0, 1)
    elif keys[pygame.K_LEFT] and direction != (1, 0):
        next_direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and direction != (-1, 0):
        next_direction = (1, 0)

    # Update snake position
    direction = next_direction
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)

    # Check if snake ate the apple
    if snake[0] == apple:
        apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        score += 10  # Increase the score
    else:
        snake.pop()

    # Draw everything
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, WHITE, pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(apple[0] * GRID_SIZE, apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Display the score on the screen
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Game over condition
    if (
        head[0] < 0
        or head[0] >= GRID_WIDTH
        or head[1] < 0
        or head[1] >= GRID_HEIGHT
        or head in snake[1:]
    ):
        running = False

    # Add a delay to control the game's speed
    tim = int(100 - score/5)
    pygame.time.delay(tim)
    
print("Your score was:", score)
pygame.quit()
sys.exit()
