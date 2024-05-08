from pygame import *

clock = time.Clock()
FPS = 50
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Вызываем конструктор класса (Sprite):
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
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed



win_width = 700
win_height = 600
display.set_caption("Ping_Pong Game")
window = display.set_mode((win_width, win_height))
window.fill((255,30,15))

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render(
    'PLAYER 1 LOSE!', True, (180, 0, 0))

font2 = font.Font(None, 35)
lose2 = font1.render(
    'PLAYER 2 LOSE!', True, (180, 0, 0))


speed_x = 3
speed_y = 3
#player sprite 
player_1 = Player('racket.png', 20, 10, 30, 70, 5)
player_2 = Player('racket.png', 650, 400, 30, 70, 5)
ball = GameSprite('tenis_ball.png', 350, 300, 15, 15, 3)


#Основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.fill((149, 213, 193))
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    

    if ball.rect.y > win_height-25 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(player_1, ball) or sprite.collide_rect(player_2, ball):
            speed_x *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))

    if ball.rect.x > 700:
        finish = True
        window.blit(lose2, (200, 200))

    ball.reset()
    player_2.update_1()
    player_2.reset()
    player_1.update_r()
    player_1.reset()
    display.update()
    clock.tick(FPS)