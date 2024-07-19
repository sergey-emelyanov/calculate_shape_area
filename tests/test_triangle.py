import unittest
from calculate_area.calc_area import Triangle


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle(4.0, 3.0, 5.0)

    def test_calculate_area(self):
        self.assertEqual(self.triangle.calculate_area(), 6.0)

    def test_is_rectangular(self):
        self.assertTrue(self.triangle.is_rectangular())


if __name__ == '__main__':
    unittest.main()
