a = [31, 41, 59, 26, 41, 58]


# По возрастанию
def sortup(arr):
    for j in range(1, len(arr)):
        key = arr[j]  # Значение из массива
        i = j - 1   # значение которое надо сдвинуть
        while i >= 0 and arr[i] > key:  # Если предыдущее значение больше чем текущее
            arr[i+1] = arr[i]  # сдвигаем значение вперед
            i = i-1  # индекс на один меньше
        arr[i+1] = key  # Ставим значение на нужное место
    return arr


print(sortup(a))


# По убыванию
def sortdown(arr):
    for j in range(1, len(arr)):
        key = arr[j]  # Значение из массива
        i = j - 1   # значение которое надо сдвинуть
        while i >= 0 and arr[i] < key:  # Если предыдущее значение больше чем текущее
            arr[i+1] = arr[i]  # сдвигаем значение вперед
            i = i-1  # индекс на один меньше
        arr[i+1] = key  # Ставим значение на нужное место
    return arr


print(sortdown(a))


def search(arr, v):
    for j in range(1, len(arr)):
        key = arr[j]
        if key == v:
            return j


print(search(a, 1))



