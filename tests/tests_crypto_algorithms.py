import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from crypto_lib.crypto_algorithms import CryptoAlgorithms

class TestCryptoAlgorithms(unittest.TestCase):
  def test_exp_by_mod_from_right_to_left(self):
    test_cases = [
      (5, 101, 13, 5, None),
      (8, 150, 13, 12, None),
      (5, -1, 13, -1, None),
      (5, 150, -1, -2, None),
      (5, 150, 0, -2, None),
    ]

    for base, exp, mod, expected, message in test_cases:
      with self.subTest(base=base, exp=exp, mod=mod):
        if message:
          self.assertEqual(
            CryptoAlgorithms.exp_by_mod_from_right_to_left(base, exp, mod),
            expected,
            message
          )
        else:
          self.assertEqual(
            CryptoAlgorithms.exp_by_mod_from_right_to_left(base, exp, mod),
            expected
          )

  def test_general_euclid_alg(self):
    test_cases = [
      (180, 150, (30, 1, -1), None),
      (170, 150, (10, -7, 8), None),
      (150, 180, -1, None),
    ]

    for a, b, expected, message in test_cases:
      with self.subTest(a=a, b=b):
        if message:
          self.assertEqual(
            CryptoAlgorithms.general_euclid_alg(a, b),
            expected,
            message
          )
        else:
          self.assertEqual(
            CryptoAlgorithms.general_euclid_alg(a, b),
            expected
          )

if __name__ == '__main__':
      unittest.main()
