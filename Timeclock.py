'''
функция ошибки:
    проверка на ошибку
    если подходит вернуть True
    если нет то False
    
функция какое время суток:
    если 0 <= hour <= 5: то ночь
    если 6 <= hour <= 11: то утра
    если 12 <= hour <= 17: то дня
    если 18 <= hour <= 23: то вечера

функция окончания часа:
    если час > 12:
    то час = час - 12
    
    если час = 1: то число часа + "час"
    если час = 2,3,4: то число часа + "часа"
    если остальные: то число часа + "часов"
    
функция окончание минут:
    все минуты:
    minut=[1,21,31,41,51]
    minuti=[2,3,4,22,23,24,32,33,34,42,43,44,52,53,54]
    
    если минуты в minut: то число минут + "минута"
    если минуты в minuti: то число минут + "минуты"
    если остальные: то число минут + "минут"
    

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
    hour=time[:2]
    minn=time[3:]
    opmin=[i for i in range(1,61)]
    ophour=[i for i in range(24)]
    
    if len(time) == 5 and int(minn) in opmin and int(hour) in ophour and time[2]==" ":
        return False
    else:
        return True

def what_hour_text(hour):
    if 0 <= hour <= 5:
        return 'ночи'

    elif 6 <= hour <= 11:
        return 'утра'

    elif 12 <= hour <= 17:
        return 'дня'

    elif 18 <= hour <= 23:
        return 'вечера'

def what_hour(hour):
    if hour > 12:
        hour = hour - 12

    elif hour == 1:
        return str(hour) + ' ' + 'час'

    elif hour == 2 or hour == 3 or hour == 4:
        return str(hour) + ' ' + 'часа'

    else:
        return str(hour) + ' ' + 'часов'

def what_minute(min):
    minut=[1,21,31,41,51]
    minuti=[2,3,4,22,23,24,32,33,34,42,43,44,52,53,54]

    if min == 0:
        return 'ровно'
    elif min in minut:
        return str(min) + ' ' + 'минута'

    elif min in minuti:
        return str(min) + ' ' + 'минуты'

    else:
        return str(min) + ' ' +'минут'

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
    a=str(input())
    if osibka(a):
        print('Введены недопустимые данные')
    else:
        hor=int(a[:2])
        min=int(a[3:])
        print(tour_to_text(hor,min))

if __name__ == "__main__":
    main()










