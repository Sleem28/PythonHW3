# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import my_functions as mf

def get_fractional_part(f_value:float):
    val = str(f_value).split('.')[1]

    if len(val) == 2:
        return int(val)/100
    else:
        return int(val)/10
#-------------------------------------------------------------------------------------------------------+
def get_fract_part_array(float_list:list) -> list:
    output_list = list()

    for item in float_list:
        output_list.append(get_fractional_part(item))
    return output_list
#-------------------------------------------------------------------------------------------------------+
float_list = mf.fill_list_float_values(10)

print(f'Сгенерированный массив имеет вид: {float_list}')

fract_part_array = get_fract_part_array(float_list)
f_max = max(fract_part_array)
f_min = min(fract_part_array)
print(f'Максимальная дробная часть равна {f_max}.\nМинимальная дробная часть равна {f_min}.')
print(f'Разница между максимальным и минимальным значением дробной части равна {f_max - f_min}.')