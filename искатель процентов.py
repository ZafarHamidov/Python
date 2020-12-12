connect = True

while connect == True:
    number = input("Число: ")
    procent = input("Процент: ")
    while type(number) != int:
        try:
            number = int(number)
            procent = int(procent)
        except ValueError:
            print("Вводи цифры!")
            number = input('Введи число: ')
            print()
            procent = input('Введи процент: ')
            print()

    while type(number) != float:
        try:
            number = float(number)
            procent = float(procent)

        except ValueError:
            print('Вводи цифры!')
            number = input('Введи число: ')
            print()
            procent = input('Введи процент: ')
            print()


    finish = number / 100 * procent
    print('Ваш ответ:', float(finish))
    
