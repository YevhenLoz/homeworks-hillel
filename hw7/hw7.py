# Напишіть програму "Касир в кінотеатрі", яка буде виконувати наступне:
# попросіть користувача ввести свій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить 7 - вивести "Вам <>, вам пощастить"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів все одно нема!"
# Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
# Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача
# (1 - рік, 22 - роки, 35 - років і тд...).
# Наприклад :
# "Тобі ж 5 років! Де твої батьки?"
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
# "Попри те, що вам 42 роки, білетів все одно нема!"
# Зробіть все за допомогою функцій!
# Не забувайте, що кожна функція має виконувати тільки одне завдання і про правила написання коду.

def check_age():
    userinput = input('Будь-ласка, введіть ваш вік: ')

    if userinput.isalpha() or not userinput.isdigit():
        print('Помилка! Вік має бути цілим позитивним числом')
    return userinput


userinput = check_age()


def year_form():
    form1 = 'рік'
    form2 = 'роки'
    form3 = 'років'

    if userinput.startswith('1') and len(userinput) == 1:
        year = form1
    elif userinput.endswith('1') and userinput.startswith(('2', '3', '4', '5', '6', '7', '8', '9', '10', '12')):
        year = form1
    elif userinput.endswith(('2', '3', '4')) and userinput.startswith(('2', '3', '4', '5', '6', '7', '8', '9', '10')):
        year = form2
    elif userinput.endswith(('5', '6', '7', '8', '9', '0', '11', '12', '13', '14', '15', '16', '17', '18', '19')):
        year = form3
    else:
        year = ''
    return year


year = year_form()


def print_dialog():
    if userinput.isdigit():
        ageint = int(userinput)
        if '7' in str(ageint) and ageint < 120:
            print(f'Вам {ageint} {year}, вам пощастить')
        else:
            if 0 < ageint < 7:
                print(f'Тобі ж {ageint} {year}! Де твої батьки?')
            elif 7 < ageint < 16:
                print(f'Тобі лише {ageint} {year}, а це це фільм для дорослих!')
            elif 120 >= ageint > 65:
                print(f'Вам {ageint} {year}? Покажіть пенсійне посвідчення!')
            elif ageint > 120:
                print(f'Вам {ageint} {year}? Стільки не живуть!')
            elif ageint == 0:
                print('Введіть справжній вік!')
            else:
                print(f'Незважаючи на те, що вам {ageint} {year}, білетів все одно нема!')


print_dialog()
