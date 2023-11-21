import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01proen/fig/pg_bg.jpg")#背景画像練習1

    kk_img = pg.image.load("ex01proen/fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 0,1.0),pg.transform.rotozoom(kk_img, 1,1.0),pg.transform.rotozoom(kk_img, 2,1.0),pg.transform.rotozoom(kk_img, 3,1.0),pg.transform.rotozoom(kk_img, 4,1.0),pg.transform.rotozoom(kk_img, 5,1.0),pg.transform.rotozoom(kk_img, 6,1.0),pg.transform.rotozoom(kk_img, 7,1.0),pg.transform.rotozoom(kk_img, 8,1.0),pg.transform.rotozoom(kk_img, 9,1.0),pg.transform.rotozoom(kk_img, 10,1.0)]

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        

        x=tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(pg.transform.flip(bg_img,True,False),[1600-x,0])
        screen.blit(bg_img,(3200-x,0))
        screen.blit(kk_imgs[tmr%10],[300,200])
       

              
        pg.display.update()
        tmr += 1        
        clock.tick(400)
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()