from typing import List
import sys


def dfs_alg(matrix: list, shape: tuple, x: int, y: int) -> None:
    """Рекурсивным алгоритмом обхода графа: поиском в глубину, определяем границы лунного кратера."""
    if matrix[x][y] == 0:
        return
    # Отмечаем место как "посещённое", меняя значение в координате с 1 на 0
    matrix[x][y] = 0
    # Двигаемся вертикально ВВЕРХ, если не находимся в первой строчке
    if x != 0:
        dfs_alg(matrix, shape, x - 1, y)
    # Двигаемся горизонтально ВЛЕВО, если не находимся в первой колонке
    if y != 0:
        dfs_alg(matrix, shape, x, y - 1)
    # Двигаемся вертикально ВНИЗ, если не находимся в последней строчке
    if x != shape[0] - 1:
        dfs_alg(matrix, shape, x + 1, y)
    # Двигаемся горизонтально ВПРАВО, если не находимся в последней колонке
    if y != shape[1] - 1:
        dfs_alg(matrix, shape, x, y + 1)


def calculate(moon_map: list) -> int:
    """Вычисляем количество кратеров на бинарной карте."""
    # Параметры бинарной карты (строки х столбцы)
    shape = (len(moon_map), len(moon_map[0]))
    craters = 0
    for x in range(shape[0]):
        for y in range(shape[1]):
            if moon_map[x][y] == 1:
                dfs_alg(moon_map, shape, x, y)
                craters += 1
    return craters


def text_to_list(text_line: str) -> list:
    """Преобразуем данные типа строка в список."""
    res_list = []
    i = 0
    while i != len(text_line) - 1:
        temp_list: List[int] = []
        res_list.append(temp_list)
        for char in text_line[i:]:
            i += 1
            if char.isdigit():
                temp_list.append(int(char))
            if char == "]":
                break
    return res_list


def main(file_name: str) -> None:
    """Открываем текстовый файл с бинарной картой лунной поверхности и запускаем программу подсчёта лунных кратеров."""
    try:
        fp = open(file_name, mode="r")
        line = fp.readline()
        while line:
            text_line = line.rstrip("\n")
            moon_map_as_list = text_to_list(text_line)
            print("Кратеров на данном участке поверхности луны:", calculate(moon_map_as_list))
            line = fp.readline()
        fp.close()
        sys.exit(0)
    except OSError:
        print(f"Ошибка! Файл {file_name} не найден!")
    except SystemExit:
        print("--Программа завершена--")


if __name__ == "__main__":
    main("example.txt")
