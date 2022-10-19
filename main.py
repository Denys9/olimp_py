from tkinter import*
try:
    def Summa():
        a=int(pole1.get())
        b=int(pole2.get())
        pole3.delete(0, END)
        pole3.insert(0,a+b)

    def Summa2():
        a = int(pole1.get())
        b = int(pole2.get())
        pole3.delete(0, END)
        pole3.insert(0, a-b)

    def Summa3():
        a=int(pole1.get())
        b=int(pole2.get())
        pole3.delete(0, END)
        pole3.insert(0,a*b)

    def Summa4():
        a=int(pole1.get())
        b=int(pole2.get())
        pole3.delete(0, END)
        pole3.insert(0,a//b)

    def Summa5():
      a=int(pole1.get())
      b=int(pole2.get())
      pole3.delete(0, END)
      pole3.insert(0,a%b)


    window = Tk()
    window.geometry("400x400")
    window.configure(bg="white")
    window.title("Калькулятор")

    nad1=Label(text="Введіть перше число:", bg="white")
    nad1.place(x=20, y=20)

    nad2=Label(text="Введіть друге число:", bg="white")
    nad2.place(x=20, y=50)

    nad3=Label(text="Результат:")
    nad3.place(x=20, y=330)

    pole1 = Entry(window)
    pole1.place(x=200, y=20)

    pole2 = Entry(window)
    pole2.place(x=200, y=50)

    pole3 = Entry(window)
    pole3.place(x=200, y=330)

    kn1 = Button(window,text="plus", command=Summa)
    kn1.place(x=70, y=175, anchor="c")

    kn2 = Button(window, text="minus", command=Summa2)
    kn2.place(x=140, y=175, anchor="c")

    kn3 = Button(window, text="mult", command=Summa3)
    kn3.place(x=210, y=175, anchor="c")

    kn4 = Button(window, text="div", command=Summa4)
    kn4.place(x=280, y=175, anchor="c")

    kn5 = Button(window, text="mod", command=Summa5)
    kn5.place(x=350, y=175, anchor="c")

    window.mainloop()

except Exception as ex:
    print(f'Eror information: {ex}')