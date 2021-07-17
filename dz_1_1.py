duration = int(input('Введите колличество секунд'))

if duration < 60:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    minutes = duration // 60
    sec = duration - minutes * 60
    print(minutes, 'мин ', sec, 'сек')
elif 3600 <= duration < 86400:
    hours = duration // 3600
    minutes = (duration - hours * 3600) // 60
    sec = duration - minutes * 60 - hours * 3600
    print(hours, 'час ', minutes, 'мин ', sec, 'сек')

# Let's take the average value of days in a month = 30 (2592000sec)

elif 86400 <= duration < 2592000:
    days = duration // 86400
    hours = (duration - days * 86400) // 3600
    minutes = (duration - hours * 3600 - days * 86400) // 60
    sec = duration - minutes * 60 - hours * 3600 - days * 86400
    print(days, 'дней ', hours, 'час ', minutes, 'мин ', sec, 'сек')
elif 2592000 <= duration < 31536000:
    months = duration // 2592000
    days = (duration - months * 2592000) // 86400
    hours = (duration - months * 2592000 - days * 86400 ) // 3600
    minutes = (duration - hours * 3600 - days * 86400 - months * 2592000) // 60
    sec = duration - minutes * 60 - hours * 3600 - days * 86400 - months * 2592000
    print(months, 'месяцев', days, 'дней ', hours, 'час ', minutes, 'мин ', sec, 'сек')
else:
    years = duration // 31536000
    months = (duration - years * 31536000) // 2592000
    days = (duration - months * 2592000 - years * 31536000) // 86400
    hours = (duration - months * 2592000 - days * 86400 - years * 31536000) // 3600
    minutes = (duration - hours * 3600 - days * 86400 - months * 2592000 - years * 31536000) // 60
    sec = duration - minutes * 60 - hours * 3600 - days * 86400 - months * 2592000 - years * 31536000
    print(years, 'год(а)', months, 'месяцев', days, 'дней ', hours, 'час ', minutes, 'мин ', sec, 'сек')