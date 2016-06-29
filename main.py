import Tkinter
import tkMessageBox
import time


class TaskControls(object):
    def stop_callback(self):
        tkMessageBox.showinfo("Stop Request..", "Stopped")
        exit(0)

    def start_callback(self):
        tkMessageBox.showinfo("Start Request..", "Started")

    def pause_callback(self):
        tkMessageBox.showinfo("Puase Request..", "Paused")


class UITemplate(object):
    def __init__(self, parent):
        self.parent = parent
        self.frame1 = Tkinter.Frame(self.parent)
        self.frame1.pack(side=Tkinter.LEFT)
        self.frame3 = Tkinter.Frame(self.parent)
        self.frame3.pack(padx=5, pady=5)
        self.frame2 = Tkinter.Frame(self.parent)
        self.frame2.pack(padx=10, pady=10)
        self.dc = Tkinter.Canvas(self.frame1, width=600, height=600, borderwidth=5, background='grey', relief='raised')
        #self.dc.pack(padx=10, pady=10)
        self.dc.pack()
        self.dc.grid()
        self.draweyecord = None
        self.t1 = None
        self.t2= None


    def drawtextbox(self):
        T = Tkinter.Text(self.frame3, height=40, width=60)
        T.pack()
    
    def drawcanvas(self):
        #frame = Tkinter.Frame(self.parent)
        #frame.pack()
        self.dc.create_oval(250, 250, 350, 350, outline="red", dash=(3,5))
        self.dc.create_oval(298, 298, 302, 302, outline="blue", fill='blue')
        #self.dc.create_line(100, 100, 120, 100, fill='green')
        self.t1 = self.dc.create_line(100, 100, 120, 100, fill='green')
        self.t2 = self.dc.create_line(110, 90, 110, 110, fill='green')
        #my_img = Tkinter.PhotoImage(file='/home/kbhdog/shobha/UI/tkinter_ui/Plus_sign.gif')
        #self.draweyecord = self.dc.create_image(255, 255, image=my_img)

    def draweyecordinates(self):
        #t1 = self.dc.create_line(100, 100, 120, 100, fill='green')
        #t2 = self.dc.create_line(110, 90, 110, 110, fill='green')
        from random import randint
        deltax = randint(0, 5)
        deltay = randint(0, 5)

        self.dc.move(self.t1, deltax, deltay)
        self.dc.move(self.t2, deltax, deltay)
        self.dc.after(50, self.draweyecordinates)

    def stopdraweyecordinates(self):
        self.draweyecord = False
        
    def draw_button(self):
        #frame = Tkinter.Frame(self.parent)
        #frame.pack(side=Tkinter.)
        tc = TaskControls()
        startbutton = Tkinter.Button(self.frame2, text='Start', command=tc.start_callback, height=1, width=3)
        #stopbutton.grid(row=1000, column=600)
        startbutton.pack(side=Tkinter.LEFT)
        #startbutton.place(bordermode=Tkinter.INSIDE, height=70, width=70)

        stopbutton = Tkinter.Button(self.frame2, text='Stop', command=tc.stop_callback, height=1, width=3)
        #stopbutton.grid(row=1000, column=600)
        stopbutton.pack(side=Tkinter.BOTTOM)
        #stopbutton.place(bordermode=Tkinter.INSIDE, height=70, width=70)

        pausebutton = Tkinter.Button(self.frame2, text='Pause', command=tc.pause_callback, height=1, width=3)
        #stopbutton.grid(row=1000, column=600)
        pausebutton.pack(side=Tkinter.BOTTOM)
        #pausebutton.place(bordermode=Tkinter.INSIDE, height=70, width=70)

        # draweye = Tkinter.Button(self.frame2, text='Move Eye Crod', command=self.draweyecordinates, height=1, width=10)
        # draweye.pack(side=Tkinter.BOTTOM)
        #
        # stopdraweye = Tkinter.Button(self.frame2, text='Stop Draw Eye Crod', command=self.stopdraweyecordinates, height=1, width=10)
        # stopdraweye.pack(side=Tkinter.BOTTOM)
        pass
        
 

def main():
 
    root = Tkinter.Tk()
    ui = UITemplate(root)
    ui.drawcanvas()
    ui.draw_button()
    ui.drawtextbox()
    root.mainloop()


if __name__ == '__main__':
    main()
#frame = Tkinter.Frame(top)
#main_frame.pack()

#bottom_frame = Tkinter.Frame(top)
#bottom_frame.pack(side=Tkinter.BOTTOM)

#c = Tkinter.Canvas(top, bg='blue', height=600, width=1000)
#c.pack()

#drawing_frame = Tkinter.LabelFrame(top, text="Drawing Frame", height=500, width=900)
#drawing_frame.pack(expand="yes")

#left_drawing_frame = Tkinter.Label(drawing_frame, text="Test")
#left_drawing_frame.pack()


