import pygame
import random, time

# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the images and scale them down
coin_image = pygame.image.load("img/SnowFlake.png")
coin_image = pygame.transform.scale(coin_image, (40, 40))
coin_rect = coin_image.get_rect() # -- get its rect object
coin_rect.centerx = screen.get_rect().centerx # -- place it in the middle of the top border
coin_rect.top = 0
screen.blit(coin_image,coin_rect)

bank_image = pygame.image.load("img/SnowMan.png")
bank_image = pygame.transform.scale(bank_image, (100, 100))
bank_rect = bank_image.get_rect() # -- get its rect object
bank_rect.centerx = screen.get_rect().centerx # -- place it at the middle of the buttom border
bank_rect.bottom = screen.get_rect().bottom
screen.blit(bank_image, bank_rect) # -- blit it on the screen


# Add a background image
background_image = pygame.image.load("img/SnowBackground.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
pygame.display.flip()
# Add coin count and level to the pygame window
font = pygame.font.Font("font.ttf", 40)
coin_count = 0
remaining_count = 10
level = 1
# Set the initial speed of the coin and bank
coin_speed = 10
bank_speed = 100

# The Game Loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            bank_rect.x -= bank_speed
            if bank_rect.left < 0:
                bank_rect.left = 0 # set the left edge of the bank to 0 if it goes beyond the screen
        if event.key == pygame.K_RIGHT:
            bank_rect.x += bank_speed
            if bank_rect.right > screen.get_rect().right:
                bank_rect.right = screen.get_rect().right
    # Game Logic
    coin_rect.y += coin_speed
    
    # If the coin goes off the screen, reset it to the top with a random x coordinate
    if coin_rect.bottom > screen.get_rect().bottom:
        coin_rect.y = 0
        coin_rect.x = random.randint(100, 600)


    # Check for collision with the bank
    if coin_rect.colliderect(bank_rect):
        coin_count += 1
        remaining_count -= 1
        coin_rect.centerx = random.randint(100, 600)
        coin_rect.top = 0
        print(f"Coin count: {coin_count}")
        
        # If the remaining count reaches zero, double the speed and reset the remaining count to 10
        if remaining_count == 0:
            coin_speed *= 2
            level += 1
            remaining_count = 10
            print(">>>>> New Level Activated")
    
    # Render
    screen.blit(background_image, (0, 0))
    screen.blit(coin_image, coin_rect)
    screen.blit(bank_image, bank_rect)
    
    # Render the coin count and level
    text = font.render(f"snowFlakes {coin_count} level {level}", True, (0, 0, 232))
    screen.blit(text, (10, 10))
    
    # Flip the display
    pygame.display.flip()
    
    # Slow down the loop to reduce CPU usage
    time.sleep(0.1)
# Quit Pygame
pygame.quit()




