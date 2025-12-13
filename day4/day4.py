#!/usr/bin/python
import unittest

def veins(coord_y, coord_x):
    return [(coord_y - 1, coord_x - 1),
            (coord_y - 1, coord_x),
            (coord_y - 1, coord_x + 1),
            (coord_y, coord_x - 1),
            (coord_y, coord_x + 1),
            (coord_y + 1, coord_x - 1),
            (coord_y + 1, coord_x),
            (coord_y + 1, coord_x + 1)]

def parse_data(data):
    taula = []
    for line in data.splitlines():
        fila = []
        for c in line:
            fila.append(c == '@')
        taula.append(fila)
    return taula

def part1(data):
    taula = parse_data(data)
    count = 0
    for i in range(len(taula)):
        for j in range(len(taula[i])):
            if taula[i][j]:
                loc_count = 0
                for v in veins(i, j):
                    if v[0] >= 0 and v[0] < len(taula) and v[1] >= 0 and v[1] < len(taula[v[0]]):
                        if taula[v[0]][v[1]]:
                            loc_count += 1
                            if loc_count >= 4:
                                break
                if loc_count < 4:
                    count += 1
    return count

def purga_taula(taula):
    res = []
    removed = 0
    for i in range(len(taula)):
        fila = []
        for j in range(len(taula[i])):
            if taula[i][j]:
                loc_count = 0
                for v in veins(i,j):
                    if v[0] >= 0 and v[0] < len(taula) and v[1] >= 0 and v[1] < len(taula[v[0]]):
                        if taula[v[0]][v[1]]:
                            loc_count += 1
                            if loc_count >= 4:
                                break
                fila.append(loc_count >= 4)
                removed += loc_count < 4
            else:
                fila.append(False)
        res.append(fila)
    return (removed, res)


def part2(data):
    taula = parse_data(data)
    removed = 1
    acc = 0
    while removed > 0:
        (removed, taula) = purga_taula(taula)
        acc += removed
    return acc

def main():

    with open("input.txt") as f:
        data = f.read()
        part = input("Quina part vols fer? [1/2/T]: ")
        if part == "1":
            res = part1(data)
            print(res)
        elif part == "2":
            res = part2(data)
            print(res)
        elif part == "T" or part == "t":
            unittest.main()
        else:
            print("Part no vàlida!")

class UnitTests(unittest.TestCase):

    def setUp(self):
        self.file_test = open("test.txt")
        self.file_input = open("input.txt")

    def tearDown(self):
        self.file_test.close()
        self.file_input.close()

    def test_test1(self):
        data = self.file_test.read()
        res = part1(data)
        self.assertEqual(res, 13)

    def test_input1(self):
        data = self.file_input.read()
        res = part1(data)
        self.assertEqual(res, 1540)

    def test_test2(self):
        data = self.file_test.read()
        res = part2(data)
        self.assertEqual(res, 43)

    def test_input2(self):
        data = self.file_input.read()
        res = part2(data)
        self.assertEqual(res, 8972)

if __name__ == "__main__":
    main()
