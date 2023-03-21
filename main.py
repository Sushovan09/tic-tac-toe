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
circle = pygame.image.load("circle2.png")

line_horizontal = pygame.image.load("line1.png")
line_vertical = pygame.image.load("line.png")
line_tilted_down = pygame.image.load("line3.png")
line_tilted_up = pygame.image.load("line2.png")

line_horizontal_pos = [[0,-175],[0,-25],[0,125]]
line_vertical_pos = [[-175,0],[-25,0],[125,0]]
line_tilted_up_pos = [-25,-25]
line_tilted_down_pos = [-9,-7]


position_array = [[50,50],[200,50],[350,50],[50,200],[200,200],[350,200],[50,350],[200,350],[350,350]]

x_position = [False,False,False,False,False,False,False,False]
o_position = [False,False,False,False,False,False,False,False]

wining_combination =[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

real_pos = [0,0,0,0,0,0,0,0,0] #can be [0,1,2]  0->means no element. 1-> means circle. 2->means cross.

#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #RGB - Red, Green ,Blue
    screen.fill((255,255,255))
    #background image
    screen.blit(background,(0,0))
    
    screen.blit(cross,(50,50))
    screen.blit(circle,(200,50))
    screen.blit(circle,(350,50))
    screen.blit(cross,(50,200))
    screen.blit(cross,(200,200))
    screen.blit(cross,(350,200))
    screen.blit(cross,(50,350))
    screen.blit(cross,(200,350))
    screen.blit(circle,(350,350))

    screen.blit( line_tilted_down , line_tilted_down_pos)
    screen.blit( line_tilted_up , line_tilted_up_pos )

    screen.blit( line_horizontal , line_horizontal_pos[0] )
    screen.blit( line_horizontal , line_horizontal_pos[1] )
    screen.blit( line_horizontal , line_horizontal_pos[2] )

    screen.blit( line_vertical , line_vertical_pos[0] )
    screen.blit( line_vertical , line_vertical_pos[1] )
    screen.blit( line_vertical , line_vertical_pos[2] )


    pygame.display.update()


