# -*- coding:utf-8 -*-
"""
# @project : spider
# @Time : 2019/8/8 14:07
# @FileName : aiheart.py
# @Author : 摩登老师
# @在线教育机构 : 扣丁学堂
# @个人学习公众号(bilibili) : 猫在大神旁的小C
"""
import turtle
import time

# 曲线移动
def curveMove():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

# 画心
def drawHeart():
    turtle.title("Welcome to my class")
    turtle.speed(10)
    turtle.pensize(2)
    turtle.color("red","pink")
    turtle.begin_fill()
    turtle.left(140) # 逆时针旋转140
    turtle.forward(111.65)
    curveMove() # 继续画曲线
    turtle.left(120)
    curveMove()  # 继续画曲线
    turtle.forward(111.65)
    turtle.end_fill()
    turtle.write("摩登，摩登，指路明灯!!!", font=("华文行楷", 20, "italic"))
    time.sleep(10)

if __name__ == "__main__":
    drawHeart()
