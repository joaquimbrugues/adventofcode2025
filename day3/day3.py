#!/usr/bin/python
import unittest

def part1(data):
    res = 0
    for line in data.splitlines():
        # Primer trobem el màxim de la línia (i si algun dígit és el 9 no cal que busquem més), juntament amb el seu índex
        imaxim = -1
        maxim = 0
        for i, c in enumerate(line[:-1]):
            n = int(c)
            if n > maxim:
                imaxim = i
                maxim = n
            if n == 9:
                break
        # Segon, busquem el màxim a la resta de la cadena
        mmaxim = 0
        for c in line[imaxim+1:]:
            n = int(c)
            if n > mmaxim:
                mmaxim = n
            if n == 9:
                break
        res_line = maxim * 10 + mmaxim
        res += res_line
    return res

def part2(data):
    res = 0
    for line in data.splitlines():
        current = 0
        left_limit = 0
        for pos in range(1,12):
            right_limit = 12 - pos
            imaxim = -1
            maxim = 0
            for i, c in enumerate(line[left_limit:-right_limit]):
                n = int(c)
                if n > maxim:
                    imaxim = i
                    maxim = n
                if n == 9:
                    break
            left_limit += imaxim + 1
            current *= 10
            current += maxim
        maxim = 0
        for c in line[left_limit:]:
            n = int(c)
            if n > maxim:
                maxim = n
            if n == 9:
                break
        current *= 10
        current += maxim
        res += current
    return res

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
        self.assertEqual(res, 357)

    def test_input1(self):
        data = self.file_input.read()
        res = part1(data)
        self.assertEqual(res, 17278)

    def test_test2(self):
        data = self.file_test.read()
        res = part2(data)
        self.assertEqual(res, 3121910778619)

    def test_input2(self):
        data = self.file_input.read()
        res = part2(data)
        self.assertEqual(res, 171528556468625)

if __name__ == "__main__":
    main()
