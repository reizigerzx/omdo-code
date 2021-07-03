import xlsxwriter

def write_xlsx(row,array:[], filename:str):
  workbook = xlsxwriter.Workbook(filename)
  worksheet = workbook.add_worksheet()
  for col, data in enumerate(array):
    worksheet.write_column(row, col, data)
  return
