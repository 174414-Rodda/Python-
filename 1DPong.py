import pygame
import random
pygame.init()

display_width = 500
display_height = 300
x = random.randint(70,200)
y = random.randint(20,150)
radius = 10
dx = 3
dy = 3
speed = 30
paddle_x,paddle_y  = 10,10
paddle_height,paddle_width = 40,4
play_score = 0
clock = pygame.time.Clock()
def hit_back():
    if x+radius > display_width:
        return True
    return False
def hit_sides():
    if (y-radius < 0) or (y+radius > display_height):
        return True
    return False
def hit_paddle():
    global play_score
    if x-radius <= paddle_x + paddle_width and y > paddle_y and y < paddle_y+paddle_height:
        play_score+=10
        return True
    return False
def gameover():
    end = True
    display.fill((0,0,0))
    font_title = pygame.font.Font(None,36)
    font_inst = pygame.font.Font(None,24)
    announcement = font_title.render("GameOver", True, (255,255,255))
    announcement_rect = announcement.get_rect(center = (int(display_width/2),int(display_height/2)))
    display.blit(announcement,announcement_rect)
    announcementQ = font_title.render("Press q to Quit", True, (255,255,255))
    announcement_rectQ = announcement.get_rect(center = (int(display_width/2),int(display_height/1.5)))
    display.blit(announcementQ,announcement_rectQ)
    announcementR = font_title.render("Press r to Resume", True, (255,255,255))
    announcement_rectR = announcement.get_rect(center = (int(display_width/2),int(display_height/1.3)))
    display.blit(announcementR,announcement_rectR)

    pygame.display.flip()
    while(end):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                print("saIRAN")
                if event.key == pygame.K_q:
                    exit()
                if event.key == pygame.K_r:
                    return
display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("1D-Pong")
font_title = pygame.font.Font(None,30)
announcement = font_title.render("Rodda", True, (255,255,255))
announcement_rect = announcement.get_rect(center = (50,50))
announcements = font_title.render("It will start in 2 Sec, Press s to start Now", True, (255,255,255))
announcement_rects = announcement.get_rect(center = (50,90))
display.blit(announcements,announcement_rects)
display.blit(announcement,announcement_rect)
pygame.display.flip()
pygame.time.set_timer(pygame.USEREVENT,2500)
set_timer = True
while set_timer:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            set_timer=False
        if event.type == pygame.KEYDOWN:
            print("saIRAN")
            if event.key == pygame.K_s:
                set_timer=False
        

while True:
    clock.tick(speed)
    pressed= pygame.key.get_pressed()
    if(pressed[pygame.K_DOWN]):
        if(paddle_height+paddle_y + 10 <= display_height):
            paddle_y+=10
    if(pressed[pygame.K_UP]):
        if(paddle_y - 10 >= 0):
            paddle_y-=10
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    display.fill((0,0,0))
    x+=dx
    y+=dy
    pygame.draw.rect(display, (255,255,255), (paddle_x,paddle_y,paddle_width,paddle_height))
    pygame.draw.circle(display, (255,255,255), (x,y), radius)
    if(x < radius):
        gameover()
        x,y=250,250
        dx=abs(dx)
    if(hit_back() or hit_paddle()):
        dx*=-1
       
    if(hit_sides()):
        dy*=-1
       
    
    pygame.display.update()
    
