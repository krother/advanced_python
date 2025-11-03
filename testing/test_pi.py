
from unittest import TestCase

def pi():
    return 3.14159


class PiTests(TestCase):

    def test_pi_digist(self):
        self.assertAlmostEqual(pi(), 3.14, 2)
        self.assertEqual([1,2,3], [1,2,4,3])
        
