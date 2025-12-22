# ЕГЭ Задача 8: Рекурсия
# Использование рекурсивных функций

def task8_solution():
    """
    Задача: Вычислить факториал числа рекурсивно
    """
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    
    n = int(input("Введите число: "))
    result = factorial(n)
    return result

if __name__ == "__main__":
    result = task8_solution()
    print(f"Факториал: {result}")
