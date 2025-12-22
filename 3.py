# ЕГЭ Задача 3: Работа со строками
# Обработка текстовой информации

def task3_solution():
    """
    Задача: Посчитать количество различных символов в строке
    """
    s = input("Введите строку: ")
    unique_chars = len(set(s))
    return unique_chars

if __name__ == "__main__":
    result = task3_solution()
    print(f"Количество различных символов: {result}")
