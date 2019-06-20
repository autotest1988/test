import xlrd

class ExcelUntil():

    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        self.keys = self.table.row_values(0)
        self.nrows = self.table.nrows
        self.ncols = self.table.ncols

    def readData(self):
        r = []

        for i in range(1, self.nrows):
            tmp = {}
            for j in range(self.ncols):

                tmp[self.keys[j]] = self.table.row_values(i)[j]

            r.append(tmp)
        return r


if __name__ == '__main__':
    excelPath = 'test.xls'
    sheetName = 'Sheet1'
    excel = ExcelUntil(excelPath, sheetName)
    result = excel.readData()
    print(result)
