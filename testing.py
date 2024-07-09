from functions import processing_data
import unittest
import numpy as np


class TestProcessing(unittest.TestCase):

    def test_processing_large_datasets(self):
        for _ in range(10):
            bagcount = np.random.randint(1, int(1e3))
            gamescount = np.random.randint(1, int(1e3))
            games = np.random.randint(1, int(3e4), size=gamescount)

            result = np.array(processing_data(bagcount, gamescount, games), dtype=int)
            self.assertEqual(len(result), bagcount)

            self.assertTrue(np.all(np.max(result, axis=0) - np.min(result, axis=0) <= 1))
            self.assertTrue(np.all(np.sum(result, axis=0) == games))
            bagssum = np.sum(result, axis=1)
            self.assertTrue(np.max(bagssum) - np.min(bagssum) <= 1)

            
if __name__ == '__main__':
    unittest.main()