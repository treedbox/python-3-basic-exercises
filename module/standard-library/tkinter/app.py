import tkinter
"""
_init_
    constructor
    is the function that is called when you create an instance of a class
self
    a pointer to class itself (Window)
"""


class Window(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.master = master


root = tkinter.Tk()
print(root)
# .

root.title('Treedbox Tk')
# root['bg'] = '#f00'
# root.configure(background='#fd0')
root['background'] = '#00f'
print(root)
# .


app = Window(root)
print(app)
# .!window

print(root.mainloop())
root.mainloop()

"""
tkinter.scrolledtext
    Text widget with a vertical scroll bar built in.
tkinter.colorchooser
    Dialog to let the user choose a color.
tkinter.commondialog
    Base class for the dialogs defined in the other modules listed here.
tkinter.filedialog
    Common dialogs to allow the user to specify a file to open or save.
tkinter.font
    Utilities to help work with fonts.
tkinter.messagebox
    Access to standard Tk dialog boxes.
tkinter.simpledialog
    Basic dialogs and convenience functions.
tkinter.dnd
    Drag-and-drop support for tkinter. This is experimental and should become deprecated when it is replaced with the Tk DND.
turtle
    Turtle graphics in a Tk window.
"""
