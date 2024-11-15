from pygame import *
from random import randint
from time import sleep

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Raketka_right(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
class Raketka_left(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
win_width = 500
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping_pong")
field = (255, 120, 255)
window.fill(field)
game = True
fps = 60
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(fps)
    


    
