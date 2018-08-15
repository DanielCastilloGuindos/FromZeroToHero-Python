import pygame, sys, random
from pygame.locals import *

width, height  = 544, 544
sizeBox = 32
SCENE1 = [\
["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],\
["0","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","0"],\
["0","1","0","1","0","1","0","0","0","0","0","1","0","1","0","1","0"],\
["0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0"],\
["0","0","0","1","0","0","0","0","1","0","0","0","0","1","0","0","0"],\
["0","0","0","1","0","1","1","1","1","1","1","1","0","1","0","0","0"],\
["0","0","0","1","0","1","0","0","0","0","0","1","0","1","0","0","0"],\
["0","0","0","1","0","1","0","1b","1b","1b","0","1","0","P","0","0","0"],\
["1","1","1","1","1","1","0","1b","1b","1b","0","1","1","1","1","1","1"],\
["0","0","0","1","0","G3","0","1b","1b","1b","0","1","0","1","0","0","0"],\
["0","0","0","1","0","1","0","0","0","0","0","1","0","1","0","0","0"],\
["0","0","0","1","0","1","1","1","G2","1","1","1","0","1","0","0","0"],\
["0","0","0","1","0","0","0","0","1","0","0","0","0","1","0","0","0"],\
["0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","0"],\
["0","1","0","1","0","1","0","0","0","0","0","1","0","G1","0","1","0"],\
["0","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","0"],\
["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]]

class Scene:
	def __init__(self, matrix):
		self.matrix = matrix

	def drawRect(self, surface):
		temp1 = 0
		for i in self.matrix:
			temp2 = 0
			for ii in i:
				if ii == "0":
					pygame.draw.rect(surface, (0,0,0), (temp2 * sizeBox, temp1 *sizeBox, sizeBox, sizeBox), 0)
				if ii == "1":
					pygame.draw.rect(surface, (255,0,255), (temp2 * sizeBox, temp1 *sizeBox, sizeBox, sizeBox), 0)
					pygame.draw.circle(surface, (255,255,0), (temp2 * sizeBox + 16, temp1 *sizeBox + 16), 5, 0)
				if ii == "1b":
					pygame.draw.rect(surface, (255,0,255), (temp2 * sizeBox, temp1 *sizeBox, sizeBox, sizeBox), 0)
				temp2 += 1
			temp1 += 1

	def win(self):
		for i in self.matrix:
			for ii in i:
				if ii == "1":
					return False
		return True

class PacMan:
	def __init__(self,matrix):
		self.matrix = matrix
		self.letter = "P"
		self.directtion = "w"
		self.tempPos1 = "1"

	def drawRect(self, surface):
		temp1 = 0
		for i in self.matrix:
			temp2 = 0
			for ii in i:
				if ii == self.letter:
					#pygame.draw.rect(surface, (150,150,150), (temp2 * sizeBox, temp1 *sizeBox, sizeBox, sizeBox), 0)
					pygame.draw.circle(surface, (255,255,0), (temp2 * sizeBox + 16, temp1 *sizeBox + 16), 16, 0)
				temp2 += 1
			temp1 += 1

	def searchPacman(self, matriz):
		for f in range(len(matriz)):
			for c in range(len(matriz[f])):
				if matriz[f][c] == "P":
					return f, c
		return -1, -1

	def movePacman(self, matriz):
		posX, posY = self.searchPacman(matriz)
		if posX != -1:
			if self.directtion == "w":
				if matriz[posX + -1][posY] == "1" or matriz[posX + -1][posY] == "1b":
					matriz[posX][posY] = "1b"
					matriz[posX + -1][posY] = self.letter
			elif self.directtion == "d":
				if posX == 8 and posY == 16 :
					matriz[posX][posY] = self.tempPos1
					self.tempPos1 = matriz[posX][posY]
					matriz[8][0] =  self.letter
				elif matriz[posX][posY + 1] == "1" or matriz[posX][posY + 1] == "1b":
					matriz[posX][posY] = "1b"
					matriz[posX][posY + 1] = self.letter
			elif self.directtion == "s":
				if matriz[posX + 1][posY] == "1" or matriz[posX + 1][posY] == "1b":
					matriz[posX][posY] = "1b"
					matriz[posX + 1][posY] = self.letter
			elif self.directtion == "a":
				if matriz[posX][posY + -1] == "1" or matriz[posX][posY + -1] == "1b":
					matriz[posX][posY] = "1b"
					matriz[posX][posY + -1] = self.letter

	def changeDir(self, letter):
			self.directtion = letter

class Ghost:
	def __init__(self, matriz, letter):
		self.matrix = matriz
		self.letter = letter
		self.directtionList = ("w","d","s","a")
		self.directtion = self.directtionList[0]
		self.tempPos1 = "1"

	def drawRect(self, surface):
		temp1 = 0
		for i in self.matrix:
			temp2 = 0
			for ii in i:
				if ii == self.letter:
					#pygame.draw.rect(surface, (255,255,255), (temp2 * sizeBox, temp1 *sizeBox, sizeBox, sizeBox), 0)
					pygame.draw.circle(surface, (255,255,255), (temp2 * sizeBox + 16, temp1 *sizeBox + 16), 16, 0)
				temp2 += 1
			temp1 += 1

	def searchGhost(self, matriz):
		for f in range(len(matriz)):
			for c in range(len(matriz[f])):
				if matriz[f][c] == self.letter:
					return f, c
		return -1, -1

	def moveGhost(self, matriz):
		posX, posY = self.searchGhost(matriz)
		if posX != -1:
			if self.directtion == "w":
				if matriz[posX + -1][posY] == "1" or matriz[posX + -1][posY] == "1b":
					matriz[posX][posY] = self.tempPos1
					self.tempPos1 = matriz[posX + -1][posY]
					matriz[posX + -1][posY] = self.letter
				elif matriz[posX + -1][posY] == "P":
					pygame.quit()
					sys.exit()
				elif matriz[posX + -1][posY] == "0":
					self.directtion = self.directtionList[random.randint(0, 3)]
			elif self.directtion == "d":
				if matriz[posX][posY + 1] == "1" or matriz[posX][posY + 1] == "1b":
					matriz[posX][posY] = self.tempPos1
					self.tempPos1 = matriz[posX][posY + 1]
					matriz[posX][posY + 1] = self.letter
				elif posX == 8 and posY == 16 :
					matriz[posX][posY] = self.tempPos1
					self.tempPos1 = matriz[posX][posY + 1]
					matriz[8][0] =  self.letter
				elif matriz[posX][posY + 1] == "P":
					pygame.quit()
					sys.exit()
				else:
					self.directtion = self.directtionList[random.randint(0, 3)]
			elif self.directtion == "s":
				if matriz[posX + 1][posY] == "1" or matriz[posX + 1][posY] == "1b":
					matriz[posX][posY] = self.tempPos1
					self.tempPos1 = matriz[posX + 1][posY]
					matriz[posX + 1][posY] = self.letter
				elif matriz[posX + 1][posY] == "P":
					pygame.quit()
					sys.exit()
				else:
					self.directtion = self.directtionList[random.randint(0, 3)]
			elif self.directtion == "a":
				if matriz[posX][posY + -1] == "1" or matriz[posX][posY + -1] == "1b":
					matriz[posX][posY] = self.tempPos1
					self.tempPos1 = matriz[posX][posY + -1]
					matriz[posX][posY + -1] = self.letter
				elif matriz[posX][posY + -1] == "P":
					pygame.quit()
					sys.exit()
				else:
					temDir = random.randint(0, 3)
					self.directtion = self.directtionList[temDir]

def main():
	pygame.init()
	screen = pygame.display.set_mode((width, height))
	clock = pygame.time.Clock()

	scene1 = Scene(SCENE1)
	pacman1 = PacMan(SCENE1)
	ghost1 = Ghost(SCENE1, "G1")
	ghost2 = Ghost(SCENE1, "G2")
	ghost3 = Ghost(SCENE1, "G3")
	while not scene1.win():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP] or keys[pygame.K_w]:
			pacman1.changeDir("w")
		elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			pacman1.changeDir("d")
		elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
			pacman1.changeDir("s")
		elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
			pacman1.changeDir("a")

		pacman1.movePacman(SCENE1)
		ghost1.moveGhost(SCENE1)
		ghost2.moveGhost(SCENE1)
		ghost3.moveGhost(SCENE1)

		screen.fill((255,0,255))
		scene1.drawRect(screen)
		pacman1.drawRect(screen)
		ghost1.drawRect(screen)
		ghost2.drawRect(screen)
		ghost3.drawRect(screen)

		pygame.display.update()
		clock.tick(5)

if __name__ == "__main__":
	main()