try:
    cost = int(input('Введіть ціну однієї шоколадки - '))
    per = int(input('Введіть відсоток подорожання шоколадки - '))
    money = int(input('Введіть суму грошей Степана - '))
    sum1 = cost*per/100
    sum2 = sum1+cost
    amount = money//sum2
    print('Степан може купити',amount,'шоколадок')
except Exception as ex:
    print(f'Eror information: {ex}')