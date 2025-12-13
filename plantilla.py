#!/usr/bin/python
import unittest

def part1(data):
    pass
def part2(data):
    pass

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
        self.assertEqual(res, 0)

    # def test_input1(self):
        # data = self.file_input.read()
        # res = part1(data)
        # self.assertEqual(res, 0)

    # def test_test2(self):
        # data = self.file_test.read()
        # res = part2(data)
        # self.assertEqual(res, 0)

    # def test_input2(self):
        # data = self.file_input.read()
        # res = part2(data)
        # self.assertEqual(res, 0)

if __name__ == "__main__":
    main()
