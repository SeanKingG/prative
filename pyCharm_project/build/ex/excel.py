import xlwt

book = xlwt.Workbook()
sheet1 = book.add_sheet('hello')
sheet1.write(0, 0, 'cloudox')
sheet1.write(1, 0, 'ox')
book.save('dsds.xls')