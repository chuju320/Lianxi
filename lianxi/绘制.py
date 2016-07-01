#-*-coding:utf-8-*-
from Tkinter import *

back = list()
gridBack = list()
window = Tk()
frame1 = Frame(window,width=300,height=600,bg="black")
frame1.place(x=20,y=30)
canvas = Canvas(frame1,width=300,height=600,bg="black")
def init():

    for i in range(0,20):

      back.insert(i,list())
      gridBack.insert(i,list())

    for i in range(0,20):
      for j in range(0,10):
        back[i].insert(j,0)
        gridBack[i].insert(j,canvas.create_rectangle(30*j,30*i,30*(j+1),30*(i+1),fill="black"))
    canvas.pack()
    window.mainloop()

init()