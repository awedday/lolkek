print("Калькулятор")

'''
Сделать калькулятор с базовыми функциями и добавить ввод количества введенных чисел, используя то, что изучили в лекции
'''

mas = int(input("Введите количество операции: "))
one = float(input('Введите число: '))
i=0
while i<mas:
    print("введите желаемую операцию:\n1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление\n5 - процент от числа")
    operation = input( )
    if operation == '1':
        two = float(input('Введите второе число: '))
        one = one + two
        i +=1
        print(one)
    elif operation == '2':
        two = float(input('Введите второе число: '))
        one = one - two
        i +=1
        print(one)
    elif operation == '3':
        two = float(input('Введите второе число: '))
        one = one * two
        i +=1
        print(one)
    elif operation == '4':
        two = float(input('Введите второе число: ')) 
        if two == 0:
            print("На ноль делить нельзя")
        else:
            one = one / two
            i +=1
            print(one)
    elif operation == '5':
        two = float(input('Введите второе число: '))
        one = one / two * 100
        i +=1
        print(one)
    else:
        print("Такой операции нет")
    
