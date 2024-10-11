import math

def calculate_position(x_center, y_center, radius, x_point, y_point):
    distance = math.sqrt((x_point - x_center)**2 + (y_point - y_center)**2)
    if abs(distance - radius) < 1e-6:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2

def main():


    circle_file_path = r"C:\\Users\\Рамиль\\Desktop\\ТЗ\\file1.txt"
    points_file_path = r"C:\\Users\\Рамиль\\Desktop\\ТЗ\\file2.txt"

    try:
        with open(circle_file_path, 'r') as circle_file:
            x_center, y_center, radius = map(float, circle_file.read().split())
    except FileNotFoundError:
        print(f"Отсутствует файл с координатами окружности: '{circle_file_path}'")
        return


    try:
        with open(points_file_path, 'r') as points_file:
            for line in points_file:
                x_point, y_point = map(float, line.split())
                position = calculate_position(x_center, y_center, radius, x_point, y_point)
                print(position)
    except FileNotFoundError:
        print(f"Отсутствует файл с координатами точек: '{points_file_path}'")
        return


if __name__ == "__main__":
    main()