import customtkinter
import tkinter as tk
from PIL import Image, ImageTk
from views import welcome


def interface(self):
    # color_varibles
    self.blue = "#004AAD"
    self.red = "#FF3131"
    self.black = "#1E1E1E"
    self.bg = "#FFF9E1"

    # font_styles
    self.font1 = ("Inter", 14)
    self.font2 = ("Inter", 24, "bold")
    self.font3 = ("Inter", 20, "bold")
    self.font4 = ("Inter", 14, "bold")
    self.font5 = ("Inter", 32, "bold")
    self.font6 = ("Inter", 18)

    self.mainframe = customtkinter.CTkFrame(
        self, width=600, height=700, fg_color="#FFF9E1"
    )
    self.mainframe.pack()

    self.upper_bar = customtkinter.CTkFrame(
        self.mainframe, width=550, height=4, fg_color=self.black
    )
    self.upper_bar.place(relx=0.5, rely=0.03, anchor="center")
    self.about_image = customtkinter.CTkImage(
        light_image=Image.open("./src/Assets/nospacelogo.png"),
        dark_image=Image.open("./src/Assets/nospacelogo.png"),
        size=(91, 74),
    )
    self.background_label = customtkinter.CTkLabel(
        self.mainframe, image=self.about_image, text=""
    )
    self.background_label.place(x=95, y=25)
    self.lower_bar = customtkinter.CTkFrame(
        self.mainframe, width=550, height=4, fg_color=self.black
    )
    self.lower_bar.place(relx=0.5, rely=0.15, anchor="center")

    # buttons
    self.button_container = customtkinter.CTkFrame(
        self.mainframe, fg_color="transparent", bg_color="transparent"
    )
    self.button_container.place(relx=0.5, rely=0.91, anchor="center")
    self.reset_button = customtkinter.CTkButton(
        self.button_container,
        text="Reset",
        text_color=self.bg,
        height=37,
        corner_radius=50,
        font=self.font4,
        width=200,
        bg_color=self.bg,
        fg_color=self.blue,
        command=self.reset_progress,
    )
    self.return_button = customtkinter.CTkButton(
        self.button_container,
        height=37,
        text="Return",
        text_color=self.bg,
        width=200,
        corner_radius=50,
        font=self.font4,
        bg_color=self.bg,
        fg_color=self.blue,
        command=lambda: self.controller.show_frame(welcome.startpage),
    )
    self.reset_button.pack(side="left", padx=5)
    self.return_button.pack(side="left", padx=5)
