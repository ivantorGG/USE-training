# ЕГЭ Задача 7: Анализ массивов
# Работа с одномерными массивами

def task7_solution():
    """
    Задача: Найти максимальный элемент и его индекс в массиве
    """
    arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
    max_value = max(arr)
    max_index = arr.index(max_value)
    return max_value, max_index

if __name__ == "__main__":
    value, index = task7_solution()
    print(f"Максимальное значение: {value}, индекс: {index}")
