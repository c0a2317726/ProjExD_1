import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2= pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")#こうかとん画像の読み込みsurfaceを作成
    kk_img = pg.transform.flip(kk_img, True, False) #こうかとん左右反転
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 1600
        screen.blit(bg_img, [-x, 0]) # screen surfaceに背景画像surfaceを貼り付ける
        screen.blit(bg_img2, [800-x, 0])
        screen.blit(bg_img, [1600-x, 0])
        screen.blit(kk_img, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()