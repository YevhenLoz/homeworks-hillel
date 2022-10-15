# 1. напишіть функцію, яка перевірить, чи передане їй число є парним чи непарним (повертає True False)
print('Задача 1')

def even_odd_checker(num):
    """
    Function checks the number is even or odd
    :param num:
    :return: True or False
    """
    if num % 2:
        return True
    else:
        return False


m = 6

if even_odd_checker(m):
    print(m, "is an even number")
else:
    print(m, "is an odd number")

print(type(even_odd_checker(m)))


assert type(even_odd_checker(m)) is bool, 'Function should return bool'
assert type(m) is int, 'Function should receive int'
assert m >= 0, 'Function should receive positive numbers'




# 2. напишіть функцію. яка приймає стрічку, і визначає, чи дана стрічка відповідає
# результатам роботи методу capitalize()
# (перший символ є верхнім регістром, а решта – нижнім.) (повертає True False)
#написати до кожної функції мінімум 5 assert

print('Задача 2')

def check_capitalize(text):
    """
    Function to check is string is capitalized or not
    :param text:
    :return: True or False
    """
    if text == text.capitalize():
        return True
    else:
        return False


text = ' Aaron'

if check_capitalize(text):
    print('String capitalized')
else:
    print('String starts in lower case')

print(type(check_capitalize(text)))

assert type(check_capitalize(text)) is bool, 'Function should return bool'
assert type(text) == str, 'Function should receive string'



# 3. написати декоратор, який додає принт з результатом роботи отриманої функції + текстовий параметр,
# отриманий ним (декоратор з параметром - це там, де три функції)
# # при цьому очікувані результати роботи функції не змінюються (декоратор просто добавляє принт)
print('Задача 3')

def add_result_and_text(txt: str):
    print(txt)

    def real_decorator(func):
        def wrapper(*args, **kwargs):
            new_list = func(*args, **kwargs)
            print('Result list =', new_list)

            return new_list

        return wrapper

    return real_decorator


@add_result_and_text('Add element to list')
def add_element_to_list(lst1):
    lst1.append(1)

    return lst1


my_list = [1, 2, 3]
my_list = add_element_to_list(my_list)
