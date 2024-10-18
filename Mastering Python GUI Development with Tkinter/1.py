import tkinter as tk

root = tk.Tk()

root.title("label")
root.geometry('250x150')
label = tk.Label(root,text= " label in Tkinter", bg="lightgreen", foreground="black")
label.pack(fill='x')

entry = tk.Entry(root)
entry.insert(0, "Test Text")
entry.config(state="disabled")
entry.pack()

button1 = tk.Button(root, text= "Test Button")
button1.pack(side="bottom")

root.mainloop()