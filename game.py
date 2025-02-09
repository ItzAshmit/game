import pygame
from sys import exit


def display_score():
    global current_time
    current_time = int(pygame.time.get_ticks() // 1000) - start_time
    text_surface = test_font.render(f"Score: {current_time}", False, (64, 64, 64))
    score_rect = text_surface.get_rect(center=(400, 50))
    screen.blit(text_surface, score_rect)
    

    
    


game_active = True
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font(r"C:\Users\karth\Downloads\ComingSoon-Regular.ttf", 50)
sky_surface = pygame.image.load(r"C:\Users\karth\Pictures\sky.png").convert_alpha()
enemy_surface2 = pygame.image.load(r"C:\Users\karth\Downloads\car (1).png").convert_alpha()
enemy_rect2 = enemy_surface2.get_rect(center=(350,290))

text_surface = test_font.render("lets start", False, "cyan")
score_rect = text_surface.get_rect(topleft=(220,43))
enemy_surface = pygame.image.load(r"C:\Users\karth\Downloads\car (1).png").convert_alpha()
enemy_rect = enemy_surface.get_rect(topleft=(350,290))
ground = (0,250)
player_surface = pygame.image.load(r"C:\Users\karth\Downloads\bluet (1).png").convert_alpha()
player_rect = player_surface.get_rect(topleft = (100, 315))
player_rect = player_rect.inflate(-20, -20)
enemy_rect = enemy_rect.inflate(-20, -20)
Atext_surface = test_font.render("Press enter to retry", False, "red")
Atext_rect = Atext_surface.get_rect(topleft = (100, 315))
player_gravity = 0
start_time = 0
start_time -= pygame.time.get_ticks() // 1000 // 60    

snail_speed = 6
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
      
    
    
        # if game_active:
        #     if event.type == pygame.MOUSEMOTION:
        #         print(event.pos)
        

    
    
    
    if game_active:
        #BACKGROUND
        screen.blit(sky_surface, (0,0))
        pygame.draw.line(screen,"green",(0,320),(800,320),width=10)

        
        #___________

        
        
        #ENEMY    
        enemy_rect.left += snail_speed


        if enemy_rect.left > 800:
            enemy_rect.left = -200
            snail_speed+=0.5
        screen.blit(enemy_surface,enemy_rect)

        if enemy_rect.colliderect(player_rect):
            game_active = False
        #____________

        #PLAYER
        player_gravity+=1
        player_rect.y += player_gravity
        
        
        keys = pygame.key.get_pressed()
        #MOVEMENT
        if keys[pygame.K_SPACE] and player_rect.bottom >= 310:
            player_gravity = -20 
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_rect.left += -5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_rect.right += 5
        display_score()
                    
        if player_rect.bottom >= 310:
            player_rect.bottom = 310   
        screen.blit(player_surface, player_rect)
        #___________
    else:
        start_time = pygame.time.get_ticks() // 1000
        screen.fill("red")
        enemy_rect.width=500
        enemy_rect.center = (400,300)
        enemy_rect.height=500
        pygame.draw.ellipse(screen,"#03FFDC",enemy_rect,width=50)
        enemy_rect.height=450
        enemy_rect.width=450
        enemy_rect.center = (400,325)
        pygame.draw.ellipse(screen,"#0B47FF",enemy_rect,width=1000)

        score_rect.y = 25
        score_rect.x = 260
        
        
        Btext_surface = test_font.render(f"Your Score:{current_time}", False, "green")
        Btext_rect = Btext_surface.get_rect(center = (400, 310))

        score_rect.width=285
        # pygame.draw.rect(screen,(30,40,230),score_rect)
        player_surface2 = pygame.transform.scale(player_surface,(350,200))
        pygame.draw.rect(screen,"#1681F5",score_rect,5,100)
        enemy_rect.center = (453,400)
        enemy_rect.y = 100
        screen.blit(player_surface2,enemy_rect)
        
        
        text_surface = test_font.render(f"GAME OVER", False, (64, 64, 64))
        screen.blit(text_surface, score_rect)
        Atext_rect.left = 168
        screen.blit(Atext_surface, Atext_rect)
        screen.blit(Btext_surface,Btext_rect)

        
        



        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
                game_active = True
                enemy_rect.left =  350
                score_rect = text_surface.get_rect(topleft=(220,43))
                enemy_surface = pygame.image.load(r"C:\Users\karth\Downloads\car (1).png").convert_alpha()
                enemy_rect = enemy_surface.get_rect(topleft=(350,290))
                ground = (0,250)
                player_surface = pygame.image.load(r"C:\Users\karth\Downloads\bluet (1).png").convert_alpha()
                player_rect = player_surface.get_rect(topleft = (100, 315))
                player_rect = player_rect.inflate(-20, -20)
                enemy_rect = enemy_rect.inflate(-20, -20)
                snail_speed = 6
    

    
    
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print("collision")

    pygame.display.update()
    clock.tick(60)                                                                                                                      