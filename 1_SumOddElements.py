from array import array
import my_functions as mf

int_list     = mf.fill_list(items=10)
sum_odd_indexes_elem = 0

for i in range(0,len(int_list)):
    if i%2 != 0:
        sum_odd_indexes_elem += int_list[i]


print(int_list)
print(f'Сумма нечетных элементов массива равна {sum_odd_indexes_elem}.')