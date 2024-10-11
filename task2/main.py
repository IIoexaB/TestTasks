import sys
import math

def calculate_position(x_center, y_center, radius, x_point, y_point):
    """Функция, определяющая положение точки относительно окружности
    """
    distance = math.sqrt((x_point - x_center)^2 + (y_point - y_center)^2)
    if abs(distance - radius) < 1e-6:  # Проверка на равенство с учетом погрешности
        return 0
    elif distance < radius:
        return 1
    else:
        return 2

def main():
    """
    Основная функция программы.
    """
    if len(sys.argv) != 3:
        print("Неверное количество аргументов! Требуется два файла: файл с координатами окружности и файл с координатами точек.")
        return

    circle_file_path = r"C:\\Users\\Рамиль\\Desktop\\ТЗ\\file1.txt"
    points_file_path = r"C:\\Users\\Рамиль\\Desktop\\ТЗ\\file2.txt"

    try:
        with open(circle_file_path, 'r') as circle_file:
            x_center, y_center, radius = map(float, circle_file.read().split())
    except FileNotFoundError:
        print(f"Файл с координатами окружности '{circle_file_path}' не найден!")
        return
    except ValueError:
        print(f"Неверный формат данных в файле '{circle_file_path}'!")
        return

    try:
        with open(points_file_path, 'r') as points_file:
            for line in points_file:
                x_point, y_point = map(float, line.split())
                position = calculate_position(x_center, y_center, radius, x_point, y_point)
                print(position)
    except FileNotFoundError:
        print(f"Файл с координатами точек '{points_file_path}' не найден!")
        return
    except ValueError:
        print(f"Неверный формат данных в файле '{points_file_path}'!")
        return

if __name__ == "__main__":
    main()