try:
    petr = int(input("Введіть кількість цукерок Петрика до обміну - "))
    vasya = int(input("Введіть кількість цукерок Василька до обміну - "))
    print('Петрик отримав',vasya,'цукерок')
except Exception as ex:
    print(f'Eror information: {ex}')