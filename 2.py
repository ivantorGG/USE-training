# ЕГЭ Задача 2: Логические операции
# Определение истинности логических высказываний

def task2_solution():
    """
    Задача: Проверить, являются ли три числа сторонами треугольника
    """
    a = float(input("Введите сторону a: "))
    b = float(input("Введите сторону b: "))
    c = float(input("Введите сторону c: "))
    
    # Условия для треугольника
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

if __name__ == "__main__":
    result = task2_solution()
    print(f"Является ли треугольником: {result}")
