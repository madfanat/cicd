import unittest
import rectangle  

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        """Тест площади прямоугольника со стороной 0"""
        result = rectangle.area(0, 10)
        self.assertEqual(result, 0)
    
    def test_area_negative(self):
        """Тест площади прямоугольника с отрицательной стороной"""
        result = rectangle.area(-10, 10)
        self.assertEqual(result, -100)
    
    def test_area_broken(self):
        """Тест неправильных входных данных"""
        with self.assertRaises(TypeError):
            rectangle.area("string1", "string2")
        
    def test_area_square(self):
        """Тест площади квадрата 10x10"""
        result = rectangle.area(10, 10)
        self.assertEqual(result, 100)

    def test_perimeter_zero(self):
        """Тест периметра прямоугольника 10x0"""
        result = rectangle.perimeter(10, 0)
        self.assertEqual(result, 20)
    
    def test_perimeter_negative(self):
        """Тест периметра прямоугольника с отрицательными сторонами"""
        result = rectangle.perimeter(-10, -5)
        self.assertEqual(result, -30)

    def test_perimeter(self):
        """Тест периметра прямоугольника 10x5"""
        result = rectangle.perimeter(10, 5)
        self.assertEqual(result, 30)


unittest.main()