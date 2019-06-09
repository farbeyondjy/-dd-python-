import sys
import pygame
import random


pygame.init()
size=width,height=1500,700
screen=pygame.display.set_mode(size)
hellokitty = pygame.image.load("caixukun.jpg")
ball = [pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg"),pygame.image.load("ball.jpg")]
fail = pygame.image.load("fail.jpg")
hellokittyrect = hellokitty.get_rect()
failrect= fail.get_rect()
ballrect=[ball[0].get_rect(),ball[1].get_rect(),ball[2].get_rect(),ball[3].get_rect(),ball[4].get_rect(),ball[5].get_rect(),ball[6].get_rect(),ball[7].get_rect(),ball[8].get_rect(),ball[9].get_rect(),ball[10].get_rect(),ball[11].get_rect(),ball[12].get_rect(),ball[13].get_rect(),ball[14].get_rect()]
clock=pygame.time.Clock()
color=(255,255,255)
x=0
y=0
ok=0
k1=0
speed=[x,y]
speed2=[0,5]
ballspeed=[random.uniform(1,10),random.uniform(1,10),random.uniform(1,10),random.uniform(1,10),random.uniform(1,10),random.uniform(1,10),random.uniform(1,10),random.uniform(1,10),random.uniform(1,10),random.uniform(1,10),random.uniform(1,10),random.uniform(1,10),random.uniform(1,10),random.uniform(1,10),random.uniform(1,10)]
judge=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hellokittyrect.centerx=500
hellokittyrect.centery=500


for i in range(0,14,1):
    ballrect[i].centerx=random.uniform(0,1500)
    ballrect[i].centery=-200

while True:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_DOWN]==1:
        y=10

    if key[pygame.K_RIGHT]:
        x=10

    if key[pygame.K_UP]:
        y=-10

    if key[pygame.K_LEFT]:
        x=-10

    if key[pygame.K_DOWN] != 1 and key[pygame.K_UP] != 1:
            y = 0
    if key[pygame.K_RIGHT] != 1 and key[pygame.K_LEFT] != 1:
            x = 0
    if x!=0 and y!=0:
        x=x*7/10
        y=y*7/10



    speed=[x,y]
    hellokittyrect = hellokittyrect.move(speed)
    screen.fill(color)
    screen.blit(hellokitty, hellokittyrect)
    for i in range(0, 14, 1):
        speed2=[0,ballspeed[i]]
        if judge[i]==1:
            ballrect[i].centerx=random.uniform(0,1500)
            ballrect[i].centery=-200
            ballspeed[i]=random.uniform(5,10)
            judge[i]=0
        ballrect[i] = ballrect[i].move(speed2)
        screen.blit(ball[i], ballrect[i])
        if ballrect[i].centery>850:
            judge[i]=1

    for i in range(0,14,1):
        if (hellokittyrect.centerx)-(ballrect[i].centerx)<=85 and (hellokittyrect.centerx)-(ballrect[i].centerx)>=-85 and (hellokittyrect.centery)-(ballrect[i].centery)<=70 and (hellokittyrect.centery)-(ballrect[i].centery)>=-70:
            screen.blit(fail, (500, 200))
            screen.blit(fail, (0,0))
            screen.blit(fail, (1000,400))
            ok=1
    if ok==1:
        break
    pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.fill(color)
    screen.blit(fail, (500, 200))
    screen.blit(fail, (0,0))
    screen.blit(fail, (1000,400))
    pygame.display.flip()
