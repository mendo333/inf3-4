a = int(input("Введите первый член прогрессии: "))
d_or_q = input("Выберите тип прогрессии (d (арифметическая) / q (геометрическая)): ")

if d_or_q == "d":
    d = int(input("Введите разность прогрессии: "))
    n = int(input("Введите номер последнего члена: "))
    last_a = a + (n-1)*d
    sum_a = sum(range(a, last_a + d, d))
    sum_a_formula = ((2 * a + (n - 1) * d) / 2) * n
    print(f"Сумма арифметической прогрессии (цикл): {sum_a}")
    print(f"Сумма арифметической прогрессии (формула): {sum_a_formula}")

elif d_or_q == "q":
    q = int(input("Введите знаменатель прогрессии: "))
    n = int(input("Введите номер последнего члена: "))
    last_q = a * (q ** (n-1))
    if q == 1:
        sum_q = n * a
    else:
        sum_q = a * ((1 - (q ** n)) / (1 - q))
    sum_q_formula = a * ((1 - (q ** n)) / (1 - q))
    print(f"Сумма геометрической прогрессии (цикл): {sum_q}")
    print(f"Сумма геометрической прогрессии (формула): {sum_q_formula}")
