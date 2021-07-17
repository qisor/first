# import xlrd
#
# file1 = r"C:\Users\dsg\Desktop\xueasn.xlsx"
# file2 = r"C:\Users\dsg\Desktop\abcd.xls"
#
# wb = xlrd.open_workbook(file2, formatting_info=True)
# table = wb.sheets()[0]  # 通过索引顺序获取
# # table = wb.sheet_by_index(0)) #通过索引顺序获取
# # table = wb.sheet_by_name(sheet_name)#通过名称获取 以上三个函数都会返回一个xlrd.sheet.Sheet()对象
# names = wb.sheet_names()  # 返回book中所有工作表的名字
# wb.sheet_loaded(0)  # 检查某个sheet是否导入完毕
# print(names)
#
# nrows = table.nrows  #获取该sheet中的有效行数
# # table.row(rowx)  #返回由该行中所有的单元格对象组成的列表
# # table.row_slice(rowx)  #返回由该列中所有的单元格对象组成的列表
# # table.row_types(rowx, start_colx=0, end_colx=None)    #返回由该行中所有单元格的数据类型组成的列表
# # table.row_values(rowx, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表
# # table.row_len(rowx) #返回该列的有效单元格长度
#
#
# # 5、列
# # ncols = table.ncols  # 获取列表的有效列数
# ncol = table.ncols
# # table.col(colx, start_rowx=0, end_rowx=None)  # 返回由该列中所有的单元格对象组成的列表
# nncol = table.col(2)
# # table.col_slice(colx, start_rowx=0, end_rowx=None)  # 返回由该列中所有的单元格对象组成的列表
# ncno = table.col_slice(2)
# # table.col_types(colx, start_rowx=0, end_rowx=None)  # 返回由该列中所有单元格的数据类型组成的列表
# n1 = table.col_types(2)
# # table.col_values(colx, start_rowx=0, end_rowx=None)  # 返回由该列中所有单元格的数据组成的列表
# n2 = table.col_values(2)
#
# # 6、单元格cell
# # table.cell(rowx, colx)  # 返回单元格对象
# cell = table.cell(1, 2)
# # table.cell_type(rowx, colx)  # 返回单元格中的数据类型
# cell1 = table.cell_type(2, 1)
# # table.cell_value(rowx, colx)  #
# cell2 = table.cell_value(1, 2)
# # table.cell_xf_index(rowx, colx)  # 暂时还没有搞懂
# cell3 = table.cell_xf_index(1, 2)
#
# # print(cell)
# # print(cell1)
# # print(cell2)
# # print(cell3)
#
# for i in range(nrows):
#     for j in range(ncol):
#         print(table.cell_value(i,j),end=" ")
#     print()

import requests

url = "https://www.runoob.com/wp-content/uploads/2015/06/golist.jpg"
r = requests.get(url)
with open("go.png", mode="wb") as fp:
    fp.write(r.content)
