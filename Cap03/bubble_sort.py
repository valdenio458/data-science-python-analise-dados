lista = [6, 7, 8, 3, 10, 19, 4, 1]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort(lista))
