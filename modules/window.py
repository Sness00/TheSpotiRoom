from tkinter import *

class window():

    root = None
    link_var = None
    link = None

    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.link_var = StringVar()

    def submit(self, dummy_argument):
        self.link = self.link_var.get()
        self.root.destroy()

    def display_window(self):
        self.root.iconbitmap("./img/icona.ico")
        self.root.geometry("1920x1080+0+0")
        self.root.title("The Spoti-Room")

        canvas1 = Canvas(self.root, relief='raised')
        canvas1.pack(fill = "both", expand = True)

        bg = PhotoImage(file = "./img/rendering_finale.png")
        canvas1.create_image(-300, -200, image = bg, anchor = "nw")

        label1 = Label(self.root, text='The Spoti-Room')
        label1.config(font=('helvetica', 32))
        canvas1.create_window(600, 100, window=label1, anchor = "nw")

        label2 = Label(self.root, text='You have been redirected to a web page: copy the URL and paste it down below.')
        label2.config(font=('helvetica', 12))
        canvas1.create_window(500, 200, window=label2, anchor = "nw")

        button3 = Button(self.root, text='Submit Link', command=lambda: self.submit(1), bg='blue', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(700, 300, window=button3, anchor="nw")

        entry = Entry(self.root, textvariable=self.link_var, background='white')
        canvas1.create_window(680, 260, window=entry, anchor="nw")

        self.root.bind('<Return>', self.submit)

        self.root.mainloop()
        return self.link