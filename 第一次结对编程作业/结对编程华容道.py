

#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import simpleguitk as simplegui
import random
from tkinter import messagebox
import tkinter
from multiprocessing import Queue

import os
import sys
import PySide2

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

from enum import IntEnum
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QGridLayout, QMessageBox
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtCore import Qt


from PIL import Image
import matplotlib.pyplot as plt
 
byamax = simplegui.load_image('a_.jpg')

 
WIDTH = 900
HEIGHT = WIDTH+104
 
IMAGE_SIZE = WIDTH/3

width = 600
image_size = 200
height = width+100
frame = simplegui.create_frame('华容道',width,height)

all_coordinates = [[IMAGE_SIZE*0.5, IMAGE_SIZE*0.5], [IMAGE_SIZE*1.5, IMAGE_SIZE*0.5],
                        [IMAGE_SIZE*2.5, IMAGE_SIZE*0.5], [IMAGE_SIZE*0.5, IMAGE_SIZE*1.5],
                        [IMAGE_SIZE*1.5, IMAGE_SIZE*1.5], [IMAGE_SIZE*2.5, IMAGE_SIZE*1.5],
                        [IMAGE_SIZE*0.5, IMAGE_SIZE*2.5], [IMAGE_SIZE*1.5, IMAGE_SIZE*2.5], None]

win_coordinates = [[IMAGE_SIZE*0.5, IMAGE_SIZE*0.5], [IMAGE_SIZE*1.5, IMAGE_SIZE*0.5],
                        [IMAGE_SIZE*2.5, IMAGE_SIZE*0.5], [IMAGE_SIZE*0.5, IMAGE_SIZE*1.5],
                        [IMAGE_SIZE*1.5, IMAGE_SIZE*1.5], [IMAGE_SIZE*2.5, IMAGE_SIZE*1.5],
                        [IMAGE_SIZE*0.5, IMAGE_SIZE*2.5], [IMAGE_SIZE*1.5, IMAGE_SIZE*2.5], None]

match_array = [0,1,2,3,4,5,6,7,8]
match_map = [[0,1,2],
             [3,4,5],
             [6,7,8]]

board_coordinates = [[None,None,None],[None,None,None],[None,None,None]]

ROWS = 3
COLS = 3
steps = 0
board = [[None,None,None],[None,None,None],[None,None,None]]

class Square:
    def __init__(self,coordinage):
        self.center = coordinage
    def draw(self,canvas,board_pos):    #画出随机出来的九宫格图
        canvas.draw_image(byamax,self.center,[IMAGE_SIZE,IMAGE_SIZE],
                          [(board_pos[1]+0.5)*image_size,(board_pos[0]+0.5)*image_size],[image_size,image_size])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

class Node(object):
    class Struct(object):
        def __init__(self,x,y,step,mapp,array):
            self.array = array
            self.array[0][step] = x
            self.array[1][step] = y
            self.x = x
            self.y = y
            self.step = step
            self.mapp = mapp    #用于hash
            self.hash = 0
            for i in range(3):
                for j in range(3):
                    self.hash = self.hash * 10 + mapp[i][j]
            self.temp = 0

        def swap(self,x1,y1,x2,y2):
            self.temp = self.mapp[x1][y1]
            self.mapp[x1][y1] = self.mapp[x2][y2]
            self.mapp[x2][y2] = self.temp

    def make_struct(self,x,y,step,mapp,array):
        return self.Struct(x,y,step,mapp,array)

def check_right():
    global match_array
    sum = 0
    for i in range(9):
        if match_array[i] == 8:
            continue
        for j in range(9):
            if match_array[j] == 8:
                continue
            if j <= i:
                continue
            if match_array[i] > match_array[j]:
                sum += 1
    if sum%2 == 0:
        return True
    return False

def init_board():
    global match_array
    global match_map
    #确保随机生成的华容道可以还原成原来的图片
    while(True):
        random.shuffle(match_array)
        if check_right():
            break
    
    for i in range(9):
        i1 = (int)(i / 3)
        i2 = i % 3
        match_map[i1][i2] = match_array[i]

    for i in range(ROWS):
        for j in range(COLS):
            idx = match_map[i][j]
            square_center = all_coordinates[idx]
            board_coordinates[i][j] = square_center
            if square_center is None:
                board[i][j] = None
            else:
                board[i][j] = Square(square_center)


def play_game():
    frame.set_draw_handler(draw)    #画图
    global steps
    steps = 0
    init_board()

def draw(canvas):
    
    flag = False

    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] is not None:
                flag = True
                board[i][j].draw(canvas,[i,j])
            
    if flag is True:
        canvas.draw_image(byamax,[WIDTH/2,WIDTH/2],[WIDTH,WIDTH],[52,width+52],[100,100])     #画出原图，便于玩家看着原图还原拼图
        canvas.draw_text('步数：'+ str(steps),[400,680],22,'white')


def keyPressEvent(key):
    global match_map
    global steps
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] is None:
                xx = i
                yy = j
    board1 = board[xx][yy]
    board2 = match_map[xx][yy]
    if(key == Qt.Key_A and yy >= 1):
        board[xx][yy] = board[xx][yy - 1]
        board[xx][yy - 1] = board1
        match_map[xx][yy] = match_map[xx][yy - 1]
        match_map[xx][yy - 1] = board2
        steps += 1
    if(key == Qt.Key_D and yy <= 1):
        board[xx][yy] = board[xx][yy + 1]
        board[xx][yy + 1] = board1
        match_map[xx][yy] = match_map[xx][yy + 1]
        match_map[xx][yy + 1] = board2
        steps += 1
    if(key == Qt.Key_W and xx >= 1):
        board[xx][yy] = board[xx - 1][yy]
        board[xx - 1][yy] = board1
        match_map[xx][yy] = match_map[xx - 1][yy]
        match_map[xx - 1][yy] = board2
        steps += 1
    if(key == Qt.Key_S and xx <= 1):
        board[xx][yy] = board[xx + 1][yy]
        board[xx + 1][yy] = board1
        match_map[xx][yy] = match_map[xx + 1][yy]
        match_map[xx + 1][yy] = board2
        steps += 1
    frame.set_draw_handler(draw)
    flag = True
    last = -1
    for i in range(ROWS):
        for j in range(COLS):
            if last > match_map[i][j]:
                flag = False
            last = match_map[i][j]
    if flag is True:
        message = "你过关了,你的通关步数为: " + (str)(steps) + "步"
        messagebox.showinfo("提示",message)
        frame.set_canvas_background('brown')
        frame.set_draw_handler(draw)
        frame.start()

def delay():
    kk = 0
    while kk >= 1000000:
        kk += 1


def bfs(sx,sy,mapp):
    array = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    end = 12345678
    QQ = Queue()
    S = set()
    Q = Queue()
    node = Node()
    temp = node.make_struct(sx,sy,0,mapp,array)
    Q.put(temp)
    step = -1
    while Q.qsize() > 0:
        
        temp = Q.get()
        print(temp.mapp," ",temp.step)
        ttx = -1
        tty = -1
        for i in range(3):
            for j in range(3):
                if temp.mapp[i][j] == 8:
                    ttx = i
                    tty = j
        print(temp.mapp[ttx][tty])        
        i = 0
        for i in range(4):
            tx = ttx + dx[i]
            ty = tty + dy[i]
            print(tx," ",ty," ",ttx," ",tty," ",temp.mapp[tx][ty]," ",temp.mapp[ttx][tty])
            if tx > 2 or tx < 0 or ty > 2 or ty < 0:
                continue
            test = node.make_struct(tx , ty , temp.step + 1 , temp.mapp , temp.array)
            print(temp.mapp)
            test.swap(tx , ty , ttx , tty)
            print(test.mapp)
            print("HH")
            if test.hash == end:
                temp = test
                array = test.array
                step = temp.step
                break
            if test.hash in S:
                continue
            else:
                S.add(test.hash)
                Q.put(test)
        if step != -1:
            break

    print(temp.array)
    print(temp.hash)
    print(temp.mapp)
    print(temp.step)
    print(temp.x," ",temp.y)
    global steps
    global board
    steps = 0
    temp = QQ.get()
    print(temp)
    for i in range(step):
        #delay()
        print(array[0][i]," ",array[1][i])
        tp = board[array[i][0]][array[i][1]]
        board[array[0][i]][array[1][i]] = board[array[0][i + 1]][array[1][i + 1]]
        board[array[0][i + 1]][array[1][i + 1]] = tp
        steps += 1
        frame.set_draw_handler(draw)
        

    return


num = 0
def PIEvent():
    getimage()
    frame.set_keydown_handler(keyPressEvent)
    play_game()

def AIEvent():
    getimage()
    global match_map
    print(match_map)
    for i in range(3):
        for j in range(3):
            if match_map[i][j] == 8:
                print(i," ",j)
                bfs(i,j,match_map)
                break
    
def getimage():
    global num
    global byamax
    if num == 0:
        byamax = simplegui.load_image('a_.jpg')   
    if num == 1:
        byamax = simplegui.load_image('B_.jpg')  
    if num == 2:
        byamax = simplegui.load_image('U_.jpg')  

def Repeat():
    getimage()
    frame.set_canvas_background('brown')
    frame.set_draw_handler(draw)
    play_game()

def Next():
    global num
    num += 1
    getimage()
    play_game()


if __name__ == "__main__":
    frame.set_canvas_background('brown')
    
    frame.add_button('开始游戏',Repeat,60)
    frame.add_button('重新开始',Repeat,60)
    frame.add_button('过关步骤',AIEvent,60)
    frame.add_button('进入下一关',Next,60)
    frame.add_button('退出游戏',exit,60)

    frame.set_keydown_handler(keyPressEvent)

    frame.start()

    