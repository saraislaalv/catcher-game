import pygame as pg
import sys
import random

# Konstanter
WIDTH = 400
HEIGHT = 700

# Størrelsen til vinduet
SIZE = (WIDTH, HEIGHT)

# Frames per second (bilder per sekund)
FPS = 60

# Farger
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
GRAY = (65,65,65)
LIGHTBLUE = (173,216,230)

# Initierer pygame
pg.init()

# Lager overflate (surface) vi kan tegne på
surface = pg.display.set_mode(SIZE)

# Lager en klokke
clock = pg.time.Clock()

# Variabel som styrer om spillet skal kjøres
run = True
game= True
# Verdier for spilleren
w=60 #bredde
h=80 #høyde

x= WIDTH//2
y= HEIGHT-h-10

# Henter bilde til spilleren
player_img = pg.image.load('bucket.png')

#Henter bakgrunnsbilde
background_img=pg.image.load('background_snow_2-3.png')
# Tilpasser bakgrunnsbilde til vår skjermstørrelse
background_img = pg.transform.scale(background_img, SIZE)

# Henter font
font = pg.font.SysFont('Arial', 26)

# Funksjonn som viser antall poeng
def display_points(poeng):
    text_img = font.render(f"Antall poeng:{poeng}", True, GRAY)
    if game is False:
        text_img = font.render(f"", True, GRAY)
    surface.blit(text_img, (20,20))
    
def loss(poeng):
    text_img = font.render(f"Du tapte! Du fikk {poeng} poeng.", True, GRAY)
    surface.blit(text_img, (50,200))

class Ball:
    def __init__ (self):
        self.r = 10
        self.x = random.randint(0, WIDTH)
        self.y = -self.r
        self.tall = 0
        
    def update(self):
        self.y += 5
    
    def draw(self):
        pg.draw.circle(surface, WHITE, (self.x,self.y), self.r)
        
# Lager et ballobjekt
ball= Ball()

poeng=0

while run:
    while game:
        #Sørger for at løkken kjører i korrekt hastighet
        clock.tick(FPS)
    
        #Går gjennom hendelser (events)
        for event in pg.event.get():
            #Sjekker om vi ønsker å lukke vinduet
            if event.type == pg.QUIT:
                run=False
    
        #Fyller skjermen med bakgrunnsbildet
        surface.blit(background_img,(0,0))
    
        vx=0
    
        #Henter tastene fra tastaturet som klikkes på
        keys = pg.key.get_pressed()
    
    
        # Sjekker om ulike taster trykkes på
        if keys[pg.K_LEFT] and x>0:
            vx=-5
            
        elif keys[pg.K_RIGHT] and x<WIDTH-w:
            vx=5
    
        #Oppdaterer posisjonen til rektangelet
        x+=vx
    
        # Ball
        ball.update()
        ball.draw()
    
        if ball.y > y and x < ball.x < x+w:
            poeng+=1
            ball = Ball()
    
        if ball.y + ball.r > HEIGHT:
            game = False
    
        # Spiller
        surface.blit(player_img, (x,y))
    
        
        display_points(poeng)
        
        # Flipper displayet for å vise hva vi har tegnet
        pg.display.flip()
        
    loss(poeng)
    
    # Flipper displayet for å vise hva vi har tegnet
    pg.display.flip()
    #Går gjennom hendelser (events)
    for event in pg.event.get():
        #Sjekker om vi ønsker å lukke vinduet
        if event.type == pg.QUIT:
            run=False
            

pg.quit()
sys.exit()
