import unittest
import ddt
from test0617 import ExcelUntil

d = ExcelUntil('test.xls', 'Sheet1').readData()

@ddt.ddt
class Test(unittest.TestCase):

    def setUp(self):
        print("setUp")

    @ddt.data(*d)
    def test_01(self, test_data):

        print(test_data)

    def tearDown(self):
        print("tearDown")

if __name__ == '__main__':
    unittest.main()
