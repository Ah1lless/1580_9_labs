'''
функция ошибки:
    проверка на ошибку
    если подходит вернуть True
    если нет то False
    
функция какое время суток:
    если 0 <= часы <= 5: то ночь
    если 6 <= часы <= 11: то утра
    если 12 <= часы <= 17: то дня
    если 18 <= часы <= 23: то вечера

функция окончания часа:
    если час > 12:
    то час = час - 12
    
    если час = 1: то число часа + "час"
    если час = 2,3,4: то число часа + "часа"
    если остальные: то число часа + "часов"
    
функция окончание минут:
    если минуты в определенных минутах: то число минут + "минута"
    если минуты в других определенных минутах: то число минут + "минуты"
    если не то и не то: то число минут + "минут"
    

функция общая:
    результат = ''
    
    если часы == 0 и минуты == 0: то полночь
    если часы == 12 и минуты == 0: то полдень
    
    если минуты == 0: то выводим итоге и вместо минут слово ровно
    если другое: то обычный вывод
    
функция маин:
    вводим данные
    проверка на ошибку: вывести ошибку
    если нет то: часы = первые 2 цифры, минуты = 2 последние, написать основную функцию
    
'''

def osibka(time):
    try:
        hour,minut=time.split()
    except ValueError:
        return True
    opmin=[i for i in range(60)]
    ophour=[i for i in range(24)]
    
    if len(time) <=5 and int(minut) in opmin and int(hour) in ophour and (time[2]==" " or time[1]==" ") and hour[0] !="-" and minut[0] != "-":
        return False
    else:
        return True

def what_hour_text(hour):
    if 0 <= hour < 6:
        return 'ночи'

    elif 6 <= hour < 12:
        return 'утра'

    elif 12 <= hour < 18:
        return 'дня'

    elif 18 <= hour < 24:
        return 'вечера'

def what_hour(hour):
    if hour > 12:
        hour = hour - 12

    if hour == 1:
        return str(hour) + ' ' + 'час'

    elif hour == 2 or hour == 3 or hour == 4:
        return str(hour) + ' ' + 'часа'

    else:
        return str(hour) + ' ' + 'часов'

def what_minute(minn):
    minut=[1,21,31,41,51]
    minuti=[2,3,4,22,23,24,32,33,34,42,43,44,52,53,54]

    if minn == 0:
        return 'ровно'
    elif minn in minut:
        return str(minn) + ' ' + 'минута'

    elif minn in minuti:
        return str(minn) + ' ' + 'минуты'

    else:
        return str(minn) + ' ' +'минут'

def tour_to_text(hour,minute):
    ig = ''
    
    if hour == 0 and minute == 0:
        return 'Полночь'

    if hour == 12 and minute == 0:
        return 'Полдень'

    elif minute == 0:
        ig = what_hour(hour) + ' ' + what_hour_text(hour)+ ' ' + what_minute(minute)
        return ig

    else:
        ig = what_hour(hour) + ' ' + what_minute(minute) + ' ' + what_hour_text(hour)
        return ig


    '''
    1 - час
    2, 3, 4 - часа
    #, 6, 7, 8, 9, 10, 11, 12 - часов
    1, 21, 31, 41, 51 - минута
    2-4, 22-24, 32-34, 42-44, 52, 53, 54 - минуты
    Остальное - минут
    '''

def main():
    print("Это программа перевода числовых данных времени в текст.")
    vvod=str(input("Введите данные в виде ЧЧ ММ: "))
    try:
        hour,minn=vvod.split()
    except ValueError:
        print('Введены недопустимые данные. Введите данные в виде ЧЧ ММ')
        print("Введите часы от 0 до 23 и минуты от 0 до 59")
    else:
        if osibka(vvod):
            print('Введены недопустимые данные. Введите данные в виде ЧЧ ММ')
            print("Введите часы от 0 до 23 и минуты от 0 до 59")
        else:
            hour,minn=vvod.split()
            hour=int(hour)
            minn=int(minn)
            print(tour_to_text(hour,minn))

        
if __name__ == "__main__":
    main()
    








