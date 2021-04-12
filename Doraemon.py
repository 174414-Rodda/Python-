import pygame
pygame.init()
clock = pygame.time.Clock()
board = pygame.display.set_mode((1300,700))
pygame.display.set_caption("Doreamon")
while True :
    
    board.fill((0,0,0))
    
    clock.tick(4)
    #pygame.draw.rect(board,(255,255,255),rect,3)
    
    
   #keys = pygame.key.get_pressed()
    event = pygame.event.get()
        
    kstate =  pygame.key.get_pressed()
    
    if pygame.key.get_pressed()[pygame.K_a]: 
        board.fill((255,255,255))           
            
    if kstate[pygame.K_q]:
            pygame.quit()#Write game for pause alaso
    pygame.draw.rect(board,(255,255,255),(450,100,400,500),4)
    pygame.draw.circle(board,(0,69,255),(650,250),75)
    pygame.draw.circle(board,(255,255,255),(650,265),60)
    pygame.draw.circle(board,(255,255,255),(635,210),17)#Eye1
    pygame.draw.circle(board,(0,0,0),(635,210),17,1)#Iborder1    
    pygame.draw.circle(board,(0,0,0),(635,210),7,3)#InnerI2  
    pygame.draw.circle(board,(255,255,255),(667,210),17)#Eye2
    
    pygame.draw.circle(board,(0,0,0),(667,210),17,1)#Iborder2
    pygame.draw.circle(board,(0,0,0),(665,210),7,3)#InnerI1  
    pygame.draw.circle(board,(255,0,0),(650,245),10)#Nose
    pygame.draw.line(board, (0,0,0), (650, 255), (650, 300),1)#Vertical Line
    pygame.draw.line(board, (0,0,0), (605,277),(692,277),1)#Horizontal Line
    pygame.draw.line(board,(0,0,0),(600,260),(643,270),1)#Topleft 1
    pygame.draw.line(board,(0,0,0),(696,260),(657,270),1)#Topright1
    pygame.draw.line(board,(0,0,0),(643,283),(600,293),1)#Bottom right
    pygame.draw.line(board,(0,0,0),(657,283),(696,293),1)#Bottom right
    pygame.draw.arc(board,(0,0,0),[624,289,55,15],3,0.1,1)#ARc
    pygame.draw.rect(board,(0,69,255),(595,320,110,90))#Bottom Rect
    pygame.draw.circle(board,(255,255,255),(650,348),45)#Down white circle
    pygame.draw.rect(board,(255,0,0),(580,310,140,10))#Cololur
    pygame.draw.circle(board,(255,255,0),(650,325),10)#Bell
    pygame.draw.rect(board,(0,0,0),(640,320,20,9),1)#Bell rect
    pygame.draw.circle(board,(0,0,0),(650,333),3)


    
    pygame.draw.circle(board,(255,255,255),(650,410),15)#Bottom circle
    pygame.draw.circle(board,(0,0,0),(650,360),24,1)#Pocket circle
    pygame.draw.rect(board,(255,255,255),(620,335,60,25))#Pocekt circle coverer
    pygame.draw.line(board,(0,0,0),(625,360),(675,360))#Pocket line
    pygame.draw.rect(board,(0,0,0),(635,410,30,30))#Down rect ot cover make semi circle
    pygame.draw.circle(board,(255,255,255),(615,410),20)#Left Leg
    pygame.draw.circle(board,(255,255,255),(685,410),20)#Right Leg


    image_orig = pygame.Surface((50 , 20))  
    image_orig.set_colorkey((0,0,0))  
    image_orig.fill((0,69,255))  
    image = image_orig.copy()  
    image.set_colorkey((0,0,0))  
    rect = image.get_rect()  
  
    rot = 31
    new_image = pygame.transform.rotate(image_orig , rot)  
    rect = new_image.get_rect()  
    rect.center = (580,340) 
    board.blit(new_image , rect)
    pygame.draw.circle(board,(255,255,255),(555,358),13)

    
    image_orig = pygame.Surface((50 , 20))  
    image_orig.set_colorkey((0,0,0))  
    image_orig.fill((0,69,255))  
    image = image_orig.copy()  
    image.set_colorkey((0,0,0))  
    rect = image.get_rect()  
  
    rot = 151
    new_image = pygame.transform.rotate(image_orig , rot)  
    rect = new_image.get_rect()  
    rect.center = (720,340) 
    board.blit(new_image , rect)
    pygame.draw.circle(board,(255,255,255),(750,355),13)
    pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 40)
    textsurface = myfont.render('Doraemon', False, (255,255,255))
    board.blit(textsurface,(570,500))
    pygame.display.flip()


    
    pygame.display.update()
