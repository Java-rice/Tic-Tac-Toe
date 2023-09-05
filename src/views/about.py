import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from views import welcome

class aboutpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        #color_varibles
        self.blue = "#004AAD"
        self.red = "#FF3131"
        self.black = "#1E1E1E"
        self.bg = "#FFF9E1"
        
        #font_styles
        self.font1 = ('Inter', 14)
        self.font2 = ('Inter', 24, 'bold')
        self.font3 = ('Inter', 20, 'bold')
        self.font4 = ('Inter', 14, 'bold')

        #mainframe
        self.bg_frame = customtkinter.CTkFrame(self, width=600, height = 700, fg_color = "#FFF9E1")
        self.bg_frame.pack()
        
        #title-image and title-text
        self.about_image = customtkinter.CTkImage(light_image=Image.open("./src/Assets/logo.png"),dark_image=Image.open("./src/Assets/logo.png"),size=(100, 100))
        self.background_label = customtkinter.CTkLabel(self.bg_frame, image=self.about_image, text="")
        self.background_label.place(x = 100, y = 40)
        self.about = customtkinter.CTkLabel(self.bg_frame, text="About", font=self.font2, text_color=self.black)
        self.about.place(x = 220, y = 70)
        
        #what is tic-tac-toe
        self.what_is_TTT = customtkinter.CTkLabel(self.bg_frame, text="What is Tic Tac Toe?", font=self.font3, text_color=self.black)
        self.what_is_TTT.place(x = 110, y = 150)
        self.TTT_text = customtkinter.CTkTextbox(self.bg_frame, wrap="word",font=self.font1,width=400, height=120, text_color=self.black, bg_color="transparent", fg_color="transparent")
        self.TTT_text.place(x = 100, y = 180)
        self.TTT_text.insert("0.0",text="Tic-Tac-Toe, also known as Noughts and Crosses, is a classic two-player strategy game typically played on a 3x3 grid. The objective of the game is for one player to form a line of three of their own symbols (either 'X' or 'O') horizontally, vertically, or diagonally, before the opponent does.")
        
        #instructions
        self.inst_label = customtkinter.CTkLabel(self.bg_frame, text="Instructions", font=self.font3, text_color=self.black)
        self.inst_label.place(x = 110, y = 300)
        
        
        #return_to_welcome
        self.return_welcome = customtkinter.CTkButton(self.bg_frame,text = "Return", text_color=self.bg,  height=37, corner_radius=50, font=self.font4,width = 200,bg_color=self.bg, fg_color=self.red, command=lambda: self.controller.show_frame(welcome.startpage))
        self.return_welcome.place(relx = 0.5, rely = 0.85, anchor = "center")