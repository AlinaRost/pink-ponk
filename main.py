from pygame import *
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
    
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
    
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
            
back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
game = True
finish = False
clock = time.Clock()
fps = 60 
rocet1 = Player('rocet.png',30,200,4,50,150)
rocet2 = Player('rocet.png',520,200,4,50,150)
ball = GameSprite('tenis_ball.png',200,200,4,50,50)
font.init()
font = font.Font(None,35)
lose1 = font.render('Player1 lose',True,'180,0,0')
lose2 = font.render('Player2 lose',True,'180,0,0')
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.fill(back)
        rocet1.update_l()
        rocet2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(rocet1,ball) or sprite.collide_rect(rocet2,ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y> win_height -50 or ball.rect.y<0:
            speed_y*= - 1
        if ball.rect.x <0:
            finish = True
            window.blit(lose1,(200,200))
            #game_over = True
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose1,(200,200))
            #game_over = True
        rocet1.reset()
        rocet2.reset()
        ball.reset()
    display.update()
    clock.tic(fps)
