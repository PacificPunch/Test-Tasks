import sys

def find_path(n, m):
    # Создаем круговой массив
    circular_array = [i+1 for i in range(n)]
    
    # Находим путь
    path = [circular_array[0]]
    current_index = 0
    while True:
        current_index = (current_index + m - 1) % n
        path.append(circular_array[current_index])
        if circular_array[current_index] == circular_array[0]:
            break
    
    return path[:-1]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    
    path = find_path(n, m)
    print("".join(map(str, path)))