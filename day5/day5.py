#!/usr/bin/python
import unittest


def insert_interval(collection, interval):
    # Esquerra de l'interval
    insert_left = 0
    while insert_left < len(collection) and collection[insert_left] < interval[0]:
        insert_left += 1

    insert_right = insert_left
    while insert_right < len(collection) and collection[insert_right] < interval[1]:
        insert_right += 1

    if insert_left >= len(collection):
        collection.append(interval[0])
        collection.append(interval[1])
    else:
        # Primer ajustem la part de la dreta
        if insert_right % 2 == 0:
            # Parell, per tant entre `i-1` i `i` és fora d'interval
            if insert_right < len(collection) and collection[insert_right] == interval[1]:
                # Hem d'eliminar aquest principi d'interval
                insert_right += 1
            else:
                # Altrament, hem d'inserir el final d'interval i eliminar fins just a la seva esquerra
                collection.insert(insert_right, interval[1])

        # Ajustem la part de l'esquerra
        if insert_left % 2 == 0:
            # Parell, per tant entre `i-1` i `i` és fora d'interval
            # Hem d'inserir el principi d'interval i desplaçar els índexs d'eliminació
            collection.insert(insert_left, interval[0])
            insert_left += 1
            insert_right += 1

        # Eliminem
        del collection[insert_left:insert_right]

def collect_intervals(string):
    intervals = []
    for line in string.splitlines():
        a, b = map(int, line.split('-',1))
        insert_interval(intervals, (a,b))
    return intervals

def part1(data):
    first, second = data.split("\n\n")
    intervals = collect_intervals(first)

    fresh = 0
    for line in second.splitlines():
        num = int(line)
        for i in range(0,len(intervals),2):
            if intervals[i] <= num and num <= intervals[i+1]:
                fresh += 1
                break
    return fresh

def part2(data):
    first, _ = data.split("\n\n")
    intervals = collect_intervals(first)

    suma = 0
    for i in range(0, len(intervals), 2):
        suma += intervals[i+1] - intervals[i] + 1
    return suma

def main():
    with open("input.txt") as f:
        data = f.read().strip()
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
        self.assertEqual(res, 3)

    def test_input1(self):
        data = self.file_input.read()
        res = part1(data)
        self.assertEqual(res, 868)

    def test_test2(self):
        data = self.file_test.read()
        res = part2(data)
        self.assertEqual(res, 14)

    def test_input2(self):
        data = self.file_input.read()
        res = part2(data)
        self.assertEqual(res, 354143734113772)

if __name__ == "__main__":
    main()
