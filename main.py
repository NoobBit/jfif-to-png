from tkinter import *
from tkinter import filedialog, messagebox
import cv2
import sys
import os

img = ""

def r_img():
    global img
    img = open_image()

def open_image():
    img_path = filedialog.askopenfilename(initialdir="C:/", 
        title="Open Image", 
        filetypes=(("Jfif File", "*.jfif"), ("All Files", "*.*")))
    
    if img_path == "" or os.path.splitext(img_path)[1] != ".jfif": 
        messagebox.showwarning("Warning", "You must enter an jfif image")
    else:
        submit_button["state"] = "normal"
        return img_path

def open_image_result():
    opened_img = cv2.imread(img, 1)
    cv2.imshow("Jfif to Png Conversion Tool - " + os.path.splitext(img)[0] + ".png", opened_img)
    key = cv2.waitKey(0)
    
    cv2.destroyAllWindows()

def convert():
    pic = cv2.imread(img, 1)
    cv2.imwrite(os.path.splitext(img)[0] + ".png", pic)

    open_image_result()

root = Tk()

root.title("Jfif to Png Conversion Tool")
root.geometry("500x300")

title_text = Label(text="Jfif to Png Conversion Tool", font=("Arial", 20))
title_text.grid(row=0, column=0, padx=80, pady=30)

image_button = Button(text="Open Image", command=r_img, fg="#FFFFFF", bg="#0000FF", height=5, width=30, font=("Arial", 10), borderwidth=1)
image_button.grid(row=1, column=0)

submit_button = Button(text="Convert", command=convert, font=("Arial", 11), borderwidth=1)
submit_button["state"] = "disabled"
submit_button.grid(row=2, column=0, pady=20)

root.mainloop()