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
    if hour == 0:
        return 'ровно'
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
    if 0<=hour<=23 and 0<=minute<=59 and hour != None and minute != None:
        if hour == 0 and minute == 0:
            return print('Полночь')
        if hour == 12 and minute == 0:
            return print('Полдень')
        elif minute == 0:
            ig = what_hour(hour) + ' ' + what_hour_text(hour)+ ' ' + what_minute(minute)
            return ig
        else:
            ig = what_hour(hour) + ' ' + what_minute(minute) + ' ' + what_hour_text(hour)
            return ig
    else:
        return 'Введены недопустимые данные'

    # Справка:
    # 1 - час
    # 2, 3, 4 - часа
    # 5, 6, 7, 8, 9, 10, 11, 12 - часов
    # 1, 21, 31, 41, 51 - минута
    # 2-4, 22-24, 32-34, 42-44, 52, 53, 54 - минуты
    # Остальное - минут

a,b=map(int,input().split())
if a != None and b != None:
    print(tour_to_text(a,b))
else:
    print('Введены недопустимые данные')
    
