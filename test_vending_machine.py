import unittest
from vending_machine import give_change, give_item_and_change

class TestVendingMachine(unittest.TestCase):
    def test_return_change(self):
        self.assertEqual(give_change(.17), [.10, .05, .02])
        self.assertEqual(give_change(.18), [.10, .05, .02, .01])
        self.assertEqual(give_change(.04), [.02, .02])

    def test_multiple_same_coins(self):
        self.assertEqual(give_change(.04), [.02, .02])

    def test_unavailable_item(self):
        """if user asks for an item that's unavailable, they should not be given the item, and their money should be returned"""
        item, change, _ = give_item_and_change('crisps', .50)
        self.assertIsNone(item)
        self.assertEqual(change, 0.5)

    def test_give_item_and_change_amount_less_than_cost(self):
        """tests is amount is less than the cost"""
        item, change, _ = give_item_and_change('coke', .50)
        self.assertIsNone(item)
        self.assertEqual(change, 0.5)

    def test_give_item_and_change_amount_works_with_correct_money(self):
        """tests is amount is less than the cost"""
        item, change, _ = give_item_and_change('coke', .73)
        self.assertIsNotNone(item)
        self.assertEqual(item, 'coke')
        self.assertEqual(change, [])

    def test_give_item_and_change_amount_works_with_correct_money(self):
        """tests is amount is less than the cost"""
        item, change, _ = give_item_and_change('coke', 2.0)
        self.assertIsNotNone(item)
        self.assertEqual(item, 'coke')
        self.assertEqual(change, [1,.20, .05, .02])

#   AssertionError: [] != 0.73




