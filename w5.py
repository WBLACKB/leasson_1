# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

profit = int(input("Введите доход: "))
outlay = int(input("Введите затраты: "))

if profit > outlay:
    gain = profit - outlay
    rent = gain / profit
    print(f"Прибыль составляет {gain}, рентабельность выручки {rent}")
    worker = int(input("ВВедите численость сотрудников: "))
    worker_gain = gain / worker
    print("Прибыль на одного сотрудника составляет", worker_gain)
elif profit == outlay:
    print("Доход равен расходу. Фирма вышла в ноль")
else:
    loss = outlay - profit
    print("Расход превышает прибыль. Убыток фирмы равен", loss)
