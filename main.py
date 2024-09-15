def pass_word():
    list_value = []
    list_password = []
    n = int(input('Введите число от 3 до 20: '))
    if n < 3 :
        print('Неверное число, попытайся снова')
    if n > 20:
        print('Неверное число, попытайся снова')
        pass_word()
    else:
        for i in range(1, n):
            for j in range(1, n):
                if all([n % (i + j) == 0,
                        i != j,
                        [j, i] not in list_value]):
                    list_value.append([j, i])
    for i in list_value:
        list_password.extend(i)
    password = ' '.join(str(x) for x in list_password)
    print(password)

pass_word()
