num1 = int(input("Введите первую цифру: "))
num2 = int(input("Введите вторую цифру: "))
num3 = int(input("Введите третью цифру: "))

choice = input(
    "Узнать: \n 1.Максимальное  \n 2.Минимальное \n 3.Среднеарифметическое ").lower()

if "1" in choice or "максимальное" in choice or "максимум" in choice:
    maximum = max(num1, num2, num3)
    print(f"{maximum} самая большая цифра")
elif "2" in choice or "минимальное" in choice or "минимум" in choice:
    minimum = min(num1, num2, num3)
    print(f"{minimum} самая маленькая цифра")
elif "3" in choice or "среднеарифметическое" in choice or "среднее" in choice:
    average = (num1+num2+num3)/3
    print(f"{average} среднее арифметическое")
else:
    print("Ошибка")
