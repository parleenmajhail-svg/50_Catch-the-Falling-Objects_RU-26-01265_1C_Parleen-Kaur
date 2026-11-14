import pygame 
import random
# Initialize Pygame
pygame.init()
#Screen 
WIDTH = 500
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Catch The Faliiing Objects")
#Colors
WHITE = (255,255,255)
RED = (180,0,0)
BLACK = (0,0,0)
GREEN = (0,150,0)
BLUE = (135,206,235)
VIOLET = (75,0,130)
#Basket
basket = pygame.Rect(210,560,80,20)
basket_speed = 7
#Falling Object
obj = pygame.Rect(random.randint(0,480),0,20,20)
obj_speed = 5
#Score and lives
score = 0
lives = 3
font = pygame.font.Font(None,36)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Move basket
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        basket.x -= basket_speed

    if keys[pygame.K_RIGHT]:
        basket.x += basket_speed

    # Keep basket inside screen
    basket.x = max(0, min(basket.x, WIDTH - basket.width))

    # Move falling object
    obj.y += obj_speed

    # Catch object
    if basket.colliderect(obj):
        score += 1
        obj.x = random.randint(0, WIDTH - obj.width)
        obj.y = 0

    # Miss object
    if obj.y > HEIGHT:
        lives -= 1
        obj.x = random.randint(0, WIDTH - obj.width)
        obj.y = 0

    # Draw everything
    screen.fill(BLUE)
    pygame.draw.rect(screen,RED, basket)
    pygame.draw.rect(screen,BLACK,basket,2)
    pygame.draw.rect(screen,VIOLET, obj)
    pygame.draw.rect(screen,GREEN,(0,580,WIDTH,20))

    screen.blit(font.render(f"Score: {score}", True, BLACK), (10,10))
    screen.blit(font.render(f"Lives: {lives}", True, BLACK), (380, 10))

    # Game Over
    if lives <= 0:
        screen.fill(WHITE)
        screen.blit(font.render("GAME OVER", True, RED), (160, 250))
        screen.blit(font.render(f"Final Score: {score}", True, BLACK), (150, 300))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()