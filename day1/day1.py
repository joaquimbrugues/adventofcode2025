#!/usr/bin/python

import unittest

def part1(file):
    res = 0
    dial_pos = 50
    for line in file:
        dist = int(line[1:])
        # Movem l'agulla: si tenim LXX la movem XX a l'esquerra, si tenim RXX la movem XX a la dreta
        if line[0] == 'L':
            dial_pos -= dist
        else:
            dial_pos += dist
        # Apliquem el mòdul (a Python el resultat del mòdul té el mateix signe que el denominador)
        dial_pos %= 100
        # Si caiem al 0, ho comptem
        if dial_pos == 0:
            res += 1
    return res

def part2(file):
    res = 0
    dial_pos = 50
    for line in file:
        dist = int(line[1:])
        # Movem l'agulla: si tenim LXX la movem XX a l'esquerra, si tenim RXX la movem XX a la dreta
        if line[0] == 'L':
            if dial_pos == 0:
                res -= 1
            dial_pos -= dist
            # Fem la divisió euclidiana (a Python, el residu sempre tindrà el mateix signe que el denominador: això vol dir, per exemple, que -1 // 100 = -1)
            res += abs(dial_pos // 100)
            dial_pos %= 100
            if dial_pos == 0:
                res += 1
        else:
            dial_pos += dist
            res += abs(dial_pos // 100)
            dial_pos %= 100
            # En el cas positiu, si acabem a 0 això ja està comptat a la divisió euclidiana
    return res

def main():
    f = open("input.txt")
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
        self.assertEqual(res, 3)

    def test_input1(self):
        res = part1(self.file_input)
        self.assertEqual(res, 1191)

    def test_test2(self):
        res = part2(self.file_test)
        self.assertEqual(res, 6)

    def test_input2(self):
        res = part2(self.file_input)
        self.assertEqual(res, 6858)

if __name__ == "__main__":
    main()
