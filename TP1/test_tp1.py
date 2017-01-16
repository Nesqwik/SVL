import unittest
import tp1
from tp1 import Stuff
class TestTp1(unittest.TestCase):

#    def setUp(self):

    def test_sum_empty_first(self):
        s = Stuff()
        self.assertEqual([], s.refs())

    def test_add_ref(self):
        s = Stuff()
        s.add_ref(42)
        arr = s.refs()
        self.assertEqual(42, arr[0])
        self.assertEqual(1, len(arr))

    def test_add_ref_twice(self):
        s = Stuff()
        s.add_ref(42)
        self.assertRaises(ValueError, s.add_ref, 42)


    def test_add_ref_sorted(self):
        s = Stuff()
        s.add_ref(42)
        s.add_ref(1337)
        s.add_ref(1)
        self.assertEqual([1337, 42, 1], s.refs())

    def test_add_item_ref(self):
        s = Stuff()
        s.add_ref(42)
        s.add_ref(1337)
        s.add_item_ref(1337, 1)
        s.add_item_ref(42, 1)
        s.add_item_ref(42, 3)
        self.assertEqual(4, s.item_ref(42));
        self.assertEqual(1, s.item_ref(1337));

    def test_add_item_ref_error_0(self):
        s = Stuff()
        s.add_ref(42)
        self.assertRaises(ValueError, s.add_item_ref, 42, 0)

    def test_add_item_ref_error_m1(self):
        s = Stuff()
        s.add_ref(42)
        self.assertRaises(ValueError, s.add_item_ref, 42, -1)

    def test_add_item_ref_error_no_ref(self):
        s = Stuff()
        self.assertRaises(ValueError, s.add_item_ref, 42, 1)

    def test_add_item_ref_bad_parameter(self):
        s = Stuff()
        s.add_ref(42)
        self.assertRaises(TypeError, s.add_item_ref, 42, "1")

    def test_cons_item_ref(self):
        s = Stuff()
        s.add_ref(42)
        s.add_ref(1337)
        s.add_item_ref(1337, 1)
        s.add_item_ref(42, 3)
        s.cons_item_ref(42, 2)
        self.assertEqual(1, s.item_ref(42))
        self.assertEqual(1, s.item_ref(1337))

    def test_cons_item_ref_cons_plus(self):
        s = Stuff()
        s.add_ref(42)
        s.add_item_ref(42, 3)
        self.assertRaises(ValueError, s.cons_item_ref, 42, 4)

    def test_cons_item_ref_cons_inexistant(self):
        s = Stuff()
        s.add_ref(1337)
        s.add_item_ref(1337, 3)
        self.assertRaises(ValueError, s.cons_item_ref, 42, 1)

    def test_cons_item_ref_bad_parameter(self):
        s = Stuff()
        s.add_ref(42)
        self.assertRaises(TypeError, s.cons_item_ref, 42, "4")

    def test_cons_item_ref_bad_value_0(self):
        s = Stuff()
        s.add_ref(42)
        self.assertRaises(ValueError, s.cons_item_ref, 42, 0)

    def test_cons_item_ref_bad_value_m1(self):
        s = Stuff()
        s.add_ref(42)
        self.assertRaises(ValueError, s.cons_item_ref, 42, -1)

    def test_del_ref(self):
        s = Stuff()
        s.add_ref(42)
        s.add_ref(1337)
        s.del_ref(42)
        self.assertEqual([1337], s.refs())

    def test_del_ref_inexistant(self):
        s = Stuff()
        s.add_ref(42)
        self.assertRaises(ValueError, s.del_ref, 1)

    def test_del_ref_not_empty(self):
        s = Stuff()
        s.add_ref(42)
        s.add_item_ref(42, 1)
        self.assertRaises(ValueError, s.del_ref, 42)
