import os
from tkinter import *
import tkinter as tk

window=Tk()
window.configure(bg='#c8f7f7')
my_frame = Frame(window, border = 20)
def ActionBlur():
    os.system('DetectLive\cmd.py')
    
def ActionFilters():
    os.system('Filters\Filter.py')

def ActionExist():
    os.system('Existing\existing.py')

lbl=Label(window, text="Blurry Image Detection And Modifications", bg='#0cede6', fg='white', font=("Times",40,"bold","italic"))
lbl.config()
lbl.pack()

btn=tk.Button(window, command= ActionExist, background="#023030", text="Blur Detection With Existing Images", fg='white', height='3', width='35', font=("Times",20,"italic") ,bd=10 )
btn.pack(side=TOP, expand=YES, pady=1)

btn=tk.Button(window, command= ActionBlur, background="#1f4a46", text="Blur Detection With Live Images", fg='white', height='3', width='35', font=("Times",20,"italic"),bd=10)
btn.pack(side=TOP, expand=YES, pady=1)

btn=tk.Button(window, command= ActionFilters, background="#023030", text="Modify with Filters", fg='white', height='3', width='35', font=("Times",20,"italic") ,bd=10 )
btn.pack(side=TOP, expand=YES, pady=1)

lbl=Label(window, text="Rates For Not Blurry", bg='white', fg='black', font=("Times",30,"bold","italic","underline"))
lbl.place(x=0, y=180)

lbl=Label(window, text="0>250: Average", bg='white', fg='black', font=("Times",20,"italic"))
lbl.place(x=0, y=240)

lbl=Label(window, text="250>500: Above Average", bg='white', fg='black', font=("Times",20,"italic"))
lbl.place(x=0, y=320)

lbl=Label(window, text="500>750: Good!", bg='white', fg='black', font=("Times",20,"italic"))
lbl.place(x=0, y=400)

lbl=Label(window, text="750>1000: Excellent!!", bg='white', fg='black', font=("Times",20,"italic"))
lbl.place(x=0, y=480)

lbl=Label(window, text="1000>: Outstanding! :)", bg='white', fg='black', font=("Times",20,"italic"))
lbl.place(x=0, y=560)

lbl=Label(window, text="Rates For Blurry", bg='white', fg='black', justify="right", font=("Times",30,"bold","italic","underline"))
lbl.place(relx = 1, x =-2, y = 180, anchor = NE)

lbl=Label(window, text="0<: Outstanding! :) ", bg='white', fg='black', justify="right", font=("Times",20,"italic"))
lbl.place(relx = 1, x =-2, y = 240, anchor = NE)

lbl=Label(window, text="0>250: Average Image", bg='white', fg='black', justify="right", font=("Times",20,"italic"))
lbl.place(relx = 1, x =-2, y = 320, anchor = NE)

lbl=Label(window, text="250>500: little Bad Image", bg='white', fg='black', justify="right", font=("Times",20,"italic"))
lbl.place(relx = 1, x =-2, y = 400, anchor = NE)

lbl=Label(window, text="500>750: Bad Image", bg='white', fg='black', justify="right", font=("Times",20,"italic"))
lbl.place(relx = 1, x =-2, y = 480, anchor = NE)

lbl=Label(window, text="<750: Extremely Bad Image", bg='white', fg='black', justify="right", font=("Times",20,"italic"))
lbl.place(relx = 1, x =-2, y = 560, anchor = NE)

window.title('Blur Detections')
window.mainloop()

