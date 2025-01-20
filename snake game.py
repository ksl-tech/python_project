import pygame
import sys
import random

def draw_grid(surface, cell_size, width, height):
    for x in range(0, width, cell_size):
        pygame.draw.line(surface, (50, 50, 50), (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(surface, (50, 50, 50), (0, y), (width, y))

def show_message(screen, text, size, color, position):
    font = pygame.font.Font(None, size)
    message = font.render(text, True, color)
    rect = message.get_rect(center=position)
    screen.blit(message, rect)

def main():
    pygame.init()

    # Screen dimensions and colors
    WIDTH, HEIGHT = 600, 400
    CELL_SIZE = 20
    BG_COLOR = (200, 200, 200)  # Light gray background
    SNAKE_COLOR = (0, 128, 0)
    FOOD_COLOR = (255, 0, 0)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()

    def start_screen():
        screen.fill(BG_COLOR)
        show_message(screen, "Snake Game", 50, (0, 0, 0), (WIDTH // 2, HEIGHT // 2 - 50))
        show_message(screen, "Press SPACE to Start", 30, (0, 0, 0), (WIDTH // 2, HEIGHT // 2 + 20))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False

    def game_over_screen():
        screen.fill(BG_COLOR)
        show_message(screen, "Game Over", 50, (255, 0, 0), (WIDTH // 2, HEIGHT // 2 - 50))
        show_message(screen, "Press R to Restart or Q to Quit", 30, (0, 0, 0), (WIDTH // 2, HEIGHT // 2 + 20))
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return True
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
        return False

    start_screen()

    while True:
        # Initial snake setup
        snake = [(100, 100), (80, 100), (60, 100)]
        direction = (CELL_SIZE, 0)
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        score = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                        direction = (0, -CELL_SIZE)
                    if event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                        direction = (0, CELL_SIZE)
                    if event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                        direction = (-CELL_SIZE, 0)
                    if event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                        direction = (CELL_SIZE, 0)

            # Move snake
            new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            # Check for collisions
            if (
                new_head[0] < 0 or new_head[0] >= WIDTH or
                new_head[1] < 0 or new_head[1] >= HEIGHT or
                new_head in snake
            ):
                running = False

            # Check if the snake eats food
            if new_head == food:
                score += 1
                food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
            else:
                snake.pop()  # Remove the tail if no food eaten

            snake.insert(0, new_head)

            # Drawing everything
            screen.fill(BG_COLOR)
            draw_grid(screen, CELL_SIZE, WIDTH, HEIGHT)
            for segment in snake:
                pygame.draw.rect(screen, SNAKE_COLOR, (*segment, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, FOOD_COLOR, (*food, CELL_SIZE, CELL_SIZE))
            pygame.display.flip()

            clock.tick(10)

        if not game_over_screen():
            break

if __name__ == "__main__":
    main()
