import pygame
import time
import random
import psycopg2

pygame.init()

# Database connection parameters
DB_PARAMS = {
    'dbname': 'snake',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432',
}

# Establishing a connection to the database
connection = psycopg2.connect(**DB_PARAMS)
cursor = connection.cursor()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display and game settings
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Font styles
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Define different types of food with different weights
foods = [(green, 0.6), (red, 0.3), (blue, 0.1)]

def your_score(score):
    """Display the user's current score on the screen."""
    value = score_font.render(f"Your Score: {score}", True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    """Draw the snake on the screen based on the provided snake list."""
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    """Display a message on the screen."""
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def generate_food():
    """Generate a random position for food."""
    food_type = random.choices(foods, weights=[w for _, w in foods])[0]
    food_color, _ = food_type
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    return foodx, foody, food_color

def save_game_state(user_id, current_score):
    """Save the current state and score of the game to the database."""
    cursor.execute(
        "INSERT INTO user_score (user_id, score) VALUES (%s, %s)",
        (user_id, current_score)
    )
    connection.commit()
    print(f"Game saved. Your score: {current_score}")

def get_user_data():
    """Prompt the user for a username and retrieve their data from the database."""
    username = input("Enter your username: ")

    # Query the database for the user's data
    cursor.execute("SELECT id, level FROM \"user\" WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user:
        user_id, level = user
        print(f"Welcome back, {username}! You are at level {level}.")
    else:
        # Insert a new user record
        cursor.execute(
            "INSERT INTO \"user\" (username) VALUES (%s) RETURNING id, level",
            (username,)
        )
        user_id, level = cursor.fetchone()
        connection.commit()
        print(f"Welcome, {username}! Starting at level {level}.")

    return user_id, level

def game_loop():
    """Main game loop function."""
    game_over = False
    game_close = False
    paused = False

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    # Initialize user data
    user_id, level = get_user_data()

    foodx, foody, food_color = generate_food()

    # Timer for food disappearance
    food_timer = time.time() + 5  # Food disappears after 5 seconds

    while not game_over:

        # Handle game over condition
        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
                if event.type == pygame.QUIT:
                    game_over = True
                    break

        # Check for pause shortcut
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        print("Game paused. Press P to resume.")
                    else:
                        print("Game resumed.")
                elif event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
            elif event.type == pygame.QUIT:
                game_over = True
                break

        # Handle game pausing
        if paused:
            # Save the current state of the game if the user is asked to save
            if input("Would you like to save the game? (y/n): ").lower() == 'y':
                save_game_state(user_id, length_of_snake - 1)
            continue

        # Game logic
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Draw food
        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block])

        # Check if food disappears
        if time.time() > food_timer:
            foodx, foody, food_color = generate_food()
            food_timer = time.time() + 5  # Reset timer

        # Snake movement and collision
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check for snake collision
        for part in snake_list[:-1]:
            if part == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats food
        if x1 == foodx and y1 == foody:
            foodx, foody, food_color = generate_food()

            save_game_state(user_id, length_of_snake - 1)
            length_of_snake += 1

        clock.tick(snake_speed)

    # Cleanup
    cursor.close()
    connection.close()
    pygame.quit()
    quit()

game_loop()
