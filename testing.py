import betterfunctions as bf
import functions as f
import unittest
import numpy as np
from pprint import pprint
from timeit import timeit

class TestProcessing(unittest.TestCase):

    np.random.seed(0)
    bagcount = 50  # np.random.randint(1, int(1e3))
    gamescount = 100  # np.random.randint(1, int(1e3))
    games = np.random.randint(1, int(1e6), size=gamescount)

    def test_processing_large_datasets_old(self):
        for _ in range(1):
            result = np.array(f.processing_data(self.bagcount, self.gamescount, self.games), dtype=np.uint64)
            self.assertEqual(len(result), self.bagcount)
            self.assertTrue(np.all(np.max(result, axis=0) - np.min(result, axis=0) <= 1))
            self.assertTrue(np.all(np.sum(result, axis=0) == self.games))
            bagssum = np.sum(result, axis=1)
            self.assertTrue(np.max(bagssum) - np.min(bagssum) <= 1)

    def test_processing_large_datasets_new(self):
        for _ in range(1):
            np.random.seed(0)
            result = np.array(bf.processing_data(self.bagcount, self.gamescount, self.games), dtype=np.uint64)
            self.assertEqual(len(result), self.bagcount)
            self.assertTrue(np.all(np.max(result, axis=0) - np.min(result, axis=0) <= 1))
            self.assertTrue(np.all(np.sum(result, axis=0) == self.games))
            bagssum = np.sum(result, axis=1)
            self.assertTrue(np.max(bagssum) - np.min(bagssum) <= 1)

    def test_speed(self):
        num = 1
        print("\nOLD:")
        fun = lambda: f.processing_data(self.bagcount, self.gamescount, self.games)
        print(t1:=timeit(fun, number=num)/num)
        print("\nNEW:")
        fun2 = lambda: bf.processing_data(self.bagcount, self.gamescount, self.games)
        print(t2:=timeit(fun2, number=num)/num)
        print(f'{t1/t2:.2f}x faster')

if __name__ == '__main__':
    unittest.main()
