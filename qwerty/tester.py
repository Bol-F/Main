import unittest
# from qwerty.func import sum_
#
#
# class TestAddFunction(unittest.TestCase):
#     def test_add_positive(self):
#         self.assertEqual(sum_(1, 2), 3)
#
#     def test_add_negative(self):
#         self.assertEqual(sum_(-1, -2), -3)

class TestMethods(unittest.TestCase):
    def test_object_create(self):
        obj = Auto("GM", "Nexia", "White", "Green")
        self.assertIsInstance(obj, Auto)
        self.assertEqual(obj.name, "GM")
        self.assertEqual(obj.model, "Nexia")
        self.assertEqual(obj.rang, "White")

    def test_set_damaged(self):
        car1 = Auto("GM", "Nexia", "White", "Green")
        self.assertFalse(car1.damaged)
        car1.set_damaged()
        self.assertTrue(car1.damaged)



class Auto:
    autos = []
    def __init__(self, name, model, rang, company):
        self.name = name
        self.model = model
        self.rang = rang
        self.company = company
        self.damaged = False
        Auto.autos.append(self)

    def set_damaged(self):
        self.damaged = True
        return self.damaged

    def get_info(self):
        return self.name, self.model, self.rang, self.company

    @classmethod
    def get_autos(cls):
        autos_ = []
        for i in cls.autos:
            autos_.append(i.get_info())
        return autos_

auto1 = Auto("GM", "Nexia", "White", "Green")
auto2 = Auto("GM", "Nexia2", "Black", "Good")

print(auto1.get_info())
print(auto2.get_info())
