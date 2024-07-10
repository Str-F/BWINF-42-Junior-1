import betterfunctions as bf
import functions as f
import unittest
import numpy as np
from timeit import timeit


class TestProcessing(unittest.TestCase):

    np.random.seed(0)
    bagcount = 50 # np.random.randint(1, int(1e3))
    gamescount = 100 # np.random.randint(1, int(1e3))
    games = np.random.randint(1, int(1e3), size=gamescount)

    def test_processing_large_datasets_old(self):
        for _ in range(1):

            result = np.array(f.processing_data(self.bagcount, self.gamescount, self.games), dtype=np.uint16)
            self.assertEqual(len(result), self.bagcount)

            self.assertTrue(np.all(np.max(result,  axis=0) - np.min(result, axis=0) <= 1))
            self.assertTrue(np.all(np.sum(result, axis=0) == self.games))
            bagssum = np.sum(result, axis=1)
            self.assertTrue(np.max(bagssum) - np.min(bagssum) <= 1)

    def test_processing_large_datasets_new(self):
        for _ in range(1):
            np.random.seed(0)

            result = np.array(bf.processing_data(self.bagcount, self.gamescount, self.games), dtype=np.uint16)
            self.assertEqual(len(result), self.bagcount)

            self.assertTrue(np.all(np.max(result, axis=0) - np.min(result, axis=0) <= 1))
            self.assertTrue(np.all(np.sum(result, axis=0) == self.games))
            bagssum = np.sum(result, axis=1)
            self.assertTrue(np.max(bagssum) - np.min(bagssum) <= 1)

    def test_speed(self):
        num = 100
        print("\nOLD:")
        fun = lambda: f.processing_data(self.bagcount, self.gamescount, self.games)
        print(timeit(fun, number=num))
        print("\nNEW:")
        fun2 = lambda: bf.processing_data(self.bagcount, self.gamescount, self.games)
        print(timeit(fun2, number=num))
            
if __name__ == '__main__':
    unittest.main()