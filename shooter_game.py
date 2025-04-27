from pygame import *
from random import randint
window = display.set_mode((700,500))
display.set_caption("Шутер")
FPS = 60

x1= 10
y1 = 400
x2 = 600
y2 = 200

background = transform.scale(image.load("galaxy.jpg"),(700,500))
window.blit(background,(0,0))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
shoot = mixer.Sound('fire.ogg')

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,play_x,player_y, player_with,player_hight,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_with,player_hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = play_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_LEFT] and self.rect.x>5:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x< 630:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.top, 15,20,15)
        bullets.add(bullet)


lost = 0
score = 0
class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(0,700)
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

sprite1 = Player('rocket.png',310,435, 65,65,10)
enemy1 = Enemy('ufo.png',300,0,65,65,5)
enemy2 = Enemy('ufo.png',100,0,65,65,5)
enemy3 = Enemy('ufo.png',157,0,65,65,5)
enemy4 = Enemy('ufo.png',250,0,65,65,5)
enemy5 = Enemy('ufo.png',400,0,65,65,5)

monsters = sprite.Group()
monsters.add(enemy1)
monsters.add(enemy2)
monsters.add(enemy3)
monsters.add(enemy4)
monsters.add(enemy5)

bullets = sprite.Group()

font.init()
font1 = font.Font(None,36)
font2 = font.Font(None,36)
font3 = font.Font(None,46)

win = font3.render("YOU WIN",1,(234,222,108))
lose = font3.render("YOU LOSE",1,(234,222,108))

score = 0


clock = time.Clock()
finish = False
run = True
while run:
    if finish!= True:
        window.blit(background,(0,0))
        text = font1.render('Пропущено:' + str(lost), 1,(255,255,255))
        text2 = font2.render("Счет:" + str(score),1,(255,255,255))
        window.blit(text,(10,10))
        window.blit(text2,(10,40))
        sprite1.reset()
        sprite1.update()
        monsters.update()
        monsters.draw(window)
        keys = key.get_pressed()
        if keys[K_SPACE]:
            sprite1.fire()
            shoot.play()
        bullets.draw(window)
        bullets.update()
        sprites_list = sprite.groupcollide(monsters,bullets,True, True)
        for i in sprites_list:
            monster1 = Enemy('ufo.png',310,0,65,65,5)
            monsters.add(monster1)
            score +=1
        if sprite.spritecollide(sprite1,monsters,False):
            finish = True
            window.blit(lose, (260,250))
        if score>=10:
            finish = True
            window.blit(win, (260,250))
        if lost>=3:
            finish = True
            window.blit(lose, (260,250))


    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)

