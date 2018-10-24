from tkinter import *
from os.path import abspath, join, dirname


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

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label='Save', command=self.save)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Show message', command=self.show_message)
        menu.add_cascade(label='Edit', menu=edit)

        showMessageButton = Button(self, text='Show Message Log', command=self.show_message)
        showMessageButton.place(x=100, y=100)

        showImageButton = Button(self, text='Show Image', command=self.show_image)
        showImageButton.place(x=100, y=130)

        showTextButton = Button(self, text='Show Text', command=self.show_text)
        showTextButton.place(x=100, y=160)

        quitButton = Button(self, text='Quit', command=self.client_exit)
        quitButton.place(x=170, y=190)

    def show_text(self):
        text = Label(self, text='Some text here')
        text.pack()

    def show_image(self):
        canvas = Canvas(width=100, height=50, bg='blue')
        canvas.pack()

        filename = 'treedbox.png'
        dir = abspath(dirname(__file__))
        absFilePathAutoSlash = abspath(join(dirname(__file__), filename))

        photo = PhotoImage(file=absFilePathAutoSlash)
        canvas.image = photo
        canvas.create_image(0, 0, image=photo, anchor=NW)
        print(photo)
        # pyimage1

    def client_exit(self):
        print('Bye bye! :*')
        exit()

    def show_message(self):
        print('Lorem Ipsum Dolor Sit Amet')

    def save(self):
        print('Save successful')


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
