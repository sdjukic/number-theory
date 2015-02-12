#!/usr/bin/env python3

import unittest
import prime_lib 

class TestPrimeLib(unittest.TestCase):
  
  def setUp(self):
      self.is_prime = prime_lib.is_prime
      self.gcd = prime_lib.gcd

  def test_exceptions(self): 
      pass

  def test_primes(self):
      self.assertEqual(self.is_prime(11), True)
      self.assertEqual(self.is_prime(13), True)
      self.assertEqual(self.is_prime(31), True)
      self.assertEqual(self.is_prime(52), False)
      self.assertEqual(self.is_prime(15), False)

  
  def test_gcd(self):
      self.assertEqual(self.gcd(5, 50), 5)
      self.assertEqual(self.gcd(100, 51), 1)
      self.assertEqual(self.gcd(198, 252), 18)
      self.assertEqual(self.gcd(72, 36), 36)
      self.assertEqual(self.gcd(248, 64), 8)
      self.assertEqual(self.gcd(1001, 515), 1)



if __name__ == '__main__':
  unittest.main()
#suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
#unittest.TextTestRunner(verbosity=2).run(suite)
