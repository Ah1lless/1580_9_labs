import random


def selection_sort(arr):
    n = len(arr)
    coll_change = 0
    coll_compare = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                coll_compare += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        coll_change += 1
    return arr, coll_compare, coll_change


def bubble_sort(arr):
    n = len(arr)
    coll_change = 0
    coll_compare = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                coll_compare += 1
                coll_change += 1
                swapped = True
        if not swapped:
            break
    return arr, coll_compare, coll_change


def cocktail_shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    coll_change = 0
    coll_compare = 0
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                coll_compare += 1
                coll_change += 1
                swapped = True
        if not swapped:
            break
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                coll_compare += 1
                coll_change += 1
                swapped = True
        start += 1
    return arr, coll_compare, coll_change

def demonstrative_mode():
    length_mas = random.randint(1, 15)
    arr = [random.randint(0, 99) for _ in range(length_mas)]
    print(*arr)
    select_arr = selection_sort(arr.copy())
    bubble_arr = bubble_sort(arr.copy())
    shaker_arr = cocktail_shaker_sort(arr.copy())






def main():
    while True:
        print("Выберите действие")
        print("1. Демонстративный режим")
        print("2. Интерактивный режим режим")
        print("3. Выйти из программы")
        a=str(input())
        if a.isdigit():
            if a=="1":
                return 0
            
            
if __name__ == "__main__":
    main()