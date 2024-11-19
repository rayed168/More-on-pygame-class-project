import pygame as pg
pg.init()
screen=pg.display.set_mode((640,480))
WHITE=(0,0,0)
BLUE=(0,0,255)
screen.fill(WHITE)
while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
    pg.draw.rect(screen,BLUE,(280,200,100,50))
    pg.display.flip()        