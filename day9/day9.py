import unittest

def part1(file):
    maxim = 0
    coords = []
    for line in file:
        x,y = map(int, line.split(',',1))
        for xx, yy in coords:
            area = (abs(x - xx) + 1) * (abs(y - yy) + 1)
            if area > maxim:
                maxim = area
        coords.append((x,y))
    return maxim

def part2(file):
    pass

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
        self.assertEqual(res, 50)

    def test_input1(self):
        res = part1(self.file_input)
        self.assertEqual(res, 4746238001)

    def test_test2(self):
        res = part2(self.file_test)
        self.assertEqual(res, 24)

    # def test_input2(self):
        # res = part2(self.file_input)
        # self.assertEqual(res, 0)

if __name__ == "__main__":
    main()
