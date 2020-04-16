import pygame, sys, time

from pygame.locals import*

pygame.init()
DISPLAY = pygame.display.set_mode((600,600))
ORANGE	= (255, 69, 0)
YELLOW	= (255, 255, 0)
BLUE	= (0,0,255)
BLACK	= (0,0,0)
count	= 0
flag 	= 1
font 	= pygame.font.Font('freesansbold.ttf',20)
A = [[0 for i in range(3)] for j in range(3)]
B = [[0 for i in range(3)] for j in range(3)]

#initialises a new game
def new_game(A,B):
	A = [[0 for i in range(3)] for j in range(3)]
	B = [[0 for i in range(3)] for j in range(3)]
	DISPLAY.fill(BLACK)
	draw_grid()
	pygame.display.update()

#prints who won the game 
def win(S) :
	if (S == 'cross'):
		text = font.render('Cross Wins !',True, YELLOW, BLACK)
		textRect = text.get_rect()
		textRect.center = (300,50)
		DISPLAY.blit(text, textRect)
		pygame.display.update()
		time.sleep(1)
	if (S == 'circle'):
		text = font.render('Circle Wins !',True, YELLOW, BLACK)
		textRect = text.get_rect()
		textRect.center = (300,50)
		DISPLAY.blit(text, textRect)
		pygame.display.update()
		time.sleep(1)

#draws the four lines of the game 
def draw_grid():
	pygame.draw.line(DISPLAY, ORANGE, (220,100), (220,500), 4) #left-most vertical line 
	pygame.draw.line(DISPLAY, ORANGE, (380,100), (380,500), 4) #right-most vertical line 
	pygame.draw.line(DISPLAY, ORANGE, (100,220), (500,220), 4) #top-most horizontal line 
	pygame.draw.line(DISPLAY, ORANGE, (100,380), (500,380), 4) #bottom-most horizontal line

#draws either the cross or the circle according to the player's turn
def draw_obj(cenx,ceny,count,wx,wy,A,B):
	if(count%2 == 0):
		pygame.draw.line(DISPLAY, YELLOW, (cenx-30,ceny-30), (cenx+30,ceny+30), 7)
		pygame.draw.line(DISPLAY, YELLOW, (cenx+30,ceny-30), (cenx-30,ceny+30), 7)
		B[wx][wy] = 1
	else :
		pygame.draw.circle(DISPLAY, BLUE, (cenx,ceny), 40, 7)
		B[wx][wy] = 2

#tracks where the mouse has been clicked, returns true if the player has clicked on an empty space 
def mouse(pos,count,A):
	if( pygame.Rect(100, 100, 500, 500).collidepoint(pos)):
		if( pygame.Rect(100, 100, 120, 120).collidepoint(pos) and A[0][0]!=1):
			draw_obj(160, 160, count,0,0,A,B)
			A[0][0] = 1
			return True
		if( pygame.Rect(220, 100, 160, 160).collidepoint(pos) and A[0][1]!=1):
			draw_obj(300, 160, count,0,1,A,B)
			A[0][1] = 1
			return True
		if( pygame.Rect(380, 100, 120, 120).collidepoint(pos) and A[0][2]!=1):
			draw_obj(440, 160, count,0,2,A,B)
			A[0][2] = 1
			return True
		if( pygame.Rect(100, 220, 120, 120).collidepoint(pos) and A[1][0]!=1):
			draw_obj(160, 300, count,1,0,A,B)
			A[1][0] = 1
			return True
		if( pygame.Rect(220, 220, 160, 160).collidepoint(pos) and A[1][1]!=1):
			draw_obj(300, 300, count,1,1,A,B)
			A[1][1] = 1
			return True
		if( pygame.Rect(380, 220, 120, 120).collidepoint(pos) and A[1][2]!=1):
			draw_obj(440, 300, count,1,2,A,B)
			A[1][2] = 1
			return True
		if( pygame.Rect(100, 380, 120, 120).collidepoint(pos) and A[2][0]!=1):
			draw_obj(160, 440, count,2,0,A,B)
			A[2][0] = 1
			return True
		if( pygame.Rect(220, 380, 160, 160).collidepoint(pos) and A[2][1]!=1):
			draw_obj(300, 440, count,2,1,A,B)
			A[2][1] = 1
			return True
		if( pygame.Rect(380, 380, 120, 120).collidepoint(pos) and A[2][2]!=1):
			draw_obj(440, 440, count,2,2,A,B)	
			A[2][2] = 1
			return True	

#checks the rules of the game and returns True if no rule is violated
def rules(A,B):
	jhanda = 0
	for x in range(3):					#if all the places in the grid are filled, the the game is over :/
		for y in range(3):
			if(A[x][y]==0):
				jhanda = 1				#jhanda = 1 means continue playing, no new game 
	if(B[0][0]==B[0][1]==B[0][2]==1 or B[0][2]==B[1][2]==B[2][2]==1 or B[2][0]==B[2][1]==B[2][2]==1 or B[0][0]==B[1][0]==B[2][0]==1 or B[0][0]==B[1][1]==B[2][2]==1 or B[0][2]==B[1][1]==B[2][0]==1):
		jhanda = 0
		win('cross')
	if(B[0][0]==B[0][1]==B[0][2]==2 or B[0][2]==B[1][2]==B[2][2]==2 or B[2][0]==B[2][1]==B[2][2]==2 or B[0][0]==B[1][0]==B[2][0]==2 or B[0][0]==B[1][1]==B[2][2]==2 or B[0][2]==B[1][1]==B[2][0]==2):
		jhanda = 0
		win('circle')
	if jhanda == 1:
		return False
	else :
		return True

#the main game loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False
			pygame.quit()
			sys.exit()
		if flag == 0 :
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					flag = 1
					A = [[0 for i in range(3)] for j in range(3)]
					B = [[0 for i in range(3)] for j in range(3)]
					DISPLAY.fill(BLACK)
					draw_grid()
					pygame.display.update()
					count = 0
		if flag == 1:
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				if(mouse(pos,count,A)):
					count += 1
			if rules(A,B) :
				flag = 0
		draw_grid()
		pygame.display.update()
		""""for x in range(3):
			for y in range(3):
				print(B[x][y],end=" ")
			print("")
		print("")
		for x in range(3):
			for y in range(3):
				print(A[x][y],end=" ")
			print("")"""