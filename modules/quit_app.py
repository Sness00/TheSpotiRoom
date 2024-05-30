import wx

class quit_app():

    app = None
    quit = False
    spotipy_object = None

    def __init__(self, spotipy_object):
        self.app = wx.App()
        self.spotipy_object = spotipy_object

    def get_quit(self):
        return self.quit

    def destroy_window(self):
        self.quit = True
        self.app.Destroy()
    
    def quit_function(self):
        self.quit = True
        self.app.Destroy()

    def quit_function_button(self, dummy_argument):
        self.quit = True
        self.spotipy_object.stop_spotify()
        self.app.Destroy()

    def window(self):
        frame = wx.Frame(None, -1, 'The Spoti-Room')
        button = wx.Button(parent=frame, label='Quit App')
        button.SetOwnBackgroundColour('red')
        button.Bind(event=wx.EVT_BUTTON, handler=self.quit_function_button)
        frame.Bind(event=wx.EVT_CLOSE, handler=self.quit_function_button)

        frame.SetIcon(icon=wx.Icon("./img/icona.ico"))

        frame.Show()

        self.app.MainLoop()
