import xlrd;
# xl = xlrd.open_workbook('./userinfo.xls')
# table = xl.sheets()[0]
# row = table.row_values(0)
# print(row)
# col = table.col_values(0)
# print(col)
# print(table.nrows)
# print(table.ncols)
# print("---------------------")
# print(table.cell(1, 0).ctype)

class XlUserinfo():
    def __init__(self,url):
        self.xl = xlrd.open_workbook(url)

    def get_sheet_info(self):
        rnameList = ['username','pwd']
        userinfo = [];
        for line in range(1, self.sheet.nrows):
            #[{'username': 'test@163.com', 'pwd': 123456.0}, {'username': 'test', 'pwd': 'adafdaf'}, {'username': '', 'pwd': 'adafa'}, {'username': 'test', 'pwd': ''}]
            [(self.sheet.cell(line, j).value()=str(int(self.sheet.cell(line,j).value()))) for j in range(1, self.sheet.ncols) if (self.sheet.cell(line,j).ctype == 2)]:


            info = self.sheet.row_values(line)
            print(info)
            tmp = zip(rnameList, info)
            userinfo.append(dict(tmp))
        return userinfo

    def get_sheetinfo_by_name(self, name):
        self.sheet = self.xl.sheet_by_name(name)
        return self.get_sheet_info()

    def get_sheetinfo_by_index(self, index):
        self.sheet = self.xl.sheet_by_index(index)
        return self.get_sheet_info()


if __name__ == '__main__':
    xluserinfo = XlUserinfo('./userinfo.xls')
    info = xluserinfo.get_sheetinfo_by_name('Sheet1')
    print(info)
    info = xluserinfo.get_sheetinfo_by_index(0)
    print(info)