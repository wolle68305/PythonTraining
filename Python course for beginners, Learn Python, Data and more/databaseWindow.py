from tkinter import *
import databaseWorker as dbWorker

root = Tk()

def HelloWorld():
    dbWorker.writeValueToDB(text_entry.get(),text_entry2.get())

root.title("Database Window")
root.geometry("300x150")
root.resizable(False,False)
Label(root, text="").grid(row=0,column=1,sticky="w")
Label(root, text="Column1").grid(row=1,column=1,padx=20,sticky="w")
text_entry = Entry(root, width=15)
text_entry.grid(row=1,column=2,pady=5,sticky="w")

Label(root, text="Column2").grid(row=2,column=1,padx=20,sticky="w")
text_entry2 = Entry(root, width=15)
text_entry2.grid(row=2,column=2,pady=5,sticky="w")

Button(root, text="Test Button", command=HelloWorld).grid(row=3,column=2,pady=10)
root.mainloop()

