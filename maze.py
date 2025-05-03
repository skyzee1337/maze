from pygame import *
font.init()
font1 = font.SysFont('Arial', 70)
win = font1.render('Ты выиграл!', True, (255, 215, 0))
lose = font1.render('ты проиграл:(', True, (255, 0, 0))
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')

money = mixer.Sound('money.ogg')


window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'),(700, 500))
game = True


class GameSprite(sprite.Sprite):
    def __init__(self, filename, w, h, speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(filename),(w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 435:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 635:
            self.rect.x += self.speed

class enemy(GameSprite):
    direction = 'left'
    def update(self):
            if self.rect.x <= 470:
                    self.direction = 'right'
            if self.rect.x >= 700 - 85:
                self.direction = 'left'
            
            if self.direction == 'left':
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, w, h, color, x, y):
        super().__init__()
        self.image = Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


walls = sprite.Group()
wall = Wall(30, 300, (255, 90, 43), 90, 98)            
walls.add(wall)
wall1 = Wall(100, 50, (255, 90, 43), 10, 350)            
walls.add(wall1)
wall2 = Wall(10, 300, (255, 90, 43), 190, 8)            
walls.add(wall2)
wall3 = Wall(10, 300, (255, 90, 43), 290, 198)            
walls.add(wall3)
wall4 = Wall(10, 300, (255, 90, 43), 390, 8)            
walls.add(wall4)
wall5 = Wall(10, 300, (255, 90, 43), 490, 198)            
walls.add(wall5)





player = player('hero.png', 65, 65, 4, 50, 400)
enemy = enemy('cyborg.png', 65, 65, 3, 500, 300)
shishka = GameSprite('treasure.png', 65, 65, 10, 600, 400)



clock = time.Clock()
FPS = 60    


finish = False


while game:
    if finish != True:
    

        window.blit(background, (0, 0))
        wall.draw_wall()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        player.update()
        enemy.update()
        player.reset()
        enemy.reset()
        shishka.reset()

        if sprite.collide_rect(player, enemy):
            finish = True
            kick.play()
            window.blit(lose, (200, 200))
        if sprite.collide_rect(player, shishka):
            finish = True
            money.play()
            window.blit(win, (200, 200))
        if sprite.spritecollide(player, walls, False):
            player.rect.x = 50
            player.rect.y = 400




    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
