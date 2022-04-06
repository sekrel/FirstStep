from tkinter import *
from parsing import*

#праметры окна
def ParameterWindow(root):
    root.title("ранг в лол")
    root.resizable(True, True)
    w = 800
    h = 600
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()
    x = int(ws/2-w/2)
    y = int(wh/2-h/2)
    root.geometry("{1}x{2}+{3}+{3}".format(w, h, x, y))

#обращение к парсеру/присваевание значение лейблу
def handlerButton():
    global en1
    global en2
    server = en1.get()
    name1 = en2.get()
    elo1 = elo(params(server, name1))
    result.config(text="Ваш ранг:"+str(elo1[len(elo1)-1]))

root= Tk()
ParameterWindow(root)

#объявление элементов
handler= Label(root, text="Суммированние чисел", font="Tahoma 20")
en1= Entry(root, font="Tahoma 25")
en2= Entry(root, font="Tahoma 25")
button= Button(root, text="Поиск данных", command=handlerButton)
result= Label(root, font="Tahoma 20")

#распаложение элеменов
handler.place(relx=0.5, rely=0.01, anchor="n")
en1.place(relx=0.5, rely=0.2, anchor="n")
en2.place(relx=0.5, rely=0.4, anchor="n")
button.place(relx=0.5, rely=0.6, anchor="n")
result.place(relx=0.5, rely=0.8, anchor="n")
en1.insert(0, "ru")

root.mainloop()






