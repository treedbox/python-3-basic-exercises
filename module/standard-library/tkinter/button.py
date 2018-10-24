from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title('Treedbox Button')
        self.master['background'] = '#00f'
        self.pack(
            fill=BOTH,
            expand=1
        )
        quitButton = Button(self, text='Quit', command=self.client_exit)
        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()


"""
command=self.client_exit
    call a function
        exit window
command=self.destroy
    destroy the button
command=root.destroy
    destroy the window
    exit window
"""

root = Tk()
root.geometry('400x300')

app = Window(root)
print(app)

root.mainloop()
