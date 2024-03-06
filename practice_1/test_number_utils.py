from practice_1.number_utils import is_prime_list

import unittest
class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
        
    def test_give_41_53_73_97_is_prime(self):
        prime_list = [41,53,73,97]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)