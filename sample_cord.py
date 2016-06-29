from Tkinter import *

def move():
    global Dx,Dy
    x1,y1,x2,y2=w.coords(id1)
    print x1, y1, x2, y2
    if x1+Dx<=0 or x1+Dx>=190:
        Dx=-Dx
    if y1+Dy<=0 or y1+Dy>=190:
        Dy=-Dy
    newx1 = x1+ Dx
    newx2 = x2 + Dx
    newy1 = y1 + Dy
    newy2 = y2 + Dy
    print " new value {} {} {} {} {} {}".format(
        x1, y1, x2, y2, Dx, Dy
    )
    w.coords(id1,newx1,newy1,newx2,newy2)
    root.after(50,move)


root=Tk()
w = Canvas(root, width=200, height=200,
           borderwidth=0,
           highlightthickness=0,
           background='white')
w.pack(padx=10,pady=10)
button1=Button(root,text='Move')
button1.pack()
button1.bind('<Button-1>',move)
Dx=1
Dy=1
id1=w.create_line(3,7,3+10,7+10, fill='green')
print id1
root.after(50,move)
root.mainloop()