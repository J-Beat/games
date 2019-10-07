import pygame as pg
import random
import time

win_height = 450
win_width = 400

Display = (win_width, win_height)
bg_color = '#004400'
bill = 1


def main():
	pg.init()
	screen = pg.display.set_mode(Display)
	pg.display.set_caption('My new game')
	bg = pg.Surface((win_width, win_height))
	bg.fill(pg.Color(bg_color))
	left = right = False
	pt = False

	Ball = ball(150, 20)
	hero = Player(150, 420)
	global bill
	fal = 0
	f1 = pg.font.Font(None, 30)


	entities = pg.sprite.Group()
	platforms = []
	entities.add(Ball)
	entities.add(hero)
	
		



	level = ['----------------------------------------',
			'-                                      -',
			'-                        --            -',
			'-                       --             -',
			'-        -              -       -      -',
			'-       -                       -      -',
			'-      -                        -      -',
			'-                               -      -',
			'-               -               -      -',
			'-                -                     -',
			'-                 -                    -',
			'-                  -                   -',
			'-                                      -',
			'-                                      -',
			'-   --                                 -',
			'-                                      -',
			'-            ---                       -',
			'-                                      -',
			'-                                      -',
			'-                              -       -',
			'-                             -        -',
			'-                            -         -',
			'-      -                     -         -',
			'-               ----         -         -',
			'-      -                     -         -',
			'-                            -         -',
			'-      -                               -',
			'-                                      -',
			'-                                      -',
			'-                                      -',
			'-                                      -',
			'-                                      -',
			'-                                      -',
			'-                                      -',
			'-                                      -',
			'-                                      -',
			'-                                      -',
			'-                                      -',
			'-                                      -',
			'-                                      -',
			'-                                      -',
			'---                                  ---',
			'-                                      -',
			'-                                      -',
			'-                                      -']
	# f = pg.font.Font(None, 30)
	# bill2 = str('Your score: ' + str(bill))
	# tex = f.render(bill2, 1, (180, 250, 250), (150, 150, 150))
	# tex2 = f.render(('OMT?'), 1, (180, 250, 250), (150, 150, 150))
	# screen.blit(tex, (200, 150))
	# screen.blit(tex2, (300, 150))



	x=y=0
	for row in level:
		for col in row:
			if col == "-":
				pf = Platform(x, y)
				entities.add(pf)
				platforms.append(pf)
			x += 10
		y += 10
		x = 0
	
	timer = pg.time.Clock()

	while 1==1:
		timer.tick(60)

		if pg.sprite.collide_rect(Ball, hero):
				pt = True
				bill +=5
		else:
			pt = False
		
		for i in pg.event.get():
			if i.type == pg.QUIT:
				raise SystemExit
			if i.type == pg.KEYDOWN and i.key == pg.K_LEFT:
				left = True
			if i.type == pg.KEYUP and i.key == pg.K_LEFT:
				left = False
			if i.type == pg.KEYDOWN and i.key == pg.K_RIGHT:
				right = True
			if i.type == pg.KEYUP and i.key == pg.K_RIGHT:
				right = False
			


		screen.blit(bg, (0, 0))
		hero.update(left, right, platforms)
		Ball.update(platforms, pt)
		
		entities.draw(screen)
		
		text1 = f1.render(str(bill), 1, (180, 250, 250), (150, 150, 150))
		screen.blit(text1, (10, 10))
		
		pg.display.update()



class ball(pg.sprite.Sprite):
	def __init__(self, x, y):
		pg.sprite.Sprite.__init__(self)
		self.xvel = 0
		self.yvel = 0
		self.onGround = False
		self.image = pg.Surface((10, 10))
		self.image.fill(pg.Color('#888888'))
		self.rect = pg.Rect(x, y, 10, 10)

	def update(self, platforms, pt):
		if self.onGround == False:
			self.yvel += 0.35
		self.onGround = False

		self.rect.y += self.yvel
		self.collide(0, self.yvel, platforms, pt)
		self.rect.x += self.xvel
		self.collide(self.xvel, 0, platforms, pt)

	def collide(self, xvel, yvel, platforms, pt):
		global bill
		global fal
		if pt == True:
			self.rect.bottom = 350

			self.onGround = True
			self.yvel = -12
			if self.xvel == 0:
				self.xvel = random.randint(-10, 10)
			else:
				self.xvel = self.xvel
		if self.rect.bottom > 500:
			#time.sleep(10)
			self.rect.x = 150
			self.rect.y = 20
			self.xvel = 0
			self.yvel = 0
			bill = 0
			fal = 1

		else:
			for p in platforms:
				if pg.sprite.collide_rect(self, p):
					if xvel > 0:
						self.rect.right = p.rect.left
						self.xvel = -xvel#random.randint(-5, -1)

					if xvel < 0:
						self.rect.left = p.rect.right
						self.xvel = -xvel#random.randint(1, 5)

					if yvel > 0:
						self.rect.bottom = p.rect.top
						self.onGround = True
						self.yvel = -self.yvel
						if self.xvel == 0:
							self.xvel = random.randint(-5, 5)
						else:
							self.xvel = self.xvel
						
					if yvel < 0:
						self.rect.top = p.rect.bottom
						self.yvel = 0


class Player(pg.sprite.Sprite):
	def __init__(self, x, y):
		pg.sprite.Sprite.__init__(self)
		self.xvel = 0
		self.yvel = 0
		self.startX = x
		self.startY = y
		self.image = pg.Surface((80, 20))
		self.image.fill(pg.Color('#888888'))
		self.rect = pg.Rect(x, y, 80, 20)

	def update(self, left, right, platforms):
		if left:
			self.xvel -=  1
			self.image.fill(pg.Color('#888888'))

		if right:
			self.xvel += 1
			self.image.fill(pg.Color('#888888'))
		if not (left or right):
			self.xvel = 0

		self.rect.y += self.yvel
		self.collide(0, self.yvel, platforms)
		self.rect.x += self.xvel
		self.collide(self.xvel, 0, platforms)

	def collide(self, xvel, yvel, platforms):
		for p in platforms:
			if pg.sprite.collide_rect(self, p):
				if xvel > 0:
					self.rect.right = p.rect.left

				if xvel < 0:
					self.rect.left = p.rect.right



pl_wifth = 10
pl_height = 10
PLATFORM_COLOR = "#FF6262"

class Platform(pg.sprite.Sprite):
	def __init__(self, x, y):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((pl_wifth, pl_height))
		self.image.fill(pg.Color(PLATFORM_COLOR))
		self.rect = pg.Rect(x, y, pl_wifth, pl_height)	



if __name__ == '__main__':
	main()

