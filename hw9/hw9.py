# 1. напишіть функцію, яка перевірить, чи передане їй число є парним чи непарним (повертає True False)

def is_number_even(number):

    if number % 2 == 0:
        return True
    else:
        return False


assert type(is_number_even(6)) == bool
assert is_number_even(5) is False, 'If number is odd function should return False'
assert is_number_even(6) is True, 'If number is even function should return True'
assert is_number_even(2.0) is True, 'If number is even function should return True'
assert is_number_even(2.5) is False, 'If number is odd function should return False'


# 2. напишіть функцію. яка приймає стрічку, і визначає, чи дана стрічка відповідає
# результатам роботи методу capitalize()
# (перший символ є верхнім регістром, а решта – нижнім.) (повертає True False)
# написати до кожної функції мінімум 5 assert


def is_string_capitalize(string):

    if string == string.capitalize():
        return True
    else:
        return False


assert type(is_string_capitalize('')) == bool
assert is_string_capitalize('Aaron is good looking noob') is True
assert is_string_capitalize('aaron is good looking noob') is False
assert is_string_capitalize('Aaron' * 2) is False
assert is_string_capitalize('123') is True

# 3. написати декоратор, який додає принт з результатом роботи отриманої функції + текстовий параметр,
# отриманий ним (декоратор з параметром - це там, де три функції)
# при цьому очікувані результати роботи функції не змінюються (декоратор просто додає принт)


def add_result_and_text(txt: str):

    def real_decorator(func):
        def wrapper(*args, **kwargs):
            new_list = func(*args, **kwargs)
            print(txt, new_list)

            return new_list

        return wrapper

    return real_decorator


@add_result_and_text('i am sure result is')
def add_element_to_list(my_list):
    my_list.append(1)

    return my_list


my_list = [1, 2, 3]
my_list = add_element_to_list(my_list)
