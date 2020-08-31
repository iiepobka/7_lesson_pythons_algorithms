# Отсортируйте по возрастанию методом слияния одномерный вещественный
# массив, заданный случайными числами на промежутке [0; 50). Выведите
# на экран исходный и отсортированный массивы.
from random import random

STOP = 50
COUNT = 8
array_assert = [random() * STOP for x in range(COUNT)]
print(array_assert)
array = [[y] for y in array_assert]

while True:
    if len(array) == 1:
        break
    first = array[0]
    second = array[1]
    if second[0] > first[-1]:
        array.append(first + second)
    elif second[-1] < first[0]:
        array.append(second + first)
    else:
        while len(second) != 0:
            for i in range(len(first)):
                if first[i] > second[0]:
                    first.insert(i, second[0])
                    break
            else:
                first.append(second[0])
            del second[0]
        array.append(first)
    array = array[2:]

print(array[0])

if __name__ == '__main__':
    assert array[0] == sorted(array_assert)
    print('Проверка прошла успешно!')
