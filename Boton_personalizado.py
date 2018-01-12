# coding=utf-8

import pygame,sys
from pygame.locals import*

# colores
black = (0, 0, 0)
white = (255, 255, 255)

pygame.init()
pygame.display.set_caption('Modelo de boton')
screen = pygame.display.set_mode((400, 400))

class Boton_personalizado():
	def __init__(self,posx,posy,dimen1,dimen2):
		self.x=posx
		self.y=posy
		self.largo=dimen1
		self.alto=dimen2
		self.activado=False

	def dibujar(self):
		pygame.draw.rect(screen,(white),(self.x,self.y,self.largo,self.alto))

	def deteccion(self,x,y):
		if x>self.x and x<self.x+self.largo:
			if y>self.y and y<self.y+self.alto: 
				self.activado=True
		else:
			self.activado=False

boton=Boton_personalizado(200,100,50,50)

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

    # captura el evento 'MOUSEMOTION'
	if event.type == pygame.MOUSEMOTION:
        # obtiene la posición del mouse
		x,y = pygame.mouse.get_pos()

		screen.fill(black)
		boton.deteccion(x,y)
		boton.dibujar()
	
	if event.type == pygame.MOUSEBUTTONDOWN:
		if boton.activado==True:
			print("click")

	pygame.display.flip()
