# 1.Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Зауважте, що lst1 не є статичним і може формуватися динамічно.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for elem in lst1:
    if type(elem) == str:
        lst2.append(elem)
print("List with strings:  " + str(lst2))

# 2.Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44].
# Напишіть код, який видалить з нього всі числа, які менш як 21 і більше ніж 74.

lst3 = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]
lst3 = [elem for elem in lst3 if 21 < elem < 74]
print("List of  21 < digits < 74:  " + str(lst3))

# 3. Є стрінг з певним текстом (можна скористатися input або константою).
# Напишіть код, який визначить кількість слів в цьому тексті, які закінчуються на 'о'.

my_text = 'Go and visit archipelago fantastico'
letter = 'o'
res = len([elem for elem in my_text.split() if elem.endswith(letter)])
print("Words that end with letter o count:  " + str(res))



