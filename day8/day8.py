import unittest

def distsq(x,y):
    return (x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2

def part1(file, bound):
    posicions = {}
    distancies = []
    identificador = 0
    for line in file:
        x,y,z = map(int, line.split(',',2))
        for ident in posicions:
            distancia = distsq(posicions[ident], (x,y,z))
            distancies.append((distancia, (ident, identificador)))
        posicions[identificador] = (x,y,z)
        identificador += 1
    distancies.sort(key = lambda tup: tup[0])

    circuits = []
    for i in range(bound):
        parella = distancies[i][1]
        circuits_a_unir = []
        for c in circuits:
            if parella[0] in c or parella[1] in c:
                circuits_a_unir.append(c)
                if len(circuits_a_unir) >= 2:
                    break
        if len(circuits_a_unir) == 2:
            nou = circuits_a_unir[0] | circuits_a_unir[1]
            circuits.remove(circuits_a_unir[0])
            circuits.remove(circuits_a_unir[1])
            circuits.append(nou)
        elif len(circuits_a_unir) == 1:
            circuits_a_unir[0].add(parella[0])
            circuits_a_unir[0].add(parella[1])
        else:
            nou = {parella[0], parella[1]}
            circuits.append(nou)
    longs = [ len(c) for c in circuits ]
    longs.sort(reverse=True)
    return longs[0] * longs[1] * longs[2]

def part2(file):
    posicions = {}
    distancies = []
    identificador = 0
    for line in file:
        x,y,z = map(int, line.split(',',2))
        for ident in posicions:
            distancia = distsq(posicions[ident], (x,y,z))
            distancies.append((distancia, (ident, identificador)))
        posicions[identificador] = (x,y,z)
        identificador += 1
    distancies.sort(key = lambda tup: tup[0])

    circuits = []
    for _, parella in distancies:
        circuits_a_unir = []
        for c in circuits:
            if parella[0] in c or parella[1] in c:
                circuits_a_unir.append(c)
                if len(circuits_a_unir) >= 2:
                    break
        if len(circuits_a_unir) == 2:
            nou = circuits_a_unir[0] | circuits_a_unir[1]
            circuits.remove(circuits_a_unir[0])
            circuits.remove(circuits_a_unir[1])
            circuits.append(nou)
        elif len(circuits_a_unir) == 1:
            circuits_a_unir[0].add(parella[0])
            circuits_a_unir[0].add(parella[1])
        else:
            nou = {parella[0], parella[1]}
            circuits.append(nou)

        if len(circuits) == 1 and len(circuits[0]) == len(posicions):
            x0 = posicions[parella[0]][0]
            x1 = posicions[parella[1]][0]
            return x0 * x1


def main():
    with open("input.txt") as f:
        part = input("Quina part vols fer? [1/2/T]: ")
        if part == "1":
            res = part1(f, 1000)
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
        res = part1(self.file_test, 10)
        self.assertEqual(res, 40)

    def test_input1(self):
        res = part1(self.file_input, 1000)
        self.assertEqual(res, 67488)

    def test_test2(self):
        res = part2(self.file_test)
        self.assertEqual(res, 25272)

    def test_input2(self):
        res = part2(self.file_input)
        self.assertEqual(res, 3767453340)

if __name__ == "__main__":
    main()
