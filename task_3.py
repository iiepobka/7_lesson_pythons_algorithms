# Массив размером 2m + 1, где m — натуральное число, заполнен случайным
# образом. Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не
# меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но
# если это слишком сложно, используйте метод сортировки, который не
# рассматривался на уроках (сортировка слиянием также недопустима).
from random import randint

m = int(input('Введите натуральное число m, определяющее длину массива равную 2m + 1: '))
COUNT = 2 * m + 1
START = 1
STOP = 100
array = [randint(START, STOP) for _ in range(COUNT)]
print(array)

while len(array) != 1:
    index_max = 0
    index_min = 0

    for n, i in enumerate(array):
        if i > array[index_max]:
            index_max = n
    del array[index_max]

    # если COUNT % 2 == 0
    if len(array) == 1:
        break

    for n, i in enumerate(array):
        if i < array[index_min]:
            index_min = n
    del array[index_min]

print(array)
