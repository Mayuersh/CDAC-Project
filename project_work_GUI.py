import tkinter as tk
from tkinter import *
 
root = tk.Tk()
def submit_button_click():
    input_1_value = entry_1.get()
    input_2_value = entry_2.get()
    print("Input 1:", input_1_value)
    print("Input 2:", input_2_value)
    
root.geometry=("960x538")
root.minsize(960,538)
root.maxsize(960,538)
photo=PhotoImage(file=r"F:\Python nitin sir\practise_1\Capture.png")

label1=Label(image=photo)
label1.pack()


text_label = tk.Label(root, text="Project by Mayuresh Wankhede!")
text_label.place(x=390,y=80)
label_1 = tk.Label(root, text="Input 1:")
label_1.place(x=420,y=200)
entry_1 = tk.Entry(root)
entry_1.place(x=420,y=200)
label_2 = tk.Label(root, text="Input 1:")
label_2.place(x=420,y=250)
entry_2 = tk.Entry(root)
entry_2.place(x=420,y=250)
submit_button = tk.Button( root, text="Submit", command=submit_button_click)
submit_button.place(x=455, y=280)  


root.mainloop()
