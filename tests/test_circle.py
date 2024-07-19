import unittest
from calculate_area.calc_area import Circle


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(10)

    def test_calculate_area(self):
        self.assertEqual(self.circle.calculate_area(), 314.16)
