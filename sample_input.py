import Tkinter as Tk


class App(object):
    def __init__(self):
        self.root = Tk.Tk()
        self.root.wm_title("Question 7")
        self.label = Tk.Label(self.root, text="Enter your weight in pounds.")
        self.label.pack()

        self.weight_in_kg = Tk.StringVar()
        Tk.Entry(self.root, textvariable=self.weight_in_kg).pack()

        self.buttontext = Tk.StringVar()
        self.buttontext.set("Calculate")
        Tk.Button(self.root,
                  textvariable=self.buttontext,
                  command=self.clicked1).pack()

        self.label = Tk.Label(self.root, text="")
        self.label.pack()

        self.root.mainloop()

    def clicked1(self):
        weight_in_kg = self.weight_in_kg.get()
        self.label.configure(text=weight_in_kg)

    def button_click(self, e):
        pass

App()