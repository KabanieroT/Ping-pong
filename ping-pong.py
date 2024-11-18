from pygame import *
from random import randint
from time import sleep

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed


win_width = 700
win_height = 700
window = display.set_mode((win_width, win_height))
display.set_caption("Ping_pong")
field = (180, 214, 214)
game = True
fps = 60
clock = time.Clock()
raketka_left = Player('raketka_left.png', 10, 350, 10, 16, 64)
raketka_right = Player('raketka_right.png', 674, 350, 10, 16, 64)
ball = GameSprite('ball.png', 350, 350, 10, 32, 32)
ball_speed_x = randint(-2, 2)
ball_speed_y = randint(-2, 2)
if ball_speed_x == 0:
    ball_speed_x = 1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(field)
    ball.rect.x += ball_speed_x
    ball.rect.y += ball_speed_y
    if ball.rect.y > 668 or ball.rect.y < 0:
        ball_speed_y *= -1
    if sprite.collide_rect(raketka_left, ball):
        ball_speed_x = randint(0, 5)
        ball_speed_y = randint(-5, 5)
    elif sprite.collide_rect(raketka_right, ball):
        ball_speed_x = randint(-5, 0)
        ball_speed_y = randint(-5, 5)
    ball.reset()
    raketka_right.update_right()
    raketka_right.reset()
    raketka_left.update_left()
    raketka_left.reset()
    display.update()
    clock.tick(fps)
    


    
