import pygame, sys

from pygame.locals import*

pygame.init()
DISPLAY = pygame.display.set_mode((600,600))
ORANGE = (255, 69, 0)
YELLOW = (255, 255, 0)
BLUE   = (0,0,255)
count = 0
A = [[0 for i in range(3)] for j in range(3)]

#draws the four lines of the game 
def draw_grid():
	pygame.draw.line(DISPLAY, ORANGE, (220,100), (220,500), 4) #left-most vertical line 
	pygame.draw.line(DISPLAY, ORANGE, (380,100), (380,500), 4) #right-most vertical line 
	pygame.draw.line(DISPLAY, ORANGE, (100,220), (500,220), 4) #top-most horizontal line 
	pygame.draw.line(DISPLAY, ORANGE, (100,380), (500,380), 4) #bottom-most horizontal line 

#draws either the cross or the circle according to the player's turn
def draw_obj(cenx,ceny,count):
	if(count%2 == 0):
		pygame.draw.line(DISPLAY, YELLOW, (cenx-30,ceny-30), (cenx+30,ceny+30), 7)
		pygame.draw.line(DISPLAY, YELLOW, (cenx+30,ceny-30), (cenx-30,ceny+30), 7)
	else :
		pygame.draw.circle(DISPLAY, BLUE, (cenx,ceny), 40, 7)

#tracks where the mouse has been clicked, returns true if the player has clicked on an empty space 
def mouse(pos,countm,A):
	if( pygame.Rect(100, 100, 500, 500).collidepoint(pos)):
		if( pygame.Rect(100, 100, 120, 120).collidepoint(pos) and A[0][0]!=1):
			draw_obj(160, 160, count)
			A[0][0] = 1
			return True
		if( pygame.Rect(220, 100, 160, 160).collidepoint(pos) and A[0][1]!=1):
			draw_obj(300, 160, count)
			A[0][1] = 1
			return True
		if( pygame.Rect(380, 100, 120, 120).collidepoint(pos) and A[0][2]!=1):
			draw_obj(440, 160, count)
			A[0][2] = 1
			return True
		if( pygame.Rect(100, 220, 120, 120).collidepoint(pos) and A[1][0]!=1):
			draw_obj(160, 300, count)
			A[1][0] = 1
			return True
		if( pygame.Rect(220, 220, 160, 160).collidepoint(pos) and A[1][1]!=1):
			draw_obj(300, 300, count)
			A[1][1] = 1
			return True
		if( pygame.Rect(380, 220, 120, 120).collidepoint(pos) and A[1][2]!=1):
			draw_obj(440, 300, count)
			A[1][2] = 1
			return True
		if( pygame.Rect(100, 380, 120, 120).collidepoint(pos) and A[2][0]!=1):
			draw_obj(160, 440, count)
			A[2][0] = 1
			return True
		if( pygame.Rect(220, 380, 160, 160).collidepoint(pos) and A[2][1]!=1):
			draw_obj(300, 440, count)
			A[2][1] = 1
			return True
		if( pygame.Rect(380, 380, 120, 120).collidepoint(pos) and A[2][2]!=1):
			draw_obj(440, 440, count)	
			A[2][2] = 1
			return True
		print(count)		

#the main game loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			if(mouse(pos,count,A)):
				count += 1
		draw_grid()
		pygame.display.update()