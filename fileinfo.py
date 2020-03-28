# Sript name :fileinfo.py
# Author : nathaniel cheng
# created: 2019.1
# Last modified :
# version :1.0
# modifications :

#description :show file information for a given file

# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:18:19 2019

@author: Sun Cloud
"""

import pygame
from pygame.locals import *
import random
import sys
import numpy as np
import time
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("bg.mp3")
pygame.mixer.music.play(-1,0)
pygame.display.set_caption("perfect maze")
w0=False
pos_x=0
pos_y=25
vel_up=-2
vel_down=2
vel_left=-2
vel_right=2
up=False
down=False
left=False
right=False
draw=False
monster1=False
wall=[]
way=[]
back=False
blank=[]
wall0=[]
chosed=[]
wallpos=[]
road=[]
C=[]
passed=[]
roadpos=[]
r1=25
r2=25
screen = pygame.display.set_mode((r1*25,r2*25))
s=1
    
    
def restart():
    global roadpos,space,wallpos
    wall=[]
    way=[]
    blank=[]
    wall0=[]
    chosed=[]
    wallpos=[]
    road=[]
    C=[]
    passed=[]
    roadpos=[]
    space=np.zeros((r1,r2),dtype=np.uint8)
    for i in range(r1):
        for j in range(r2):
            if i % 2 ==1 and j % 2 ==1:
                blank.append([i,j])
                space[i][j]=1
            if (i %2 == 1 and j % 2 == 0) or (i %2 == 0 and j % 2 == 1) :
                pass
                if i != 0 and i != r1-1 and j !=0 and j !=r2-1:
                    wall0.append([i,j])
    a=random.choice(blank)
    chosed.append(a)
    for i in [-1,1]:
        x=a[0]
        y=a[1]
        x1=x+i
        y1=y+i
        p=[x,y1]
        q=[x1,y]
        if p in wall0:
            wall.append(p)
        if q in wall0:
            wall.append(q)
    while wall != []:
        w=random.choice(wall)
        if w[0] % 2 == 1:
            x0=w[0]
            y2=w[1]+1
            y3=w[1]-1
            room1=[x0,y2]
            room2=[x0,y3]
        elif w[0] % 2 ==0:
            y0=w[1]
            x2=w[0]+1
            x3=w[0]-1
            room1=[x2,y0]
            room2=[x3,y0]
        if room1 in chosed and room2 in chosed:
            wall.remove(w)
            continue
        else:
            space[w[0]][w[1]]=1
            wall.remove(w)
            if room1 in chosed:
                chosed.append(room2)
                for i in [-1,1]:
                    x4=room2[0]
                    y4=room2[1]
                    x5=x4+i
                    y5=y4+i
                    p1=[x4,y5]
                    q1=[x5,y4]
                    if p1 in wall0:
                        wall.append(p1)
                    if q1 in wall0:
                        wall.append(q1)
            elif room2 in chosed:
                chosed.append(room1)
                for i in [-1,1]:
                    x4=room1[0]
                    y4=room1[1]
                    x5=x4+i
                    y5=y4+i
                    p2=[x4,y5]
                    q2=[x5,y4]
                    if p2 in wall0:
                        wall.append(p2)
                    if q2 in wall0:
                        wall.append(q2)
    space[1][0]=1
    space[r1-2][r2-1]=1
    for i in range(r1):
        for j in range(r2):
            if space[i][j]==0:
                wallpos.append([25*j,25*i])
    for j in range(r1):
        for i in range(r2):
            if space[j][i]==1:
                way.append([i,j])
    road.append([0,1])
    passed.append([0,1])
    K=[]
    P=[]
    while True:
        K=[]
        for i in way:
            P=[]
            tong=0
            P.append([i[0]+1,i[1]])
            P.append([i[0]-1,i[1]])
            P.append([i[0],i[1]+1])
            P.append([i[0],i[1]-1])
            for ele in P:
                if ele in way:
                    tong=tong+1
            if i !=[0,1] and i != [r1-1,r2-2]:
                K.append(tong)
            if tong == 1 and (i !=[0,1] and i != [r1-1,r2-2]):
                way.remove(i)
        if 1 not in K:
            break


    while len(way) !=len(road):
        for ele in way:
            sta=road[-1]
            if ((sta[0]-ele[0]==0 and abs(sta[1]-ele[1])==1) or (sta[1]-ele[1]==0 and abs(sta[0]-ele[0])==1)) and ele not in passed:
                road.append(ele)
                passed.append(ele)
            
            
    for ele in road:
        i00=int(ele[0])*25+12.5
        i11=int(ele[1])*25+12.5
        roadpos.append((i00,i11))
    
def drawwall(x,y):
    color1=0,0,0
    x=int(x)
    y=int(y)
    pygame.draw.rect(screen,color1,(25*x,25*y,25,25),0)
def move():
    global up
    global down
    global left
    global right
    global pos_x
    global pos_y
    global vel_up
    global vel_cown
    global vel_left
    global vel_right
    if up:
        pos_y += vel_up
    if down:
        pos_y += vel_down
    if left:
        pos_x += vel_left
    if right:
        pos_x += vel_right
def crash():
    global k1,k2,k3,k4,r1
    global pos_x,pos_y,vel_up,vel_down,vel_left,vel_right,wallpos
    for walls in wallpos:
        if (walls[0]-pos_x<15 and walls[0]-pos_x>-25) and walls[1]-pos_y==15:
            k1=1
        if (walls[0]-pos_x<15 and walls[0]-pos_x>-25) and walls[1]-pos_y==-25:
            k2=1
        if (walls[1]-pos_y<15 and walls[1]-pos_y>-25) and walls[0]-pos_x==15:
            k3=1
        if (walls[1]-pos_y<15 and walls[1]-pos_y>-25) and walls[0]-pos_x==-25:
            k4=1
    if k1 ==1:
        vel_down=0
    if k2 ==1 :
        vel_up=0
    if k3 ==1 or pos_x==r1*25-15:
        vel_right=0
    if k4 ==1 or pos_x==0:
        vel_left=0

n9=0
def monster():
    global screen,r1,r2
    global n9,pos_x1,pos_x2,pos_x3,pos_x4,pos_y1,pos_y2,pos_y3,pos_y4,monsterpos
    global vel_x1,vel_x2,vel_x3,vel_x4,vel_y1,vel_y2,vel_y3,vel_y4
    monsterpos=[]
    if n9 ==0:
        pos_x1=random.randrange(0, 149,2)
        pos_x2=random.randrange(150,299,2)
        pos_x3=random.randrange(300,449,2)
        pos_x4=random.randrange(450,575,2)
        pos_y1=random.randrange(0,299,2)
        pos_y2=random.randrange(300,575,2)
        pos_y3=random.randrange(0,299,2)
        pos_y4=random.randrange(300,575,2)
        vel_x1 = 1.3
        vel_x2 = 2
        vel_x3 = -1
        vel_x4 = 1.8
        vel_y1 = -1.3
        vel_y2 = -2
        vel_y3 = 1
        vel_y4 = -1.8
        n9=1
    pos_x1 += vel_x1
    pos_x2 += vel_x2
    pos_x3 += vel_x3
    pos_x4 += vel_x4
    pos_y1 += vel_y1
    pos_y2 += vel_y2
    pos_y3 += vel_y3
    pos_y4 += vel_y4
    monsterpos.append([pos_x1,pos_y1])
    monsterpos.append([pos_x2,pos_y2])
    monsterpos.append([pos_x3,pos_y3])
    monsterpos.append([pos_x4,pos_y4])
    if pos_x1>r1*25-50 or pos_x1<0:
        vel_x1 = -vel_x1
    if pos_x2>r1*25-50 or pos_x2<0:
        vel_x2 = -vel_x2
    if pos_x3>r1*25-50 or pos_x3<0:
        vel_x3 = -vel_x3
    if pos_x4>r1*25-50 or pos_x4<0:
        vel_x4 = -vel_x4
    if pos_y1>r2*25-50 or pos_y1<0:
        vel_y1 = -vel_y1
    if pos_y2>r2*25-50 or pos_y2<0:
        vel_y2 = -vel_y2
    if pos_y3>r2*25-50 or pos_y3<0:
        vel_y3 = -vel_y3
    if pos_y4>r2*25-50 or pos_y4<0:
        vel_y4 = -vel_y4
    pos1=pos_x1,pos_y1,50,50
    pos2=pos_x2,pos_y2,50,50
    pos3=pos_x3,pos_y3,50,50
    pos4=pos_x4,pos_y4,50,50
    color=0,0,200
    width=0
    pygame.draw.rect(screen,color,pos1,width)
    pygame.draw.rect(screen,color,pos2,width)
    pygame.draw.rect(screen,color,pos3,width)
    pygame.draw.rect(screen,color,pos4,width)
    
def monstercrash():    
    global monsterpos,pos_x,pos_y
    for pos in monsterpos:
        if (pos[0]-pos_x<15 and pos[0]-pos_x>-50) and (pos[1]-pos_y<=15 and pos[1]-pos_y>=-50):
            pos_x=0
            pos_y=25
        if (pos[1]-pos_y<15 and pos[1]-pos_y>-50) and (pos[0]-pos_x<=15 and pos[0]-pos_x>=-50):
            pos_x=0
            pos_y=25
nn=0
def monstereasy():
    global screen
    global nn,pos_x5,pos_y5,monsterpos
    global vel_x5,vel_y5
    monsterpos=[]
    if nn ==0:
        pos_x5=random.randrange(100,501,2)
        pos_y5=random.randrange(100,501,2)
        vel_x5 = 2
        vel_y5 = -2
        nn=1
    pos_x5 += vel_x5
    pos_y5 += vel_y5
    monsterpos.append([pos_x5,pos_y5])
    if pos_x5>575 or pos_x5<0:
        vel_x5 = -vel_x5
    if pos_y5>575 or pos_y5<0:
        vel_y5 = -vel_y5
    pos5=pos_x5,pos_y5,50,50
    color=0,0,200
    width=0
    pygame.draw.rect(screen,color,pos5,width)

k8=0
def becover():    
    global k8,screen,r1,r12
    if k8==0:
        for i in range(95):
            i0= str(i).zfill(5)
            cover=pygame.image.load("IMG%s.png"%i0)
            pic = pygame.transform.scale(cover, (r1*25,r2*25))
            screen.blit(pic,(0,0))
            time.sleep(0.05)
            pygame.display.update()
            k8=1
    cover=pygame.image.load("IMG00095.png")
    pic = pygame.transform.scale(cover, (r1*25,r2*25))
    screen.blit(pic,(0,0))
def select():
    global screen,k8,click,pos_m,r1,r2
    bblue=0,67,110
    cover=pygame.image.load("IMG00095.png")
    pic = pygame.transform.scale(cover, (r1*25,r2*25))
    myfont = pygame.font.Font(None,60)
    text1 = myfont.render("EASY", True,bblue)
    text2 = myfont.render("NORMAL",True,bblue)
    text3 = myfont.render("HELL",True,bblue)
    screen.blit(pic,(0,0))
    screen.blit(text1, (250,100))
    screen.blit(text2, (225,250))
    screen.blit(text3, (250,400))
    if click[0]==1 and pos_m[1]<=220:
        k8=2
    if click[0]==1 and (pos_m[1]>220 and pos_m[1] <=400):
        k8=3
    if click[0]==1 and (pos_m[1]>400 and pos_m[1] <=625):
        k8=4
def win():
    global screen
    yellow=70,200,200
    myfont = pygame.font.Font(None,80)
    text4 = myfont.render("WIN!",True,yellow)
    screen.blit(text4, (248,250))
    
while True:
    if s==1:
        restart()
        s=0
    vel_up=-1
    vel_down=1
    vel_left=-1
    vel_right=1
    k1=0
    k2=0
    k3=0
    k4=0
    k5=0
    click=(0,0,0)
    if k8 != 1:
        back=False
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key==K_w:
                up=True
            elif event.key==K_s:
                down=True
            elif event.key==K_a:
                left=True
            elif event.key==K_d:
                right=True
            elif event.key==K_r:
                draw=True
            elif event.key==K_SPACE and w0==True:
                restart()
                back=True
            elif event.key==K_BACKSPACE:
                pos_x=0
                pos_y=25
                k8=1
        if event.type==KEYUP:
            if event.key==K_w:
                up=False
            elif event.key==K_s:
                down=False
            elif event.key==K_a:
                left=False
            elif event.key==K_d:
                right=False
            elif event.key==K_r:
                draw=False
        if event.type == MOUSEMOTION and (k8 == 1 or w0 ==True ):
            pos_m = pygame.mouse.get_pos()
            mx=pos_m[0]
            my=pos_m[1]
            click= pygame.mouse.get_pressed()
    if k8 == 0:
        becover()
    if k8 == 1:
        select()
    if k8 == 2:
        crash()
        move()
        color1=0,0,0
        screen.fill((255,255,255))
        color=255,0,0
        width=0
        pos=pos_x,pos_y,15,15
        pygame.draw.rect(screen,color,pos,width)
        if draw :
            pygame.draw.aalines(screen,(0,255,0),False,roadpos,10)
        for i in range(r1):
            for j in range(r2):
                if space[i][j]==0:
                    a=j
                    b=i
                    drawwall(a,b)
        if pos_x == r1*25-15:
            win()
            w0=True
    if k8 == 3:
        crash()
        move()
        color1=0,0,0
        screen.fill((255,255,255))
        color=255,0,0
        width=0
        pos=pos_x,pos_y,15,15
        pygame.draw.rect(screen,color,pos,width)
        if draw :
            pygame.draw.aalines(screen,(0,255,0),False,roadpos,10)
        monstereasy()
        if w0 == False:
            monstercrash()
        for i in range(r1):
            for j in range(r2):
                if space[i][j]==0:
                    a=j
                    b=i
                    drawwall(a,b)
        if pos_x == r1*25-15:
            win()
            w0=True
    if k8 == 4:
        crash()
        move()
        color1=0,0,0
        screen.fill((255,255,255))
        color=255,0,0
        width=0
        pos=pos_x,pos_y,15,15
        pygame.draw.rect(screen,color,pos,width)
        if draw :
            pygame.draw.aalines(screen,(0,255,0),False,roadpos,10)
        monster()
        if w0 ==False:
            monstercrash()
        for i in range(r1):
            for j in range(r2):
                if space[i][j]==0:
                    a=j
                    b=i
                    drawwall(a,b)
        if pos_x == r1*25-15:
            win()
            w0=True
    if w0:
        if back:
            pos_x=0
            pos_y=25
            k8=1
            w0=False
    pygame.display.update()