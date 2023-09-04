
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk

class startpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        #color_varibles
        self.blue = "#004AAD"
        self.red = "#FF3131"
        self.black = "#1E1E1E"
        self.bg = "#FFF9E1"
        
        #font_styles
        font1 = ('Inter', 14, 'bold') 
        
        
        #background_image_frame
        self.bg_frame = customtkinter.CTkFrame(self, width=600, height = 700)
        self.bg_frame.pack()
        
        #background_image
        self.bg_image = Image.open("./src/Assets/bg.png")
        self.background_image = ImageTk.PhotoImage(self.bg_image)
        self.background_label = tk.Label(self.bg_frame, image=self.background_image)
        self.background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        
        self.oneplayer_button = customtkinter.CTkButton(self.bg_frame,text = "One Player", text_color=self.bg,  height=37, corner_radius=50, font=font1,width = 200,bg_color=self.bg, fg_color=self.blue)
        self.twoplayer_button = customtkinter.CTkButton(self.bg_frame,text = "Two Player",  text_color=self.bg, height=37, corner_radius=50, font=font1,width = 200,bg_color=self.bg, fg_color=self.blue)
        self.instructions_button = customtkinter.CTkButton(self.bg_frame,text = "Instructions",  text_color=self.bg, height=37, corner_radius=50, font=font1, width = 200,bg_color=self.bg, fg_color=self.black)
        self.exit_button = customtkinter.CTkButton(self.bg_frame, height=37,text = "Quit",  text_color=self.bg, width = 200, corner_radius=50, font=font1,bg_color=self.bg, fg_color=self.red)
        
        self.oneplayer_button.place(relx = 0.5, rely = 0.57, anchor = "center")
        self.twoplayer_button.place(relx = 0.5, rely = 0.65, anchor = "center")
        self.instructions_button.place(relx = 0.5, rely = 0.73, anchor = "center")
        self.exit_button.place(relx = 0.5, rely = 0.85, anchor = "center")