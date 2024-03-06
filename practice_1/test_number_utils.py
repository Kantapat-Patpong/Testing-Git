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
        
    def test_give_143_277_337_533_is_prime(self):
        prime_list = [143,277,337,533]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
        
    def test_give_52_12_4_33_is_prime(self):
        prime_list = [52,12,4,33]
        isnot_prime = is_prime_list(prime_list)
        self.assertFalse(isnot_prime)
        
    def test_give_613_437_469_799_is_prime(self):
        prime_list = [613_437_469_799]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
        
    def test_give_negative_767_629_441_13_is_prime(self):
        prime_list = [-767,-629,-441,-13]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)