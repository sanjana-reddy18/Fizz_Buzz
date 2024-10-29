import unittest
from fizzbuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_returns_number(self):
        # Test that a regular number returns itself
        self.assertEqual(fizz_buzz(1), "1")
        self.assertEqual(fizz_buzz(2), "2")

    def test_returns_fizz_for_multiples_of_3(self):
        # Test multiples of 3
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(6), "Fizz")

    def test_returns_buzz_for_multiples_of_5(self):
        # Test multiples of 5
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(10), "Buzz")

    def test_returns_fizzbuzz_for_multiples_of_3_and_5(self):
        # Test multiples of both 3 and 5
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(30), "FizzBuzz")

if __name__ == "__main__":
    unittest.main()
