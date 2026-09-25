import datetime, locale

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

print('Введите дату рождения в формате дд.мм.гггг')
day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождаения: "))
year = int(input("Введите год рождения: "))
date = datetime.date(year, month, day)
now_date = datetime.date.today().year

print(f"Ваша дата рождения: {day}.{month}.{year}")

digits = {
    '0' : ['***', '* *', '* *', '* *', '* *', '***'],
    '1' : ['  *', ' **', '* *', '  *', '  *', '  *'],
    '2' : ['***', '  *', '  *', '***', '*  ', '***'],
    '3' : ['***', '  *', '***', '  *', '  *', '***'],
    '4' : ['* *', '* *', '***', '  *', '  *', '  *'],
    '5' : ['***', '*  ', '***', '  *', '  *', '***'],
    '6' : ['***', '*  ', '***', '* *', '* *', '***'],
    '7' : ['***', ' * ', '*  ', '*  ', '*  ', '*  '],
    '8' : ['***', '* *', '* *', '***', '* *', '* *'],
    '9' : ['***', '* *', '***', '  *', '  *', '***']
}

def print_date_stars(date_list):
    digits_only = (
        str(date_list[0]).zfill(2) +
        str(date_list[1]).zfill(2) +
        str(date_list[2])
    )

    chars_to_print = list(digits_only[:2]) + [' '] + list(digits_only[2:4]) + [' '] + list(digits_only[4:])

    for i in range(6):
        line = ''
        for c in chars_to_print:
            if c == ' ':
                line += '   '
            else:
                line += digits.get(c, '')[i]
            line += '  '
        print(line.rstrip())

print_date_stars([day, month, year])

def getweekday(date=date):
    weekday = date.strftime("%A")
    print(f"День недели введенной даты: {weekday}")

def is_leap_year(year=year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print (f'{year} год был високосным')
    else:
        print (f'{year} год был не високосным')

def get_age (year=year, now_date=now_date):
    get_age = now_date - year
    if 10 < get_age < 20:
        suf = 'лет'
    else:
        last_digit = get_age % 10
        if last_digit == 1:
            suf = 'год'
        elif last_digit in (2, 3, 4):
            suf = 'года'
        else:
            suf = 'лет'
    print(f"Ваш возраст: {get_age} {suf}")

getweekday()
is_leap_year()
get_age()