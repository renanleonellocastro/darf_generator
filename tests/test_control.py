import unittest
from darf_generator.control import Control
from darf_generator.include.stock import StockTypes


class TestControl(unittest.TestCase):

    def setUp(self):
        self.control = Control()

    def test_add_stock(self):
        self.control.add_stock("OIBR3", 5.0, StockTypes.NORMAL, 2800, 0.0)

        self.assertEqual(1, len(self.control.stocks))

if __name__ == "__main__":
    unittest.main()
