import sys
import math

def read_circle(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        center_x, center_y = map(int, data[0].split())
        radius = int(data[1])
        return (center_x, center_y), radius

def read_dot(file_path):
    with open(file_path, 'r') as file:
        points = []
        for line in file:
            x, y = map(int, line.split())
            points.append((x, y))
        return points

def point_position(center, radius, point):
    distance = math.sqrt((point[0] - center[0])**2 + (point[1] - center[1])**2)
    if distance < radius:
        return 1  # Точка внутри окружности
    elif distance == radius:
        return 0  # Точка на окружности
    else:
        return 2  # Точка снаружи окружности

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task2.py circle dot")
    else:
        circle_center, circle_radius = read_circle(sys.argv[1])
        points = read_dot(sys.argv[2])
        for point in points:
            print(point_position(circle_center, circle_radius, point))
