import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from crypto_lib.crypto_algorithms import CryptoAlgorithms

class TestCryptoAlgorithms(unittest.TestCase):
  pass

if __name__ == '__main__':
    unittest.main()
