# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import my_functions as mf

def mult_opposite_items(input_list:list) -> list:
    output_list = list()
    neg_counter = len(input_list)-1
    half_counter = int(len(input_list)/2)

    if len(input_list)%2 == 0: 
        is_odd = False
    else:
        is_odd = True

    for i in range(0,half_counter):
        output_list.append(input_list[i] * input_list[neg_counter])
        neg_counter -= 1

    if is_odd:
        output_list.append(input_list[neg_counter] * input_list[neg_counter])
    return output_list
#------------------------------------------------------------------------------------------------------------------+
int_list = mf.fill_list(int(input('Введите размер генерируемого массива: ')))
print(f'Сгенерированный массив имеет вид {int_list}.')
print(f'Массив с перемноженными противоположными элементами имеет вид {mult_opposite_items(int_list)}.')

