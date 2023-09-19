import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from views import about, singleplayer, welcome, multiplayer


class mainpage(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # clip the main window in the center
        width = 600
        height = 700
        s_width = self.winfo_screenwidth()
        s_height = self.winfo_screenheight()
        x = (s_width / 2) - (width / 2)
        y = (s_height / 2) - (height / 2)

        # main-window
        self.wm_title("Tic Tac Toe")
        self.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.resizable(0, 0)
        self.iconbitmap("./src/Assets/icon.ico")

        # main-container
        container = customtkinter.CTkFrame(self)
        container.place(relx=0.5, rely=0.5, anchor="center")

        # frames
        self.frames = {}
        for F in (
            welcome.startpage,
            about.aboutpage,
            singleplayer.main_game,
            multiplayer.main_game,
        ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(welcome.startpage)

    # raise the current frame to the top
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == "__main__":
    App = mainpage()
    App.mainloop()
