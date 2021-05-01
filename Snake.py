import pygame
import random
import time
pygame.init()
width,height = 750,500
main = []
main.append((108,108,12,12))
main.append((108,120,12,12))
main.append((108,144,12,12))
speed,score,level = 10,0,0
direction = 2
nx,ny = 108,96
x=0
dif = 3
color_temp=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
bx,by = random.randrange(12,width,12),random.randrange(12,height,12)
clock = pygame.time.Clock()
def gameover():
    end = True
    board.fill((0,0,0))
    font_title = pygame.font.Font(None,36)
    font_inst = pygame.font.Font(None,24)
    announcement = font_title.render("GameOver. Score: "+str(score*10), True, (255,255,255))
    announcement_rect = announcement.get_rect(center = (int(width/2),int(height/3)))
    board.blit(announcement,announcement_rect)
    announcementQ = font_title.render("Press q to Quit", True, (255,255,255))
    announcement_rectQ = announcement.get_rect(center = (int(width/2),int(height/1.7)))
    board.blit(announcementQ,announcement_rectQ)
    announcementR = font_title.render("Press r to Restart", True, (255,255,255))
    announcement_rectR = announcement.get_rect(center = (int(width/2),int(height/2)))
    board.blit(announcementR,announcement_rectR)

    pygame.display.flip()
    while(end):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_q:
                    exit()
                if event.key == pygame.K_r:
                    return
board = pygame.display.set_mode((width,height))
pygame.display.set_caption("Drunken Snake")
font_title = pygame.font.Font(None,30)
announcement = font_title.render("Rodda-Snake", True, (255,255,255))
announcement_rect = announcement.get_rect(center = (int(width/3),int(height/3)))
announcements = font_title.render("It will start in 10 Sec, Press s to start Now", True, (255,255,255))
announcement_rects = announcement.get_rect(center = (int(width/3),int(height/2)))
board.blit(announcements,announcement_rects)
board.blit(announcement,announcement_rect)
pygame.display.flip()
pygame.time.set_timer(pygame.USEREVENT,10000)
set_timer = True
while set_timer:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            set_timer=False
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                set_timer=False

while True:
    clock.tick(speed)
    board.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction=8
            if event.key == pygame.K_DOWN:
                direction=2
            if event.key == pygame.K_RIGHT:
                direction=6
            if event.key == pygame.K_LEFT:
                direction=4
            if event.key == pygame.K_q:
                pygame.quit()
            
       
    if(score - level == 3):
        level=score
        speed+=4
        
    if direction == 2:
        ny+=12
    elif direction == 4:
        nx-=12
    elif direction == 6:
        nx+=12
    elif direction == 8:
        ny-=12
    if nx < 0:
        nx = width -12
    if nx > width:
        nx = 12
    if ny < 0:
        ny = height -12
    if ny > height:
        ny = 12
    #main.pop(1)
    
    if (nx,ny,12,12) in main:
        x=x+1
        if x-3==0:
            gameover()
            print("Gameover")
            print("New Game")
            main=[]
            main.append((108,108,12,12))
            main.append((108,120,12,12))
            main.append((108,144,12,12))
            speed,score,level = 10,0,0
            direction = 2
            x=2
            nx,ny = 108,96
            bx,by = random.randrange(12,width,12),random.randrange(12,height,12)
            
    if(abs(nx-bx) <= 10 and ny==by) or (abs(ny-by) <= 10 and nx==bx)  :
        bx,by = random.randrange(12,width,12),random.randrange(12,height,12)
        score+=1
        color_temp=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
      
    else:
        main.pop(0)
               
    main.append((nx,ny,12,12))
    
    
    pygame.draw.circle(board,(244,81,30),(bx,by),4)
    
    #color_temp = (255,255,255)
    #
    dif*=-1
    pygame.draw.rect(board,color_temp,(nx,ny,12,12))
    for i,item in enumerate (main):
        
        temp = list(item)
        
        #if(i%2 ==0  and (direction == 4 or direction==6)):
        #    temp[1]+=dif
        #if(i%2 !=0):
            #if(direction == 2 or direction==8):
                #temp[0]+=dif
            #else:
                #temp[1]+=dif
        
        pygame.draw.rect(board, (0,0,0),tuple(temp))
        pygame.draw.circle(board,(255,255,255),(temp[0]+6,temp[1]+6),7,1)
        pygame.draw.circle(board,color_temp,(temp[0]+7,temp[1]+5),3)
        #time.sleep(0.1)
    pygame.display.update()
    
