# ЕГЭ Задача 6: Циклические алгоритмы
# Работа с циклами и итерациями

def task6_solution():
    """
    Задача: Найти сумму всех двузначных чисел, делящихся на 3
    """
    total = sum(n for n in range(10, 100) if n % 3 == 0)
    return total

if __name__ == "__main__":
    result = task6_solution()
    print(f"Сумма двузначных чисел, делящихся на 3: {result}")
