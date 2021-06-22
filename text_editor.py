from tkinter.filedialog import *
from tkinter.messagebox import showerror

filename = None


# new file
def newFile():
    global filename
    filename = 'Untitled'
    text.delete(0.0, END)


# saving the file
def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()


# save as
def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops", message="unable to save the file")


# to open a file
def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)


root = Tk()
root.title("Simple Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = Text(root, width=400, height=400)
text.pack()

# adding menu bar
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label='New', command=newFile)
filemenu.add_command(label='Open', command=openFile)
filemenu.add_command(label='Save As', command=saveAs)
filemenu.add_command(label='Save', command=saveFile)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=root.quit)
menubar.add_cascade(label='File', menu=filemenu)

root.config(menu=menubar)
root.mainloop()
