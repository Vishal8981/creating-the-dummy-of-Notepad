from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
def newf():
    global file
    root.title("Untitled-Notepad")
    file=None
    Textarea.delete(1.0,END) #1.0,END  means from first of the character to the end of the character.
def opens():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),
                                                            ("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        Textarea.delete(1.0, END)
        f = open(file, "r")
        Textarea.insert(1.0, f.read())
        f.close()
def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            # Save as a new file
            f = open(file, "w")
            f.write(Textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()
def quitapp():
    root.destroy()
def cut():
    Textarea.event_generate("<<Cut>>")
def copy():
    Textarea.event_generate("<<Copy>>")
def paste():
    Textarea.event_generate("<<Paste>>")
def about():
    tmsg.showinfo("NOTEPAD","NOTEPAD BY CODE WITH VISHAL")

root=Tk()
root.title("Untitled - Notepad")
root.geometry("654x354")
root.wm_iconbitmap("1.con.png")

# add textarea
Textarea=Text(root,font="lucida 10 ")
file=None
Textarea.pack(expand=True,fill="both")

#lets create a menubar
menubar=Menu(root)

#start a filemenu
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="NEW",command=newf)
filemenu.add_command(label="OPEN",command=opens)
filemenu.add_command(label="SAVE",command=save)
filemenu.add_separator()
filemenu.add_command(label="QUIT",command=quitapp)
menubar.add_cascade(label="FILE",menu=filemenu)
# filemenu is ends

#editmenu is started
editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="CUT",command=cut)
editmenu.add_command(label="COPY",command=copy)
editmenu.add_command(label="PASTE",command=paste)
menubar.add_cascade(label="EDIT",menu=editmenu)
#editmenu is end

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="ABOUT NOTEPAD",command=about)
menubar.add_cascade(label="HELP",menu=helpmenu)

root.config(menu=menubar)
#creating  the scrollbar
scrollbar=Scrollbar(Textarea)
scrollbar.pack(side=RIGHT,fill=Y)
scrollbar.config(command=Textarea.yview)
Textarea.config(yscrollcommand=scrollbar.set)


root.mainloop()