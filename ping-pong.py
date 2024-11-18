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
field = (120, 255, 120)
game = True
fps = 60
clock = time.Clock()
raketka_left = Player('raketka_left.png', 10, 350, 10, 16, 64)
raketka_right = Player('raketka_right.png', 674, 350, 10, 16, 64)
# ball = GameSprite()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill(field)
    raketka_right.update_right()
    raketka_right.reset()
    raketka_left.update_left()
    raketka_left.reset()
    display.update()
    clock.tick(fps)
    


    


    
