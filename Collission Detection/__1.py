"""
K_UP                  up arrow
K_DOWN                down arrow
K_RIGHT               right arrow
K_LEFT                left arrow

Coordinates for Central Block
leftBoundary = (1100/2) - (112/2)= 550-56 =494
rightBoundary = (1100/2) + (112/2)= 550+56 =606
topBoundary = (650/2) - (112/2) = 325-56 = 279
BottomBoundary = (650/2) + (112/2) = 325+56 = 381
"""
import pygame, sys
import time
import phygital_v2 as phy



phy.pinMode(2,"doutput")
phy.pinMode(3,"doutput")
#phy.pinMode(1,"Servo")

phy.init("COM7")


def showImage(img, pos):
    if img!= '':        
        image=pygame.image.load("images/"+ img +".png")
#        image=pygame.transform.scale(image, (813,375))
        screen.blit(image,(pos[0],pos[1]))
        
def moveDown(img,pos):
    if img!= '':        
        image=pygame.image.load("images/"+ img +".png")
        UI_init('Room_2')
        screen.blit(image,(pos[0],pos[1]+50))
        
        pos[1] = pos[1]+50
        return pos
        
def moveUp(img,pos):
    if img!= '':        
        image=pygame.image.load("images/"+ img +".png")
        UI_init('Room_2')
        screen.blit(image,(pos[0],pos[1]-50))
        
        pos[1] = pos[1]-50
        return pos
    
def moveRight(img,pos):
    if img!= '':        
        image=pygame.image.load("images/"+ img +".png")
        UI_init('Room_2')
        screen.blit(image,(pos[0]+50,pos[1]))
        
        pos[0] = pos[0]+50
        return pos
    
def moveLeft(img,pos):
    if img!= '':        
        image=pygame.image.load("images/"+ img +".png")
        UI_init('Room_2')
        screen.blit(image,(pos[0]-50,pos[1]))
        
        pos[0] = pos[0]-50
        return pos

def collisionDetection(pos):  
    """
    Coordinates for Central Block
    leftBoundary = (1100/2) - (112/2)= 550-56 =494
    rightBoundary = (1100/2) + (112/2)= 550+56 =606
    topBoundary = (650/2) - (112/2) = 325-56 = 279
    BottomBoundary = (650/2) + (112/2) = 325+56 = 381
    """
    if pos[0]>=(494-80) and pos[0]<=606 and pos[1]>=(279-80) and pos[1]<=381:
        collide = True
    else:
        collide = False
    
    return collide

def UI_init(bg):
    width=1100
    height= 650
    global screen
    screen=pygame.display.set_mode( ( width, height) )
    
#    Set a Title of Screen
    pygame.display.set_caption('First Test')
    bg=pygame.image.load("images/"+ bg +".jpg").convert_alpha()
    screen.blit(bg,(0,0))
    
pygame.init()
UI_init('Room_2')
PlayercurrentPos = [50,50]
showImage('player',PlayercurrentPos)
while True: 
    
    
    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                phy.close()
                sys.exit()
#                movie.stop()
                break
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_UP:
                    PlayercurrentPos = moveUp('player',PlayercurrentPos)
                if event.key == pygame.K_DOWN:
                    PlayercurrentPos = moveDown('player',PlayercurrentPos)
                if event.key == pygame.K_RIGHT:
                    PlayercurrentPos = moveRight('player',PlayercurrentPos)
                if event.key == pygame.K_LEFT:
                    PlayercurrentPos = moveLeft('player',PlayercurrentPos)
                print(PlayercurrentPos)  
        if collisionDetection(PlayercurrentPos):
            print('Collision')
            showImage('collision',[50,550])
            pygame.mixer.Sound('audio/bell2.wav').play()
            time.sleep(0.5)
            phy.dWrite(2,0)
            phy.dWrite(3,1)
            phy.MoveServo(1,170)
#            
            
            
        else:
            print("No")
            phy.dWrite(2,1)
            phy.dWrite(3,0)
            phy.MoveServo(1,0)
        pygame.display.update()
        time.sleep(0.1)
        
   
    
    except KeyboardInterrupt:
        break
    
print ('Closing')
pygame.quit()
phy.close()
sys.exit()