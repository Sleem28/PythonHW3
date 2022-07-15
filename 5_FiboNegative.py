# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def negafibonacci(n:int) -> int:
    if n == -1:
        return 1
    elif n == -2:
        return -1
    return negafibonacci(n + 2) - negafibonacci(n + 1)
#---------------------------------------------------------------------------------------------------------------------------+
def fibonacci(n:int) -> int:
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
#---------------------------------------------------------------------------------------------------------------------------+
def fill_fibolist(num:int):
    output_list = list()

    for i in range(-num,0):
        output_list.append(negafibonacci(i))
    
    for i in range(0,num+1):
        output_list.append(fibonacci(i))
    
    return output_list
#---------------------------------------------------------------------------------------------------------------------------+
n = int(input("Введите число членов последовательности для позитивного и негативного фибоначчи: "))

print(f'Позитивный и негативный ряд для {n} членов равен {fill_fibolist(n)}')


