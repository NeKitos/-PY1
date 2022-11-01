money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
loss = salary - (spend + (spend * (month * increase)))


while money_capital >= (spend + (1 + increase)):
    month += 1
    loss = salary - (spend + (spend * (month * increase)))
    money_capital += loss

print(month)
