import unittest

def invalid_ids(range_a, range_b):
    length_a = len(range_a)
    length_b = len(range_b)
    range_a = int(range_a)
    range_b = int(range_b)
    res = []
    for l in range(length_a, length_b + 1):
        if l % 2 == 0 and l > 0:
            l /= 2
            maximum = pow(10,l)
            x = pow(10,l-1)
            while x < maximum:
                number = x * maximum + x
                if number >= range_a:
                    if number > range_b:
                        break
                    else:
                        res.append(number)
                x += 1
    return res

def part1(data):
    res = 0
    for pair in data.split(','):
        pair = pair.split('-')
        invalids = invalid_ids(pair[0], pair[1])
        res += sum(invalids)
    return res

def invalid_sum2(range_a, range_b):
    elements = set()
    # print("---------------------")
    # print(range_a + "-" + range_b)
    length_a = len(range_a)
    length_b = len(range_b)
    range_a = int(range_a)
    range_b = int(range_b)
    for l in range(1, length_b//2 + 1):
        repetitions = 2
        while l * repetitions <= length_b:
            if l * repetitions >= length_a:
                for n in range(pow(10,l-1), pow(10, l)):
                    number = int(str(n) * repetitions)
                    if number >= range_a:
                        if number <= range_b:
                            elements.add(number)
                            # print(elements)
                        else:
                            break

            repetitions += 1

    return sum(elements)

def part2(data):
    res = 0
    for pair in data.split(','):
        pair = pair.split('-')
        res += invalid_sum2(pair[0], pair[1])
    return res

def main():
    with open("input.txt") as f:
        data = f.read().replace('\n', '')
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
        data = self.file_test.read().replace('\n', '')
        res = part1(data)
        self.assertEqual(res, 1227775554)

    def test_input1(self):
        data = self.file_input.read().replace('\n', '')
        res = part1(data)
        self.assertEqual(res, 19128774598)

    def test_test2(self):
        data = self.file_test.read().replace('\n', '')
        res = part2(data)
        self.assertEqual(res, 4174379265)

    def test_input2(self):
        data = self.file_input.read().replace('\n', '')
        res = part2(data)
        self.assertEqual(res, 21932258645)

if __name__ == "__main__":
    main()
