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

def draw_cross(where,count):
	if where == 1 :
		if count%2 == 0 :
			pygame.draw.line(DISPLAY, YELLOW, (110,110), (210,210), 7)
			pygame.draw.line(DISPLAY, YELLOW, (210,110), (110,210), 7)
		else :
			pygame.draw.circle(DISPLAY, BLUE, (160,160), 40, 7)
	if where == 2 :
		if count%2 == 0 :
			pygame.draw.line(DISPLAY, YELLOW, (230,110), (370,210), 7)
			pygame.draw.line(DISPLAY, YELLOW, (370,110), (230,210), 7)
		else :
			pygame.draw.circle(DISPLAY, BLUE, (300,160), 40, 7)
	if where == 3 :
		if count%2 == 0 :
			pygame.draw.line(DISPLAY, YELLOW, (390,110), (490,210), 7)
			pygame.draw.line(DISPLAY, YELLOW, (490,110), (390,210), 7)	
		else :
			pygame.draw.circle(DISPLAY, BLUE, (440,160), 40, 7)
	if where == 4 :
		if count%2 == 0 :
			pygame.draw.line(DISPLAY, YELLOW, (110,230), (210,370), 7)
			pygame.draw.line(DISPLAY, YELLOW, (210,230), (110,370), 7)
		else :
			pygame.draw.circle(DISPLAY, BLUE, (160,300), 40, 7)
	if where == 5 :
		if count%2 == 0 :
			pygame.draw.line(DISPLAY, YELLOW, (230,230), (370,370), 7)
			pygame.draw.line(DISPLAY, YELLOW, (370,230), (230,370), 7)
		else :
			pygame.draw.circle(DISPLAY, BLUE, (300,300), 40, 7)
	if where == 6 :
		if count%2 == 0 :
			pygame.draw.line(DISPLAY, YELLOW, (390,230), (490,370), 7)
			pygame.draw.line(DISPLAY, YELLOW, (490,230), (390,370), 7)
		else :
			pygame.draw.circle(DISPLAY, BLUE, (440,300), 40, 7)
	if where == 7 :
		if count%2 == 0 :
			pygame.draw.line(DISPLAY, YELLOW, (110,390), (210,490), 7)
			pygame.draw.line(DISPLAY, YELLOW, (210,390), (110,490), 7)
		else :
			pygame.draw.circle(DISPLAY, BLUE, (160,440), 40, 7)
	if where == 8 :
		if count%2 == 0 :
			pygame.draw.line(DISPLAY, YELLOW, (230,390), (370,490), 7)
			pygame.draw.line(DISPLAY, YELLOW, (370,390), (230,490), 7)
		else :
			pygame.draw.circle(DISPLAY, BLUE, (300,440), 40, 7)
	if where == 9 :
		if count%2 == 0 :
			pygame.draw.line(DISPLAY, YELLOW, (390,390), (490,490), 7)
			pygame.draw.line(DISPLAY, YELLOW, (490,390), (390,490), 7)	
		else :
			pygame.draw.circle(DISPLAY, BLUE, (440,440), 40, 7)


def mouse(pos,count):
	if( pygame.Rect(100, 100, 500, 500).collidepoint(pos)):
		if( pygame.Rect(100, 100, 120, 120).collidepoint(pos)):
			draw_cross(1, count)
		if( pygame.Rect(220, 100, 160, 160).collidepoint(pos)):
			draw_cross(2, count)
		if( pygame.Rect(380, 100, 120, 120).collidepoint(pos)):
			draw_cross(3, count)
		if( pygame.Rect(100, 220, 120, 120).collidepoint(pos)):
			draw_cross(4, count)
		if( pygame.Rect(220, 220, 160, 160).collidepoint(pos)):
			draw_cross(5, count)
		if( pygame.Rect(380, 220, 120, 120).collidepoint(pos)):
			draw_cross(6, count)
		if( pygame.Rect(100, 380, 120, 120).collidepoint(pos)):
			draw_cross(7, count)
		if( pygame.Rect(220, 380, 160, 160).collidepoint(pos)):
			draw_cross(8, count)
		if( pygame.Rect(380, 380, 120, 120).collidepoint(pos)):
			draw_cross(9, count)	
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