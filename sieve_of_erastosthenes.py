import unittest, random


class SieveOfErastosthenes:
    def __init__(self):
        self.prime = []

    def my_compute_primes(self, number):
        self.prime = [c for c in range(2, number + 1)]
        for x in range(2, number + 1):
            for y in range(2, number + 1):
                res = x * y
                if res > number:
                    break
                elif res not in self.prime:
                    continue
                else:
                    self.prime.remove(res)

    def compute_primes(self, number):
        prime_list = []
        for i in range(2, number + 1):
            if i not in prime_list:
                self.prime.append(i)
                for j in range(i * i, number + 1, i):
                    prime_list.append(j)


class Test(unittest.TestCase):

    def __init__(self, x):
        self.siv1 = SieveOfErastosthenes()
        self.siv2 = SieveOfErastosthenes()
        super().__init__(x)

    def test(self):
        self.siv1.my_compute_primes(20)
        self.assertEqual(self.siv1.prime, [2, 3, 5, 7, 11, 13, 17, 19])

    def test_methods(self):
        i = random. randint(10, 1000000)
        # print(i)
        self.siv1.my_compute_primes(i)
        self.siv2.compute_primes(i)
        self.assertEqual(self.siv1.prime, self.siv2.prime)


if __name__ == '__main__':
    unittest.main()
