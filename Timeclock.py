'''
нахождение времи суток в словах:
    если время от 0 включительно до 6 невключительно 
        ночь
    если время от 6 включительно до 12 невключительно 
        утра
    если время от 12 включительно до 18 невключительно 
        дня
    если время от 18 включительно до 24 невключительно 
        вечера

нахождение окончания у часа:
    если колличество часов больше 12:
        вычитаем из них 12
    
    если осталось 1: 
        окончание час
    если осталось 2,3,4: 
        окончание часа
    иначе: 
        окончание часов
    
нахождение окончания у минут:
    если минуты начинаются с 1:
        окончание минут
    иначе:
        если минуты заканчиваются на 1:
            окончание минута
        если минуты заканчиваются на промежуток от 2 до 4:
            окончание минуты
        иначе:
            окончание минут
            
перевод времени в текст:
    если часы равны 0 и минуты равны 0:
        полночь
    если часы равны 12 и минуты равны 0:
        полдень
    иначе:
        обычный вывод
    
основная программа:
    вводим данные
    проверка на верный ввод
    если ввод неверный:
       сообщить об этом пользователю
       завершить программу
    иначе:
        перевод времени в текст
        вывод результата
        
    
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
    if str(minn)[0] == "1" and len(str(minn)) != 1:
        return "минут"
    else:
        if minn % 10 == 1:
            return "минута"
            
        elif 2 <= minn % 10 <= 4:
            return "минуты"
            
        else:
            return "минут"

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
    









