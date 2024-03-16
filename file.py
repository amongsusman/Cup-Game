import pygame
import os
import random
import time
import math

pygame.init()

#constants
WIDTH, HEIGHT = 800, 800
BALL_WIDTH, BALL_HEIGHT = 200, 200
CUP_WIDTH, CUP_HEIGHT = 500, 500
TABLE_WIDTH, TABLE_HEIGHT = 1000, 1000
FPS = 60
BALL_ARR = [210, 390, 570]

#images 
BALL_IMG = pygame.image.load(os.path.join('unfair', 'ball.png'))
BALL = pygame.transform.scale(BALL_IMG, (BALL_WIDTH, BALL_HEIGHT))
CUP_IMG = pygame.image.load(os.path.join('unfair', 'cup.png'))
CUP = pygame.transform.scale(CUP_IMG, (CUP_WIDTH, CUP_HEIGHT))
TABLE_IMG = pygame.image.load(os.path.join('unfair', 'table.png'))
TABLE = pygame.transform.scale(TABLE_IMG, (TABLE_WIDTH, TABLE_HEIGHT))

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Unfair Game")

class ObjectInterface():
    def __init__(self, xpos, ypos, img):
        self.xpos = xpos
        self.ypos = ypos
        self.img = img
    def update(self, x, y):
        window.blit(self.img, (x, y))
    def getXpos(self):
        return self.xpos
    def getYpos(self):
        return self.ypos
    def changeXpos(self, amount):
        self.xpos += amount
    def changeYpos(self, amount):
        self.ypos += amount

class Ball(ObjectInterface):
    pass

class Cup(ObjectInterface):
    def __init__(self, xpos, ypos, img, dir):
        super().__init__(xpos, ypos, img)
        self.dir = dir
    def setXpos(self, new):
        self.xpos = new
    def getDir(self):
        return self.dir
    def changeDir(self):
        self.dir *= -1
    def isAtBorder(self):
        if self.getXpos() < 170:
            self.changeDir()
        elif self.getXpos() > 540:
            self.changeDir()
    def checkCollision(self):
        if self.getYpos() > 366:
            self.ypos = 366
            return True
        return False

class Table(ObjectInterface):
    pass

def draw_window(ball, cups, table, float, pos):
    window.fill(BLACK)
    table.update(table.getXpos(), table.getYpos())
    if float:
        ball.update(BALL_ARR[pos], 450)
    for cup in cups:
        cup.update(cup.getXpos(), cup.getYpos())
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    clock.tick(FPS)
    run = True
    roll = False
    up = False
    i = None 
    j = None
    canGen = True
    check1 = False
    check2 = False
    cup1b = False
    cup2b = False
    cup3b = False
    ac1 = False
    ac2 = False
    ac3 = False
    rolls = 0
    amount2 = -10
    canFloat = False
    ok = False
    pos = 0
    ball = Ball(210, 450, BALL)
    # cupx + 30, cupy + 85
    cup1 = Cup(180, 366, CUP, 3)
    cup2 = Cup(360, 366, CUP, 3)
    cup3 = Cup(540, 366, CUP, 3)
    table = Table(175, 480, TABLE)
    cups = [cup1, cup2, cup3]
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if canGen:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            if i == j:
                if (j == 2):
                    j = 1
                else:
                    j = i + 1
            temp1 = cups[i].getXpos()
            temp2 = cups[j].getXpos()
            roll = True
            canGen = False
        if roll:
            if cups[i].getXpos() != temp2:
                if temp1 < temp2:
                    cups[i].changeXpos(3)
                else:
                    cups[i].changeXpos(-3)
            else:
                check1 = True

            if cups[j].getXpos() != temp1:
                if temp2 < temp1:
                    cups[j].changeXpos(3)
                else:
                    cups[j].changeXpos(-3)
            else:
                check2 = True
            
            if check1 and check2:
                roll = False
                canGen = True
                check1 = False
                check2 = False
                rolls += 1
        
        if rolls == 5:
            canGen = False
            up = True
            rolls = 0

        if up:
            amount2 = -20
            canFloat = True
            up = False
        if canFloat:
            if pygame.mouse.get_pressed()[0] == True:
                if 180 < pygame.mouse.get_pos()[0] < 280 and 370 < pygame.mouse.get_pos()[1] < 490 and not ok:
                    ac1 = True
                elif 360 < pygame.mouse.get_pos()[0] < 460 and 370 < pygame.mouse.get_pos()[1] < 490 and not ok:
                    ac2 = True
                elif 540 < pygame.mouse.get_pos()[0] < 640 and 370 < pygame.mouse.get_pos()[1] < 490 and not ok:
                    ac3 = True
            if ac1:
                ok = True
                if cup1.getXpos() == 180:
                    cup1.changeYpos(amount2)
                    cup1b = True
                elif cup2.getXpos() == 180:
                    cup2.changeYpos(amount2)
                    cup2b = True
                else:
                    cup3.changeYpos(amount2)
                    cup3b = True
                pos = 0
                amount2 += 0.8
            elif ac2:
                ok = True
                if cup1.getXpos() == 360:
                    cup1.changeYpos(amount2)
                    cup1b = True
                elif cup2.getXpos() == 360:
                    cup2.changeYpos(amount2)
                    cup2b = True
                else:
                    cup3.changeYpos(amount2)
                    cup3b = True
                pos = 1
                amount2 += 0.8
            elif ac3:
                ok = True
                if cup1.getXpos() == 540:
                    cup1.changeYpos(amount2)
                    cup1b = True
                elif cup2.getXpos() == 540:
                    cup2.changeYpos(amount2)
                    cup2b = True
                else:
                    cup3.changeYpos(amount2)
                    cup3b = True
                pos = 2
                amount2 += 0.8
            print(pos)
            if cup1b and cup1.checkCollision():
                cup1b = False
                canFloat = False
                canGen = True
                ok = False
                ac1 = False
                ac2 = False
                ac3 = False
            elif cup2b and cup2.checkCollision():
                cup2b = False
                canFloat = False
                canGen = True
                ac1 = False
                ok = False
                ac2 = False
                ac3 = False
            elif cup3b and cup3.checkCollision():
                cup3b = False
                canFloat = False
                canGen = True
                ok = False
                ac1 = False
                ac2 = False
                ac3 = False
        draw_window(ball, cups, table, canFloat, pos)
    pygame.quit()

if __name__ == "__main__":
    main()