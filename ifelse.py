age = int(input("Введите возраст: ")) # запрос возраста у пользователя и преобразование в целое число
if age % 10 == 1 and age != 11: # если последняя цифра возраста равна 1 (кроме числа 11)
    print("Вам", age, "год.")
elif 1 < age % 10 < 5 and not 11 < age % 100 < 15: # если последняя цифра возраста равна 2, 3 или 4 (кроме чисел от 12 до 14)
    print("Вам", age, "года.")
else: # во всех остальных случаях
    print("Вам", age, "лет.")