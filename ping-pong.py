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
count_win = [0, 0]
font.init()
font = font.Font(None, 35)
window = display.set_mode((win_width, win_height))
display.set_caption("Ping_pong")
bg_colors = [randint(0, 255), randint(0, 255), randint(0, 255)]
bg_colors_fin = [randint(0, 255), randint(0, 255), randint(0, 255)]
field = (bg_colors[0], bg_colors[1], bg_colors[2])
game = True
finish = False
fps = 60
clock = time.Clock()


raketka_left = Player('raketka_left.png', 10, 350, 10, 16, 64)
raketka_right = Player('raketka_right.png', 674, 350, 10, 16, 64)
ball = GameSprite('ball.png', 350, 350, 10, 32, 32)

ball_speed_y = randint(-2, 2)
if randint(0, 1) == 0:
    ball_speed_x = 2
else:
    ball_speed_x = -2
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        if bg_colors[0] != bg_colors_fin[0]:
            if bg_colors[0] > bg_colors_fin[0]:
                bg_colors[0] = max(bg_colors[0] - 1, 0)  # Убедитесь, что значение не меньше 0
            else:
                bg_colors[0] = min(bg_colors[0] + 1, 255)  # Убедитесь, что значение не больше 255
        if bg_colors[1] != bg_colors_fin[1]:
            if bg_colors[1] > bg_colors_fin[1]:
                bg_colors[1] = max(bg_colors[1] - 1, 0)
            else:
                bg_colors[1] = min(bg_colors[1] + 1, 255)
        if bg_colors[2] != bg_colors_fin[2]:
            if bg_colors[2] > bg_colors_fin[2]:
                bg_colors[2] = max(bg_colors[2] - 1, 0)
            else:
                bg_colors[2] = min(bg_colors[2] + 1, 255)
        else:
            bg_colors_fin = [randint(0, 255), randint(0, 255), randint(0, 255)]
        field = (bg_colors[0], bg_colors[1], bg_colors[2])
        window.fill(field)
        window.blit(font.render(str(count_win[0]) + ' - ' + str(count_win[1]), True, (0, 0, 0)), (325, 30))
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y
        if ball.rect.y > 668 or ball.rect.y < 0:
            ball_speed_y *= -1
        if sprite.collide_rect(raketka_left, ball):
            ball_speed_x = abs(ball_speed_x)+1
            ball_speed_y = randint(0-abs(ball_speed_x), abs(ball_speed_x))
        elif sprite.collide_rect(raketka_right, ball):
            ball_speed_x = 0 - ball_speed_x - 1
            ball_speed_y = randint(0-abs(ball_speed_x), abs(ball_speed_x))
        if ball.rect.x > 668 or ball.rect.x < 0:
            if ball.rect.x > 668:
                count_win[0] += 1
            else:
                count_win[1] += 1
            ball.rect.x = 350
            ball.rect.y = 350
            ball_speed_y = randint(-2, 2)
            if randint(0, 1) == 0:
                ball_speed_x = 2
            else:
                ball_speed_x = -2
        if count_win[0] == 5:
            text_surface = font.render("Выиграл левый", True, (255, 255, 255))
            window.blit(text_surface, (100, 200))
            finish = True
        elif count_win[1] == 5:
            text_surface = font.render("Выиграл правый", True, (255, 255, 255))
            window.blit(text_surface, (350, 200))
            finish = True





    ball.reset()
    raketka_right.update_right()
    raketka_right.reset()
    raketka_left.update_left()
    raketka_left.reset()
    display.update()
    clock.tick(fps)

print(bg_colors)

    
