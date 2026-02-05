import random
from prettytable import PrettyTable




def selection_sort(arr):
    n = len(arr)
    coll_change = 0
    coll_compare = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            coll_compare += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
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
            coll_compare += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
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
            coll_compare += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                coll_change += 1
                swapped = True
        if not swapped:
            break
        end -= 1
        for i in range(end - 1, start - 1, -1):
            coll_compare += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                coll_change += 1
                swapped = True
        start += 1
    return arr, coll_compare, coll_change


def table(fistr_sort, second_sort, third_sort):
    table = PrettyTable(["Сортировка", "Сравнения", "Перестановки"])
    table.add_row(["Пузырьком", fistr_sort[1], fistr_sort[2]])
    table.add_row(["Выбором", second_sort[1], second_sort[2]])
    table.add_row(["Шейкерная", third_sort[1], third_sort[2]])
    print(table)


def demonstrative_mode():
    length_mas = random.randint(1, 15)
    arr = [random.randint(0, 99) for _ in range(length_mas)]
    print("Неотсортированный массив:",*arr)

    select_arr = selection_sort(arr.copy())
    bubble_arr = bubble_sort(arr.copy())
    shaker_arr = cocktail_shaker_sort(arr.copy())

    print("Отсрортированный массив:", *shaker_arr[0])
    table(bubble_arr, select_arr, shaker_arr)

    print("1. Остаться в демонстративном режиме")
    print("2. Перейти в интерактивный режим")
    print("3. Выход из программы")

    answer = str(input())
    while 1 != 0:
        while answer != "1" or answer != "2" or answer != "3":
            if answer == "1":
                demonstrative_mode()
            elif answer == "2":
                interactive_mode()
            elif answer == "3":
                exit()
            break
        print("Введено неверное значение")
        answer = str(input('Введите 1, 2 или 3: '))



def parse_array(arr_str):
    try:
        arr = list(map(int, arr_str.split()))
        return arr
    except ValueError:
        return None


def interactive_mode():
    while True:
        length_arr = str(input('Введите длину массива: '))
        if length_arr.isdigit() and int(length_arr) > 0:
            arr = [random.randint(0, 99) for _ in range(int(length_arr))]

            while True:
                print('Текущий массив:')
                print(*arr)

                print('Меню:')
                print('1. Ввести новый массив')
                print('2. Сгенерировать случайный массив')
                print('3. Сохранить массив')

                answer = input('Ваш выбор: ')
                if answer == '1':
                    while True:
                        arr_str = input('Введите массив целых чисел через пробел: ')
                        new_arr = parse_array(arr_str)
                        if new_arr is None:
                            print('Ошибка! Введите только целые числа.')
                        else:
                            arr = new_arr
                            break
                elif answer == '2':
                    length_arr = int(input('Введите длину массива: '))
                    arr = [random.randint(0, 99) for _ in range(length_arr)]
                elif answer == '3':
                    break
                else:
                    print('Неверный пункт меню')
                
            bubble = bubble_sort(arr.copy())
            selection = selection_sort(arr.copy())
            shaker = cocktail_shaker_sort(arr.copy())

            table(bubble, selection, shaker)

            print('1 — начать заново')
            print('2 — переключиться в другой режим')
            print('3 — выйти')
            print('Ваш выбор: ')
            
            restart = str(input())
            if restart == '1' and restart.isdigit():
                continue
            elif restart == '2' and restart.isdigit():
                demonstrative_mode()
            elif restart == '3' and restart.isdigit():
                exit()
        else:
            print("Введите натуральное число")

def main():
    while True:
        print("Выберите действие")
        print("1. Демонстративный режим")
        print("2. Интерактивный режим")
        print("3. Выйти из программы")
        a=str(input())
        if a.isdigit():
            if a=="1":
                demonstrative_mode()
            if a=="2":
                interactive_mode()
            if a=="3":
                exit()
            
            
if __name__ == "__main__":
    main()
