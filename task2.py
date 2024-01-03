meters = float(input("Введите метры: "))

choice = input("Перевести в: \n 1.Мили  \n 2.Дюймы \n 3.Ярды: ").lower()

if "1" in choice or "мили" in choice:
    miles = meters * 0.00062137
    print(f"{miles} миль в {meters} метрах.")
elif "2" in choice or "дюймы" in choice:
    inches = meters * 39.3701
    print(f"{inches} дюймов в {meters} метрах.")
elif "3" in choice or "ярды" in choice:
    yards = meters * 1.09361
    print(f"{yards} ярдов в {meters} метрах.")
else:
    print("Ошибка")
