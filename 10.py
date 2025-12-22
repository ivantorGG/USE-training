# ЕГЭ Задача 10: Поиск и сортировка
# Использование алгоритмов поиска и сортировки

def task10_solution():
    """
    Задача: Отсортировать массив и найти элемент с бинарным поиском
    """
    arr = list(map(int, input("Введите элементы массива через пробел: ").split()))
    target = int(input("Введите элемент для поиска: "))
    
    arr.sort()
    
    # Бинарный поиск
    left, right = 0, len(arr) - 1
    found = False
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            found = True
            return found, mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return found, -1

if __name__ == "__main__":
    found, index = task10_solution()
    if found:
        print(f"Элемент найден на позиции: {index}")
    else:
        print("Элемент не найден")
