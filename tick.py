import pygame, sys

from pygame.locals import*

pygame.init()
DISPLAY = pygame.display.set_mode((600,600))
ORANGE = (255, 69, 0)
YELLOW = (255, 255, 0)
BLUE   = (0,0,255)

count = 0

def draw_grid():
	pygame.draw.line(DISPLAY, ORANGE, (220,100), (220,500), 4) #left most vertical line 
	pygame.draw.line(DISPLAY, ORANGE, (380,100), (380,500), 4) #right most vertical line 
	pygame.draw.line(DISPLAY, ORANGE, (100,220), (500,220), 4) #top most horizontal line 
	pygame.draw.line(DISPLAY, ORANGE, (100,380), (500,380), 4) #bottom most horizontal line 

def draw_cross(cenx,ceny,count):
	if(count%2 == 0):
		pygame.draw.line(DISPLAY, YELLOW, (cenx-30,ceny-30), (cenx+30,ceny+30), 7)
		pygame.draw.line(DISPLAY, YELLOW, (cenx+30,ceny-30), (cenx-30,ceny+30), 7)
	else :
		pygame.draw.circle(DISPLAY, BLUE, (cenx,ceny), 40, 7)

def mouse(pos,count):
	if( pygame.Rect(100, 100, 500, 500).collidepoint(pos)):
		if( pygame.Rect(100, 100, 120, 120).collidepoint(pos)):
			draw_cross(160, 160, count)
		if( pygame.Rect(220, 100, 160, 160).collidepoint(pos)):
			draw_cross(300, 160, count)
		if( pygame.Rect(380, 100, 120, 120).collidepoint(pos)):
			draw_cross(440, 160, count)
		if( pygame.Rect(100, 220, 120, 120).collidepoint(pos)):
			draw_cross(160, 300, count)
		if( pygame.Rect(220, 220, 160, 160).collidepoint(pos)):
			draw_cross(300, 300, count)
		if( pygame.Rect(380, 220, 120, 120).collidepoint(pos)):
			draw_cross(440, 300, count)
		if( pygame.Rect(100, 380, 120, 120).collidepoint(pos)):
			draw_cross(160, 440, count)
		if( pygame.Rect(220, 380, 160, 160).collidepoint(pos)):
			draw_cross(300, 440, count)
		if( pygame.Rect(380, 380, 120, 120).collidepoint(pos)):
			draw_cross(440, 440, count)	
		print(count)		

running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			if( pygame.Rect(100, 100, 500, 500).collidepoint(pos)):
				count += 1
			mouse(pos,count)
		draw_grid()
		pygame.display.update()