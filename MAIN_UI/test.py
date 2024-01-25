
from tkinter import*
from tkinter import ttk
import customtkinter
from time import *
from PIL import Image
# AT THE END, WRITE THIS AS A CLASS


# ==============
# -- settings --
# ==============

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

win_width = 960
win_height = 640

dimension = str(win_width) + "x" + str(win_height)


# ======================
# -- helper functions --
# ======================


# ====================
# -- initialization --
# ====================

root = customtkinter.CTk()
root.geometry(dimension)



# background init
bg_image = customtkinter.CTkImage(Image.open("./resources/bg.png"),size=(win_width, win_height))


# ===============
# -- load page --
# ===============

bg_image_label = customtkinter.CTkLabel(master=root, image=bg_image, text="")
bg_image_label.grid(row=0, column=0)


label = customtkinter.CTkLabel(master=root, text="text", font=("AppleGothic", 18), text_color="#000000", fg_color=("white", "gray75"))
label.place(relx=0.5, rely=0.45, anchor=CENTER)

user_name = Label(root, text="Username").place(x=40, y=60) 

# ============
# -- update --
# ============

root.mainloop()