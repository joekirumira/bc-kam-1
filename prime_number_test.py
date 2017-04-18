import unittest
from prime_number_generator import generate_prime_numbers

class TestPrimeNumberGenerator(unittest.TestCase):

    def test_int(self):
        self.assertIsNot(generate_prime_numbers("stuff"),"range is not integer")

    def test_not_negative(self):
        self.assertIsNot(generate_prime_numbers(-1),"range is a negative number")

    def test_prime_numbers(self):
        self.assertEqual(generate_prime_numbers(10),[2,3,5,7])

if __name__ == '__main__':
    unittest.main()