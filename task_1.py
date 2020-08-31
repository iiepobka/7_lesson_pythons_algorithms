# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран
# исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход
# массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться
# сортировка пузырьком. Улучшенные версии сортировки, например, расчёской,
# шейкерная и другие в зачёт не идут.
from random import randint


def bubble(arr):
    len_arr = 1
    count = 0

    while count < len(arr):
        for i in range(len(arr) - len_arr):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        count += 1
        len_arr += 1
    return arr


START = -100
STOP = 99
COUNT = 10
array = [randint(START, STOP) for x in range(COUNT)]

print(array)
print(bubble(array))

if __name__ == '__main__':
    assert bubble(array) == sorted(array, reverse=True)
    print('Проверка прошла успешно!')
