import pygame
from pygame.locals import(
    K_a,
    K_d,
    QUIT,
    KEYUP,
    K_w,
    K_s,
    K_ESCAPE)
from random import randint
from ranking import rank
from time import sleep
from tkinter import Tk, messagebox

pygame.init()

# Time
FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (168, 168, 168)

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(GRAY)
pygame.display.set_caption("小车游戏")

# Mouse
pygame.mouse.set_visible(False)

# Sound
bgm = pygame.mixer.Sound("Bad.mp3")
enginesound = pygame.mixer.Sound("Engine.wav")
channel = bgm.play()
def sound_init():
    global bgm, channel
    bgm.play()
    bgm.set_volume(0.6)
    channel.set_volume(0.5)

# Tkinter Initialization
class tkinit(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.withdraw()
tkinit()

# Sprites
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global score, E2
        self.rect.move_ip(0, 10)
        end_1 = self.rect.colliderect(E2.rect)
        end_2 = (self.rect.bottom > 600)
        if end_1 or end_2:
            if end_2:score += 1
            self.rect.top = 0
            self.rect.center = (randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Hole(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Hole.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        global speed
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_w]:self.rect.move_ip(0, -speed)
        if (self.rect.bottom < 600):
            if pressed_keys[K_s]:self.rect.move_ip(0,speed)

        if self.rect.left - speed > 0 and pressed_keys[K_a]:
            self.rect.move_ip(-speed, 0)
        elif pressed_keys[K_a]:
            self.rect.left = 0
        if self.rect.left < SCREEN_WIDTH - 40 and pressed_keys[K_d]:
            self.rect.move_ip(speed, 0)
        elif pressed_keys[K_d]:
            self.rect.left = SCREEN_WIDTH - 40

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Star.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global speed, P1
        self.rect.move_ip(0, 5)
        end_1 = (self.rect.bottom > 600)
        end_2 = self.rect.colliderect(P1.rect)
        if end_2 or end_1:
            speed += randint(1, 2) * int(end_2)
            self.rect.top = 0
            self.rect.center = (randint(30, 370), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Heart.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global lives, P1
        self.rect.move_ip(0, 4)
        end_1 = (self.rect.bottom > 600)
        end_2 = self.rect.colliderect(P1.rect)
        if end_2 or end_1:
            if end_2 and lives < 10:
                lives = 10
            self.rect.top = 0
            self.rect.center = (randint(30, 370), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Score.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global score, P1
        self.rect.move_ip(0, 5)
        end_1 = (self.rect.bottom > 600)
        end_2 = self.rect.colliderect(P1.rect)
        if end_2 or end_1:
            score += 100 * int(end_2)
            self.rect.top = 0
            self.rect.center = (randint(30, 370), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Initialize sprites
P1 = Player()
S1 = Star()
S2 = Score()
E1 = Enemy()
E2 = Hole()
H1 = Heart()
# Initialize variables
speed = 5
running = True
score = 0
lives = 10
font = pygame.font.SysFont('Times', 30)

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYUP:
            running = not event.key == K_ESCAPE
            if event.key == K_w or event.key == K_s or event.key == K_a or event.key == K_d:
                enginesound.play()
            else:
                enginesound.stop()

    if not pygame.mixer.get_busy():
        sound_init()
    
    P1.update()# Move
    E1.move()
    E2.move()
    S1.move()
    S2.move()
    H1.move()

    DISPLAYSURF.fill(GRAY)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    E2.draw(DISPLAYSURF)
    S1.draw(DISPLAYSURF)
    S2.draw(DISPLAYSURF)
    H1.draw(DISPLAYSURF)

    if P1.rect.colliderect(E1.rect):
        lives -= 0.1
    if P1.rect.colliderect(E2.rect):
        lives = 0
    if lives <= 0:
        DISPLAYSURF.fill(RED)
        text = font.render("GAME\nOVER", False, BLACK, BLUE)
        DISPLAYSURF.blit(text, (100, 300))
        lives = 0
        running = False

    text = font.render(str(score), True, BLUE, GREEN)
    DISPLAYSURF.blit(text, (0, 0))
    text = font.render(str(lives), True, GREEN, RED)
    DISPLAYSURF.blit(text, (370, 0))
    text = font.render(str(speed), True, RED, BLUE)
    DISPLAYSURF.blit(text, (100, 0))

    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.mixer.fadeout(5000)
if lives <= 0:sleep(5)
    
pygame.quit()
messagebox.showinfo("Game Over", f"Your score is {score} and your rank is {rank(score)}")
