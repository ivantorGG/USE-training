# ЕГЭ Задача 9: Двумерные массивы (матрицы)
# Работа с двумерными массивами и матрицами

def task9_solution():
    """
    Задача: Транспонировать матрицу
    """
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    
    matrix = []
    print("Введите элементы матрицы (по строкам):")
    for i in range(rows):
        row = list(map(int, input(f"Строка {i+1}: ").split()))
        matrix.append(row)
    
    # Транспонирование
    transposed = [[matrix[i][j] for i in range(rows)] for j in range(cols)]
    
    return transposed

if __name__ == "__main__":
    result = task9_solution()
    print("Транспонированная матрица:")
    for row in result:
        print(row)
