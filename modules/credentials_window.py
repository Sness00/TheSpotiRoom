from tkinter import *

class cred_window():

    root = None
    client_id_var = None
    client_id = None
    client_secret_var = None
    client_secret = None
    uri_var = None
    uri = None

    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.client_id_var = StringVar()
        self.client_secret_var = StringVar()
        self.uri_var = StringVar()

    def submit(self, dummy_argument):
        self.client_id = self.client_id_var.get()
        self.client_secret = self.client_secret_var.get()
        self.uri = self.uri_var.get()
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

        label2 = Label(self.root, text='Insert your Client ID:')
        label2.config(font=('helvetica', 12))
        canvas1.create_window(500, 200, window=label2, anchor = "nw")
        entry1 = Entry(self.root, textvariable=self.client_id_var, background='white')
        canvas1.create_window(850, 200, window=entry1, anchor="nw")

        label3 = Label(self.root, text='Insert your Client Secret:')
        label3.config(font=('helvetica', 12))
        canvas1.create_window(500, 320, window=label3, anchor = "nw")
        entry2 = Entry(self.root, textvariable=self.client_secret_var, background='white')
        canvas1.create_window(850, 320, window=entry2, anchor="nw")

        label3 = Label(self.root, text='Insert your redirect URI:')
        label3.config(font=('helvetica', 12))
        canvas1.create_window(500, 440, window=label3, anchor = "nw")
        entry3 = Entry(self.root, textvariable=self.uri_var, background='white')
        canvas1.create_window(850, 440, window=entry3, anchor="nw")

        
        button3 = Button(self.root, text='Submit Credentials', command=lambda: self.submit(1) if (self.client_id_var != '' and self.client_secret_var != '' and self.uri_var != '') else None, bg='blue', fg='white', font=('helvetica', 9, 'bold'))
        canvas1.create_window(700, 600, window=button3, anchor="nw")

        

        self.root.bind('<Return>', self.submit)

        self.root.mainloop()
        return self.client_id, self.client_secret, self.uri
