import collections
import xlsxwriter

wordcount = collections.Counter()
with open("C:\\Users\\Xiaomi\\Documents\\count\\text.txt","r+") as file:
    for line in file:
        wordcount.update(line.split())

#creating a workbook and saving it in a specific directory that we want
workbook = xlsxwriter.Workbook('C:\\Users\\Xiaomi\\Documents\\count\\result.xlsx')
#creating a worksheet in the workbook
worksheet = workbook.add_worksheet()

#initialising the rows and coloumns to zero since they start with zero in spreadsheet
row = 0
col = 0

#iterating through words and writing them in a spreadsheet
for words,count in wordcount.iteritems():
    worksheet.write(row,col, words)
    worksheet.write(row,col+1, count)
    row = row+1

workbook.close()