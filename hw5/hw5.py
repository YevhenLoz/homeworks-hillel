#1.Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд.


my_text = 'Aaron is good looking Noob'
vowels = str.maketrans("aeiouAEIOU", "aaaaaaaaaa")
flagged = my_text.translate(vowels)
res = len([elem for elem in flagged.split() if elem.count(2*'a')])
print('Count of words with 2 vowels in row: ' + str(res))



#2. Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999,
# "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166,
# "the_partner": 38.988, "sota": 37.720, "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів,
# ціни яких попадають в діапазон між мінімальною і максимальною ціною.

lower_limit = 35.9
upper_limit = 37.339
my_dict = {
"cito": 47.999,
"BB_studio": 42.999,
"momo": 49.999,
"main-service": 37.245,
"buy.now": 38.324,
"x-store": 37.166,
"the_partner": 38.988,
"sota": 37.720,
"rozetka": 38.003
}

res = dict()
for key, value in my_dict.items():
    if lower_limit <= value <= upper_limit:
        print("Match : " + key)


