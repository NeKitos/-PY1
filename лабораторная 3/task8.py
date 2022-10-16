money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
loss = salary - (spend + (spend * (month * increase)))
ostatok = money_capital + loss

while ostatok >= 0:
    ostatok = money_capital + loss
    month += 1
    loss = salary - (spend + (spend * (month * increase)))
    money_capital += loss

print(month)
