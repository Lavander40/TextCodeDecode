from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import data.mdl.encryption as enc


# Globals
global fileName
fileName = False
global selected
selected = False


# File Menu Functions
def newFile():
    global fileName
    fileName = False
    textInput.delete("0.0", END)
    statusbar['text'] = "был создан новый файл"


def openFile(e):
    global fileName
    fileName = fd.askopenfilename(initialdir="data/enc", filetypes=(('enc text files', '*.txtx'), ('All files', '*.*')))
    if fileName:
        with open(fileName, "r") as file:
            text = file.read()
            text = enc.DecodeText(text)
            textInput.delete("1.0", END)
            textInput.insert("1.0", text)
        statusbar['text'] = "был открыт файл " + fileName


def saveFile(e):
    global fileName
    if fileName:
        text = textInput.get("1.0", END)
        text = enc.CodeText(text)
        with open(fileName, "w") as file:
            file.write(text)
        statusbar['text'] = "файл был сохранён по аддресу " + fileName
    else:
        saveFileAs(e)


def saveFileAs(e):
    global fileName
    fileName = fd.asksaveasfilename(initialdir="data/enc", filetypes=(('enc text files', '*.txtx'),)) + ".txtx"
    if fileName:
        saveFile(False)


# Edit Menu Functions
def copy(keyboardInput):
    global selected
    if keyboardInput:
        selected = app.clipboard_get()
    if textInput.selection_get():
        selected = textInput.selection_get()
        app.clipboard_clear()
        app.clipboard_append(selected)


def paste(keyboardInput):
    global selected
    if keyboardInput:
        selected = app.clipboard_get()
    elif selected:
        pos = textInput.index(INSERT)
        textInput.insert(pos, selected)


# Help Menu Functions
def certificate():
    certificateWin = Toplevel(app)
    certificateWin.title("Справка")
    certificateWin.geometry("300x200+" + str(app.winfo_screenwidth()//3) + "+" + str(app.winfo_screenheight()//3))
    Label(certificateWin, wraplength=250,
          text="Данная программа является приложением для прозрачного шифрования текста\nПрограмма позволяет создавать/открывать/сохранять зашифрованные файлы\nЛичный ключ для шифрования хранится в файле AmTCD.ini в директории /data").pack()
    Button(certificateWin, text="Закрыть", command=lambda: certificateWin.destroy()).pack()


def aboutApp():
    mb.showinfo(
        title="О программе",
        message="Программа для прозрачного шифрования\n(с) Астаев К.А., БСБО-03-20 МИРЭА 2023г."
    )


# Main app settings
app = Tk()
app.geometry("650x410+" + str(app.winfo_screenwidth()//4) + "+" + str(app.winfo_screenheight()//4))
app.title("Текстовый шифратор")
app.resizable(False, False)

# Bindings
app.bind('<Control-Key-o>', openFile)
app.bind('<Control-Key-s>', saveFile)
app.bind('<Control-Shift-KeyPress-S>', saveFileAs)
app.bind('<Control-Key-c>', copy)
app.bind('<Control-Key-v>', paste)

# Menu section
mainMenu = Menu()
app.config(menu=mainMenu)

fileMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="Файл", menu=fileMenu)
fileMenu.add_command(label="Новый", command=newFile)
fileMenu.add_command(label="Открыть", command=lambda: openFile(False), accelerator="Clrl+O")
fileMenu.add_command(label="Сохранить", command=lambda: saveFile(False), accelerator="Clrl+S")
fileMenu.add_command(label="Сохранить как...", command=lambda: saveFileAs(False), accelerator="Clrl+Shift+S")
fileMenu.add_separator()
fileMenu.add_command(label="Выход", command=lambda: app.destroy())

editMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="Правка", menu=editMenu)
editMenu.add_command(label="Копировать", command=lambda: copy(False), accelerator="Clrl+C")
editMenu.add_command(label="Вставить", command=lambda: paste(False), accelerator="Clrl+V")
editMenu.add_separator()
editMenu.add_command(label="Параметры...")

helpMenu = Menu(mainMenu, tearoff=False)
mainMenu.add_cascade(label="Справка", menu=helpMenu)
helpMenu.add_command(label="Содержание", command=certificate)
helpMenu.add_separator()
helpMenu.add_command(label="О программе...", command=aboutApp)


# Text input section
textInput = ScrolledText(app, wrap="char")
textInput.pack()

# TaskBar
statusbar = Label(app, text="Ожидаем ввода...", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

# App Start
app.mainloop()
