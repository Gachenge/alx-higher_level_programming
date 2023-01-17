#!/usr/bin/python3
"""unittest base"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """test cases parent class instantiation"""

    def test_NoArg(self):
        a = Base()
        b = Base()
        self.assertEqual(a.id, b.id - 1)

    def test_None(self):
        a = Base(None)
        b = Base(None)
        self.assertEqual(a.id, b.id - 1)

    def test_three(self):
        a = Base()
        b = Base()
        c = Base()
        self.assertEqual(a.id, c.id - 2)

    def test_NaN(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_inf(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)


class TestJson(unittest.TestCase):
    """test for json string dictionary"""

    def test_noType(self):
        a = Rectangle(4, 5)
        self.assertEqual(str, type(Base.to_json_string([a.to_dictionary()])))

    def test_none(self):
        self.assertEqual('[]', Base.to_json_string(None))

    def test_empt(self):
        self.assertEqual('[]', Base.to_json_string([]))

    def test_gd(self):
        a = Square(6, 2, 1)
        self.assertEqual('[{"id": 8, "size": 6, "x": 2, "y": 1}]',
                         Base.to_json_string([a.to_dictionary()]))

    def test_em(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual('[]', f.read())

    def test_nn(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual('[]', f.read())

    def test_gdi(self):
        a = Rectangle(3, 5, 6, 8, 7)
        Rectangle.save_to_file([a])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(52, len(f.read()))

    def test_man(self):
        a = Square(4, 6, 8)
        b = Square(5, 7, 9)
        c = Square(6, 5, 7)
        d = Square(4, 3, 6)
        Square.save_to_file([a, b, c, d])
        with open("Square.json", 'r') as f:
            self.assertEqual(155, len(f.read()))

    def test_over(self):
        a = Square(6, 9, 9)
        Square.save_to_file([a])
        a = Square(1, 1, 1)
        Square.save_to_file([a])
        with open("Square.json", 'r') as f:
            self.assertEqual(39, len(f.read()))


class TestOthr(unittest.TestCase):
    """adding other tests"""
    def test_float(self):
        self.assertEqual(3.45, Base(3.45).id)

    def test_str(self):
        self.assertEqual('cow', Base('cow').id)

    def test_dict(self):
        self.assertEqual({'a': 4, 'b': 7}, Base({'a': 4, 'b': 7}).id)

    def test_many(self):
        with self.assertRaises(TypeError):
            Base(4, 6, 3, 6)

    def test_att(self):
        with self.assertRaises(AttributeError):
            print(Base(3).__nb_instances)

    def test_fromjsonNone(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_fromjsonEmpt(self):
        self.assertEqual([], Base.from_json_string('[]'))

    def test_dictjson(self):
        with self.assertRaises(TypeError):
            print(Base.from_json_string([{'id': 89}]))

    def test_crt(self):
        with self.assertRaises(TypeError):
            a = Rectangle(89)
            b = to_dictionary()
            Rectangle.create(**b)

    def test_crt1(self):
        a = Rectangle(89, 4)
        b = a.to_dictionary()
        c = Rectangle.create(**b)
        self.assertEqual(16, c.id)

    def test_crt2(self):
        a = Rectangle(4, 5, 6)
        b = a.to_dictionary()
        c = Rectangle.create(**b)
        self.assertEqual(20, c.area())

    def test_crt3(self):
        a = Rectangle(4, 5, 6, 7, 8)
        b = a.to_dictionary()
        c = Rectangle.create(**b)
        self.assertEqual(7, c.y)

    def test_ldfl(self):
        a = Rectangle(1, 2, 3, 4, 5)
        b = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([a, b])
        lts = Rectangle.load_from_file()
        self.assertEqual(str(a), str(lts[0]))

    def test_empfl(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file([], 1)


if __name__ == '__main__':
    unittest.main()
