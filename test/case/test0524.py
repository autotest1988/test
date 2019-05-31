import xlrd
import ddt
import unittest
d12 = [{'username': 1.0, 'pwd': 2.0, 'result': 3.0, 'detail': 4.0}, {'username': 'a', 'pwd': 'b', 'result': 'c', 'detail': 'd'}]

class ExcelRead():
    """
    封装的读取excel文件，以多个字典的list格式输出

    """
    def readFile(self, excelPath = "../data/test.xlsx", sheetName = "sheet1"):
        excelFile = xlrd.open_workbook(excelPath)
        table = excelFile.sheet_by_name(sheetName)

        ncol = table.ncols
        nrow = table.nrows
        keys = table.row_values(0)

        print(type(keys))

        result = []

        for i in range(1,nrow):
            s={}
            for j in range(0,ncol):
                s[keys[j]] = table.row_values(i)[j]

            result.append(s)

        print(result)


@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print("setUp------------")

    @ddt.data(*d12)
    def test_01(self, testdata):
        self.assertTrue(testdata)
        print(testdata)

    def tearDown(self):
        print("tearDown----------")



if __name__ == "__main__":
    excel = ExcelRead()
    a = excel.readFile()
    # unittest.main()
