# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:10:15 2022

@author: unreal_num border
"""

import turtle
from tkinter import Tk
from tkinter.simpledialog import askinteger, askfloat, askstring
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfilename, askdirectory
from tkinter.messagebox import showinfo, showwarning, showerror

if __name__=="__main__":
    
    app = Tk()  #初始化GUI程序
    app.withdraw() #仅显示对话框，隐藏主窗口
    
    
    showinfo("你好！","欢迎来到海龟作画系统！")
    paintcolor=askstring("输入颜色(不输入默认为黑色)", "颜色")
    
    while 1:
        turtle.pencolor(paintcolor)
        turtle.hideturtle()
        shape1= askstring("请输入你想绘画什么？（目前只能画基本图形）",
                     prompt = "1. 圆形 2. 正方形 3. 矩形 4. 三角形（等边）")    
        if shape1=="圆形":
            r=askfloat("请输入圆的半径","半径")
            turtle.reset()
            turtle.pencolor(paintcolor)
            turtle.hideturtle()
            turtle.circle(r)
        elif shape1=="正方形":
            r=askfloat("请输入正方形的边长","半径")
            turtle.reset()
            turtle.pencolor(paintcolor)
            turtle.hideturtle()
            for i in range(0,4):
                turtle.forward(r)
                turtle.left(90)
        elif shape1=="矩形":
            turtle.reset()
            turtle.pencolor(paintcolor)
            turtle.hideturtle()
            a=askfloat("请输入矩形的长","长")
            b=askfloat("请输入矩形的宽","宽")
            for i in range(0,2):
                turtle.forward(a)
                turtle.left(90)
                turtle.forward(b)
                turtle.left(90)
        elif shape1=="等边三角形" or shape1=="三角形（等边）":
            turtle.reset()
            turtle.pencolor(paintcolor)
            turtle.hideturtle()
            r=askfloat("请输入三角形的边长","边长")
            for i in range(0,3):
                turtle.forward(r)
                turtle.left(120)
        judge=askstring("是否继续？","Y/N")
        turtle.reset()
        if judge=="N":
            break
    showinfo(title = "提示",
        message = "程序已运行结束!")
    app.destroy()
    turtle.bye()
        
    
    
    
    
