# Our imports
import random,pygame,sys
import time
import pygame.font

pygame.init() # Initializes pygame
screen = pygame.display.set_mode((800,600)) # Creates the screen
pygame.display.set_caption('Random Dodge Game') # Title of the game
w_screen = pygame.display.get_surface 
red = (255,0,0)
blue = (0,0,255)

score = pygame.time.get_ticks() // 1000 # There will be a clock in the game

game_over = False
clock = pygame.time.Clock() # We create an instance of a clock
speed = 40
enemy_pos = [random.randint(0,800),0] # Enemies are going to come from random x position
player_pos = [400,500] 
a = 0
#score = pygame.time.get_ticks() // 1000
def draw_timer():
    # Draws the timer
    score = pygame.time.get_ticks() // 1000
    font_color = pygame.Color("white")
    font_bg    = pygame.Color("black")
    font       = pygame.font.SysFont("arial", 50)
    text_img   = font.render(str(score), True, font_color, font_bg)     
    text_pos   = (750,10)
    screen.blit(text_img, text_pos)
    return score

draw_timer()
                
def detect_collision(player_pos, enemy_pos):
    ''' Checks if player's pos collides with enemy's position
        Returns true if it does. Return false otherwise '''
    
    p_x = player_pos[0]
    p_y = player_pos[1]
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if (p_x <= e_x and e_x < (p_x + 50)) or (p_x >= e_x and p_x < (e_x + 50)): # Square of the players and of enemies are going to be 50x50
        if (e_y >= p_y and e_y < (p_y + 50)) or (p_y >= e_y and p_y < (e_y + 50)):
            return True
    return False
    
while game_over == False:
    # Our main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN: # Player's model teleports to random location in the same x axis when user clicks spacebar (You can change the button from the code below see --> (pygame.K_SPACE))
            if event.key == pygame.K_SPACE:
                player_pos[0] = random.randint(0,800)
    

    screen.fill((0,0,0))   
    if enemy_pos[1]>=0 and enemy_pos[1]<600: # Enemy model's are going to move as long as they are visible in screen with the speed we declared in line 17
        enemy_pos[1] += speed
    else:
        enemy_pos[0] = random.randint(0,750) # Enemy model's are going to spawn at random x locations from top of the screen
        enemy_pos[1] = 0 
    
    if detect_collision(player_pos,enemy_pos): # Game ends if enemy model collides with player model
        game_over = True
        

    new_score = draw_timer() # Draws the timer and saves score
    
    
    
    if (int(score) != 0) and (int(score) % 5 == 0): # Speed of enemies increase after each 5 seconds
        speed += 0.5055
    
    pygame.draw.rect(screen,blue,(enemy_pos[0],enemy_pos[1],50,50)) # Draws enemy model (Check pygame documentation for more information about pygame.draw.rect())
    pygame.draw.rect(screen,red,(player_pos[0],player_pos[1],50,50)) # Draws user model
    clock.tick(20)
    pygame.display.update()
else:
    # Displays the game over message with how much time user survived for
    font_color_b = pygame.Color("blue")
    font_bg_b    = pygame.Color("black")
    font_b       = pygame.font.SysFont("arial", 50)
    text_img_b   = font_b.render(("GAME OVER. YOUR SCORE IS " + str(new_score)), True, font_color_b, font_bg_b)     
    text_pos_b   = (10,250)
    screen.blit(text_img_b, text_pos_b)    
    pygame.display.update()
    

