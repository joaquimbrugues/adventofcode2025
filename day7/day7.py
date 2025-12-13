#!/usr/bin/python
import unittest

def part1(file):
    flag_first = True
    positions = []
    result = 0
    for line in file:
        if flag_first:
            # Read first line
            positions = [c == 'S' for c in line]
            flag_first = False
        else:
            # Potential splitters
            for i, c in enumerate(line):
                if c == '^' and positions[i]:
                    if i > 0:
                        positions[i-1] = True
                    if i + 1 < len(positions):
                        positions[i+1] = True
                    positions[i] = False
                    result += 1
    return result

def part2(file):
    flag_first = True
    timelines = []
    for line in file:
        if flag_first:
            # Read first line
            timelines = [c == 'S' for c in line]
            flag_first = False
        else:
            # Potential splitters
            for i, c in enumerate(line):
                if c == '^' and timelines[i] > 0:
                    if i > 0:
                        timelines[i-1] += timelines[i]
                    if i + 1 < len(timelines):
                        timelines[i+1] += timelines[i]
                    timelines[i] = 0
    return sum(timelines)

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
        self.assertEqual(res, 21)

    def test_input1(self):
        res = part1(self.file_input)
        self.assertEqual(res, 1667)

    def test_test2(self):
        res = part2(self.file_test)
        self.assertEqual(res, 40)

    def test_input2(self):
        res = part2(self.file_input)
        self.assertEqual(res, 62943905501815)

if __name__ == "__main__":
    main()
