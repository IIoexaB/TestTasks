import math

n = 4
m = 3

def task_1(n, m):
    """Функция для решения первого задания"""
    array = list(range(1, n + 1))
    result = []
    first_element = 1
    result.append(first_element)
    while True:
        second_element = (first_element + m - 1) % n + 1
        result.append(second_element)
        if second_element == 1:
            break
        first_element = second_element
        return result

result = task_1(n, m)

print(f"Путь: {result}")