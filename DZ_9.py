

try:
    a =  input('введите числа')
    print(int (a[0])/int(a[1]))
except ZeroDivisionError as er:
    print(er)
    b = input('введите число повторно, вторая цифра должна быть не ноль')
    while b[1]!=0:
        print(int(b[0]) / int(b[1]))
        break
    else:
        print('введите число повторно')

except ValueError:
    print('были введены буквыee')
