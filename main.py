from planet import stars

stars_list = []

def load_stars_db(file_name):
    try:
        with open(file_name, 'r', encoding='UTF-8') as file:
            for string in file:
                line = string.strip()
                if not line:
                    continue
                db_line = line.split(', ')
                star = stars(db_line[0], float(db_line[1]), float(db_line[2]), float(db_line[3]), db_line[4])
                stars_list.append(star)
    except FileNotFoundError:
        print('Файла не существует, попробуйте снова')
    else:
        print('Звезды загружены из файла')

def save_stars_db(file_name):
    with open(file_name, 'w', encoding='UTF-8') as output:
        for star in stars_list:
            print(f'{star.name}, {star.radius}, {star.mass}, {star.distance}, {star.type}', file=output)
        print("Звезды сохранены в файл")

def check_err_val(val_check):
    while True:
        try:
            check_in_prog = float(input(val_check).replace(',', '.'))
            if check_in_prog >= 1: 
                return check_in_prog
            print("Минимальное допустимое значение 1")
        except ValueError:
            print("Требуется ввести число, попробуйте снова")
    
def check_err_str(val_check):
    while True:
        check_in_prog = input(val_check).strip()
        if check_in_prog:
            return check_in_prog
        print("Не может быть пустой строкой")

def create_star():
    options = [
        ('Введите название звезды: ', check_err_str),
        ('Введите радиус звезды в километрах: ', check_err_val),
        ('Введите массу звезды в килограммах: ', check_err_val),
        ('Введите расстояние от звезды до Солнца в километрах: ', check_err_val),
        ('Введите тип звезды: ', check_err_str),
    ]
    values = [cheker(stars_option) for stars_option, cheker in options]
    star = stars(*values)
    stars_list.append(star)
    print(f"Звезда {star.name} успешно создана")


def find_star_by_id(star_id):
    for star in stars_list:
        if star._id == star_id:
            return star
    return None


def find_star_by_name(name):
    for star in stars_list:
        if star.name.lower() == name.lower():
            return star
    return None


def delete_star():
    if not stars_list:
        print("Список звезд пуст, нечего удалять")
        return

    while True:
        choice = input('Удалить звезду по (1) ID или (2) названию? ').strip()
        if choice == '1':
            star_id_str = input('Введите ID звезды: ').strip()
            if not star_id_str.isdigit():
                print('ID должен быть числом')
                continue
            star = find_star_by_id(int(star_id_str))
        elif choice == '2':
            star_name = input('Введите название звезды: ').strip()
            if not star_name:
                print('Название не может быть пустым')
                continue
            star = find_star_by_name(star_name)
        else:
            print('Неверный выбор, используйте 1 или 2')
            continue

        if star:
            stars_list.remove(star)
            print(f"Звезда удалена: ID {star._id}, {star.name}")
            break
        print('Звезда не найдена. Попробуйте снова.')


def edit_star():
    if not stars_list:
        print("Список звезд пуст, нечего изменять")
        return

    while True:
        choice = input('Изменить звезду по (1) ID или (2) названию? ').strip()
        if choice == '1':
            star_id_str = input('Введите ID звезды: ').strip()
            if not star_id_str.isdigit():
                print('ID должен быть числом')
                continue
            target = find_star_by_id(int(star_id_str))
        elif choice == '2':
            star_name = input('Введите название звезды: ').strip()
            if not star_name:
                print('Название не может быть пустым')
                continue
            target = find_star_by_name(star_name)
        else:
            print('Неверный выбор, используйте 1 или 2')
            continue

        if not target:
            print('Звезда не найдена. Попробуйте снова.')
            continue

        index = stars_list.index(target)
        print(f"Изменяем звезду: ID {target._id}, {target.name}")
        new_name = check_err_str('Введите новое название звезды: ')
        new_radius = check_err_val('Введите новый радиус звезды в километрах: ')
        new_mass = check_err_val('Введите новую массу звезды в килограммах: ')
        new_distance = check_err_val('Введите новое расстояние от звезды до Солнца в километрах: ')
        new_type = check_err_str('Введите новый тип звезды: ')

        updated_star = stars(new_name, new_radius, new_mass, new_distance, new_type)
        updated_star._id = target._id
        stars_list[index] = updated_star
        print(f"Звезда обновлена: ID {updated_star._id}, {updated_star.name}")
        break


def search_star():
    if not stars_list:
        print("Список звезд пуст, нечего искать")
        return None

    while True:
        choice = input('Найти звезду по (1) ID или (2) названию? ').strip()
        if choice == '1':
            star_id_str = input('Введите ID звезды: ').strip()
            if not star_id_str.isdigit():
                print('ID должен быть числом')
                continue
            star = find_star_by_id(int(star_id_str))
        elif choice == '2':
            star_name = input('Введите название звезды: ').strip()
            if not star_name:
                print('Название не может быть пустым')
                continue
            star = find_star_by_name(star_name)
        else:
            print('Неверный выбор, используйте 1 или 2')
            continue

        if star:
            print(f"Найдена звезда: ID {star._id}, {star.name}, Тип {star.type}, Радиус {star.radius}, Масса {star.mass}, Расстояние {star.distance}")
            return star

        print('Звезда не найдена. Попробуйте снова.')



def sort_planet():
    if stars_list == []:
        print('Нет планет. Нечего сортировать')

    print('Выберите сортировку: по расстоянию(1), по радиусу(2), по массе(3)')
    input_choose = int(input())

    if input_choose == 1:
        Flag = 4
    elif input_choose == 2:
        Flag = 2
    elif input_choose == 3:
        Flag = 3
    
    length = len(stars_list)
    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            coll_compare += 1
            if stars_list[Flag][j] > stars_list[Flag][j + 1]:
                stars_list[Flag][j], stars_list[Flag][j + 1] = stars_list[Flag][j + 1], stars_list[Flag][j]
                coll_change += 1
                swapped = True
        if not swapped:
            break
    return arr, coll_compare, coll_change


def print_stars():
    if not stars_list:
        print("Список звезд пуст")
        return

    print('Текущий список звезд:')
    for star in stars_list:
        print(f"ID {star._id}, {star.name}, Тип {star.type}, Радиус {star.radius}, Масса {star.mass}, Расстояние {star.distance}")


def get_menu_choice():
    while True:
        print('\nМеню управления звездами:')
        print('1 - Создать звезду')
        print('2 - Изменить звезду')
        print('3 - Удалить звезду')
        print('4 - Найти звезду')
        print('5 - Сортировать звезды')
        print('6 - Показать все звезды')
        print('7 - Загрузить звезды из файла')
        print('8 - Сохранить звезды в файл')
        print('9 - Выход')
        choice = input('Выберите действие: ').strip()
        if choice in [str(i) for i in range(1, 10)]:
            return choice
        print('Неверный выбор, попробуйте снова.')


def run_menu():
    print("Добро пожаловать в программу по созданию звезд!")
    while True:
        choice = get_menu_choice()
        if choice == '1':
            create_star()
        elif choice == '2':
            edit_star()
        elif choice == '3':
            delete_star()
        elif choice == '4':
            search_star()
        elif choice == '5':
            sort_stars()
        elif choice == '6':
            print_stars()
        elif choice == '7':
            filename = check_err_str('Введите имя файла для загрузки: ')
            load_stars_db(filename)
        elif choice == '8':
            filename = check_err_str('Введите имя файла для сохранения: ')
            save_stars_db(filename)
        elif choice == '9':
            print('Выход из программы.')
            break
        print()


















if __name__ == '__main__':
    run_menu()
