import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
from game import tboard


class homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
