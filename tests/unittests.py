import unittest
import rectangle  

class RectangleTestCase(unittest.TestCase):
    
    def test_zero_mul(self):
        """Проверка площади с нулевым значением."""
        res = rectangle.area(10, 10)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        """Проверка площади квадрата (10x10)."""
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)
    
    def test_perimeter_calculation(self):
        """Проверка правильности вычисления периметра."""
        res = rectangle.perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_perimeter_zero(self):
        """Проверка периметра, если одна сторона равна 0."""
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)

if __name__ == '__main__':
    unittest.main()