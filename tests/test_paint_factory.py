from project.factory.paint_factory import PaintFactory
from project.factory.factory import Factory
import unittest
from unittest import mock


class TestsPaintFactory(unittest.TestCase):
    @mock.patch.multiple(PaintFactory, __abstractmethods__=set())
    def test_create_factory(self):
        pf = PaintFactory('f1', 5)
        self.assertEqual(pf.name, "f1")
        self.assertEqual(pf.capacity, 5)
        self.assertEqual(pf.ingredients, {})

    def test_beginner_inherits_player(self):
        self.assertTrue("Factory" == PaintFactory.__bases__[0].__name__)

    def test_add_ingredient_legit(self):
        pf = PaintFactory('f1', 5)
        pf.add_ingredient('blue', 3)
        self.assertEqual(pf.ingredients['blue'], 3)
        self.assertEqual(pf.capacity, 2)
        self.assertEqual(pf.products, pf.ingredients)
        pf.remove_ingredient('blue', 3)
        self.assertEqual(pf.ingredients['blue'], 0)
        self.assertEqual(pf.capacity, 5)
        self.assertEqual(pf.products, pf.ingredients)

    def test_add_ingredient_several(self):
        pf = PaintFactory('f1', 5)
        pf.add_ingredient('blue', 1)
        pf.add_ingredient('yellow', 1)
        pf.add_ingredient('green', 1)
        pf.add_ingredient('red', 1)
        pf.add_ingredient('white', 1)
        all_keys = ['blue', 'yellow', 'green', 'red', 'white']
        for x in all_keys:
            self.assertEqual(x in pf.ingredients.keys(), True)
            self.assertEqual(pf.ingredients[x], 1)
            self.assertEqual(pf.products[x], 1)
        pf.remove_ingredient('green', 1)
        self.assertEqual(pf.ingredients['green'], 0)
        self.assertEqual(pf.ingredients['blue'], 1)
        pf.add_ingredient('blue', 1)
        self.assertEqual(pf.ingredients['blue'], 2)
        self.assertEqual(pf.ingredients['green'], 0)

    def test_add_ingredient_wrong_name(self):
        pf = PaintFactory('f1', 5)
        with self.assertRaises(TypeError) as cm:
            pf.add_ingredient('asd', 2)
        self.assertEqual(str(cm.exception), "Ingredient of type asd not allowed in PaintFactory")

    def test_add_ingredient_no_capacity(self):
        pf = PaintFactory('f1', 0)
        with self.assertRaises(ValueError) as cm:
            pf.add_ingredient('blue', 2)
        self.assertEqual(str(cm.exception), "Not enough space in factory")

    def test_remove_ingredient_negative_value(self):
        pf = PaintFactory('f1', 2)
        pf.add_ingredient('blue', 1)
        with self.assertRaises(ValueError) as cm:
            pf.remove_ingredient('blue', 2)
        self.assertEqual(str(cm.exception), "Ingredient quantity cannot be less than zero")

    def test_remove_ingredient_no_key(self):
        pf = PaintFactory('f1', 2)
        pf.add_ingredient('blue', 1)
        with self.assertRaises(KeyError) as cm:
            pf.remove_ingredient('asd', 1)
        self.assertEqual(str(cm.exception), "'No such ingredient in the factory'")


if __name__ == "__main__":
    unittest.main()