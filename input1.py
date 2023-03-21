import pygame
import random


#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((500,500))

#title and icon 
pygame.display.set_caption(" Tic-Tac-Toe")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#background
background = pygame.image.load("backMain.png")


#cross and circle
cross = pygame.image.load("cancel.png")
circle = pygame.image.load("circle.png")

line_horizontal = pygame.image.load("line1.png")
line_vertical = pygame.image.load("line.png")
line_tilted_down = pygame.image.load("line3.png")
line_tilted_up = pygame.image.load("line2.png")

line_horizontal_pos = [[0,-175],[0,-25],[0,125]]
line_vertical_pos = [[-175,0],[-25,0],[125,0]]
line_tilted_up_pos = [-25,-25]
line_tilted_down_pos = [-9,-7]





position_array = [[50,50],[200,50],[350,50],[50,200],[200,200],[350,200],[50,350],[200,350],[350,350]]

x_position = [False,False,False,False,False,False,False,False,False]
o_position = [False,False,False,False,False,False,False,False,False]

wining_combination =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

real_pos = [0,0,0,0,0,0,0,0,0] #can be [0,1,2]  0->means no element. 1-> means circle. 2->means cross.

main_wining_combination = [] 

def checkingWin(array):
    global main_wining_combination
    for element in wining_combination:
        if(array[element[0]-1] and array[element[1]-1] and array[element[2]-1]):
            main_wining_combination = element
            return True
    return False

def wining_animation(combination):
    if(combination == [1,2,3]):
           screen.blit( line_horizontal , line_horizontal_pos[0] )
    if(combination == [4,5,6]):
           screen.blit( line_horizontal , line_horizontal_pos[1] )    
    if(combination == [7,8,9]):
           screen.blit( line_horizontal , line_horizontal_pos[2] )
    if(combination == [1,4,7]):
           screen.blit( line_vertical ,  line_vertical_pos[0] )
    if(combination == [2,5,8]):
           screen.blit( line_vertical , line_vertical_pos[1] )
    if(combination == [3,6,9]):
           screen.blit( line_vertical , line_vertical_pos[2] )
    if(combination == [1,5,9]):
           screen.blit( line_tilted_down , line_tilted_down_pos )
    if(combination == [3,5,7]):
           screen.blit( line_tilted_up , line_tilted_up_pos )         

def board_Print():
     for i in range(0,len(real_pos)):
            if(real_pos[i]==1):
                screen.blit(circle,(position_array[i])) 
            if(real_pos[i]==2):
                screen.blit(cross,(position_array[i])) 

def setElement(type,pos):
    if(type == 'circle'):
        o_position[pos-1] = True
        real_pos[pos-1] = 1
    if(type == 'cross'):
        x_position[pos-1] = True
        real_pos[pos-1] = 2


current_type = 'cross'

def current_type_change():
    global current_type
    if current_type == 'cross':
        current_type = 'circle'
    else:
        current_type = 'cross'

gameNotEnd = True


#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if(gameNotEnd):
                 
                if(pos[0]>=0 and pos[0]<=167 and pos[1]>=0 and pos[1]<=154):
                    if(real_pos[0]==0):
                        setElement(current_type,1)
                        current_type_change()

                if(pos[0]>=175 and pos[0]<=300 and pos[1]>=0 and pos[1]<=155):
                    if(real_pos[1]==0):
                        setElement(current_type,2)
                        current_type_change()


                if(pos[0]>=304 and pos[0]<=500 and pos[1]>=0 and pos[1]<=154):
                    if(real_pos[2]==0):
                        setElement(current_type,3)
                        current_type_change()


                if(pos[0]>=0 and pos[0]<=167 and pos[1]>=163 and pos[1]<=285):
                    if(real_pos[3]==0):
                        setElement(current_type,4)
                        current_type_change()


                if(pos[0]>=172 and pos[0]<=290 and pos[1]>=161 and pos[1]<=289):
                    if(real_pos[4]==0):
                        setElement(current_type,5)
                        current_type_change()


                if(pos[0]>=303 and pos[0]<=500 and pos[1]>=162 and pos[1]<=290):
                    if(real_pos[5]==0):
                        setElement(current_type,6)
                        current_type_change()

                if(pos[0]>=0 and pos[0]<=148 and pos[1]>=293 and pos[1]<=500):
                    if(real_pos[6]==0):
                        setElement(current_type,7)
                        current_type_change()

                if(pos[0]>=172 and pos[0]<=284 and pos[1]>=293 and pos[1]<=500):
                    if(real_pos[7]==0):
                        setElement(current_type,8)
                        current_type_change()

                if(pos[0]>=289 and pos[0]<=500 and pos[1]>=293 and pos[1]<=500):
                    if(real_pos[8]==0):
                        setElement(current_type,9)
                        current_type_change()


           

    #RGB - Red, Green ,Blue
    screen.fill((255,255,255))
    #background image
    screen.blit(background,(0,0))
    
    board_Print()

    if(checkingWin(x_position)):
        wining_animation(main_wining_combination)
        gameNotEnd = False 
                   
    if(checkingWin(o_position)):
        wining_animation(main_wining_combination)
        gameNotEnd = False


    pygame.display.update()


