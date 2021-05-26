import unittest
import leapYear

class TestCase(unittest.TestCase):
    def testOne(self):
        self.assertEqual(leapYear.isLeapYear(400),True)

if __name__ == '__main__':
    unittest.main()
