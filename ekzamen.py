a=int(input("Введіть ціну однієї пляшки:"))
b=int(input("Введіть скільки Іванчик має грошей:"))
c=int(input("Ведіть кількість пляшок в автоматі:"))

def bottles(a,b,c):
    return min(b//a,c)

result = bottles(a,b,c)
print("Максимум Іванчик візьме", result , "пляшок")
