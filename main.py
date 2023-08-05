def binary_search(array, element, left, right):
    middle = (right + left) // 2

    if left > right or middle >= len(array):
        return False

    if array[middle-1] < element and element <= array[middle]:
        return middle-1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def bubble(array):
    # Будем хранить количество сделанных перестановок
    cocount = 0
    # Будем хранить количество перестановок сделанных до текущего цикла
    prev = 0

    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                cocount += 1
                array[j], array[j + 1] = array[j + 1], array[j]
        # Оптимизировали пузырёк, отбросив пустые проходы цикла
        # Если перестановок за этот цикл не увеличилось, то всё стоит на своих местах.
        if prev == cocount:
            break
        prev = cocount

    return array


try:
    array = list(map(float, input('Введите числа через пробел: ').split()))
    number = int(input('Введите число: '))
except ValueError as error:
    print("Видимо, ввели не числа. Конец программы.")
else:
    print('Введенные числа: ', array)
    sorted_array = bubble(array)
    print('Введенные числа отсортированы: ', sorted_array)
    print('Позиция элемента, который меньше введенного, а следующий за ним больше или равен:', binary_search(sorted_array, number, 1, len(sorted_array)))

