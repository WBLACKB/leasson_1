# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Введите целое положительное число > "))

temp = str(n)
nn = temp + temp
nnn = temp + temp + temp
summ = n + int(nn) + int(nnn)

print(summ)
