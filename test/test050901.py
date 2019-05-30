import xlsxwriter
import time

xl = xlsxwriter.Workbook('./test.xls');

table = xl.add_worksheet('sheet1');

table.write_string(0,0,'username');
table.write_string(0,1,'pwd');
table.write_string(0,2,'result');
table.write_string(0,3,'detail');

xl.close()


class xlsLoginfo():
    def __init__(self, url=''):
        filename = url + time.strftime('%Y-%m-%d', time.gmtime()) + '.xls'
        self.xlsrow = 0;
        self.xl = xlsxwriter.workbook(filename)

    def xls_write(self, *args):
        self.xlscols = 0;
        for i in args:
            self.sheet.write_string(self.xlsrow,self.xlscols,i);
            self.xlscols += 1
        self.xlsrow = self.xlsrow + 1

    def XL_init(self, sheetname, *title):
        self.sheet = xl.add_worksheet(sheetname)
        self.sheet.set_column('A:E', 30);
        self.xls_write(title)

    def xl_clost(self):
        self.xl.close()


