# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Пустые списки для простых и непростых чисел
primes = []
not_primes = []

# Перебор чисел из списка numbers
for number in numbers:
    if number < 2:  # Числа меньше 2 не являются простыми
        continue

    is_prime = True  # Флаг, изначально считаем число простым

    # Проверка на делимость числа number
    for i in range(2, int(number**0.5) + 1):  # Проверяем до корня из числа
        if number % i == 0:  # Если число делится на i, оно не простое
            is_prime = False
            break  # Прерываем цикл, дальнейшая проверка не нужна

    # Добавляем число в соответствующий список
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Вывод результатов
print("Primes:", primes)
print("Not Primes:", not_primes)
