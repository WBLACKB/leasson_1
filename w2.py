# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

time = int(input("Введите время в секундах >"))


def convert(seconds):
    min, sec = divmod(seconds, 60)

    hour, min = divmod(min, 60)

    return "%d:%02d:%02d" % (hour, min, sec)


print(convert(time))
