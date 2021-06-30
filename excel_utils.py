import xlsxwriter



def write_xlsx():
  workbook = xlsxwriter.Workbook('arrays.xlsx')
  worksheet = workbook.add_worksheet()
  return
