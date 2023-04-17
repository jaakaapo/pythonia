import unittest
from onkolukusuurempi import onkolukusuurempi

class TestOnkolukuSuurempi(unittest.TestCase):
  def test_area(self):
   self.assertAlmostEqual(onkolukusuurempi(1,2),"ei ole")
   self.assertAlmostEqual(onkolukusuurempi(2,1),"on")
   self.assertAlmostEqual(onkolukusuurempi(2,2),"yhtä suuret")
   
  def test_values(self):
    self.assertRaises(ValueError, onkolukusuurempi, "c" "b")