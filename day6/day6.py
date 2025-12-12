import unittest
import math

def part1(file):
    taula = []
    for line in file:
        if any(char.isdigit() for char in line):
            taula.append(list(map(int, line.split())))
        else:
            res = 0
            for i, symb in enumerate(line.split()):
                if symb == '+':
                    for fila in taula:
                        res += fila[i]
                else:
                    prod = 1
                    for fila in taula:
                        prod *= fila[i]
                    res += prod
            return res

def part2(file):
    data = file.read()
    data = list(data.splitlines())
    L = len(data[0])
    number_list = []
    result = 0
    for j in range(L-1, -1, -1):
        current_num = 0
        flag_operate = False
        for i in range(len(data)):
            if data[i][j].isdigit():
                current_num *= 10
                current_num += int(data[i][j])
            elif data[i][j] == '+':
                res = sum(number_list) + current_num
                result += res
                flag_operate = True
            elif data[i][j] == '*':
                res = math.prod(number_list) * current_num
                result += res
                flag_operate = True
        if flag_operate:
            number_list = []
        elif current_num != 0:
            number_list.append(current_num)
    return result

def main():
    with open("input.txt") as f:
        part = input("Quina part vols fer? [1/2/T]: ")
        if part == "1":
            res = part1(f)
            print(res)
        elif part == "2":
            res = part2(f)
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
        res = part1(self.file_test)
        self.assertEqual(res, 4277556)

    def test_input1(self):
        res = part1(self.file_input)
        self.assertEqual(res, 5873191732773)

    def test_test2(self):
        res = part2(self.file_test)
        self.assertEqual(res, 3263827)

    def test_input2(self):
        res = part2(self.file_input)
        self.assertEqual(res, 11386445308378)

if __name__ == "__main__":
    main()
