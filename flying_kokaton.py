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
    kk_rct = kk_img.get_rect()
    kk_rct.center = (300, 200)
    tmr = 0
    move_x, move_y = -1, 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            move_x, move_y = -1, -1  
        elif keys[pg.K_DOWN]:
            move_x, move_y = -1, 1  
        elif keys[pg.K_LEFT]:
            move_x, move_y = -1, 0  
        elif keys[pg.K_RIGHT]:
            move_x, move_y = 1, 0  
        elif not any(keys):  
            move_x, move_y = -1, 0  

        
        kk_rct.move_ip(move_x, move_y)
        x = -(tmr % 3200)
        screen.blit(bg_img, [x, 0]) # screen surfaceに背景画像surfaceを貼り付ける
        screen.blit(bg_img2, [x+1600, 0])
        screen.blit(bg_img, [x+3200, 0])
        screen.blit(bg_img2, [x+4000, 0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()