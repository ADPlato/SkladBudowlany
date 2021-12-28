import xlrd
import xlwt
import os
from datetime import date
import sqlite3

def saveToExcel(excelName,excelPath, data):
    excelWorkBook = xlwt.Workbook()
    excelWorkSheet= excelWorkBook.add_sheet("Sheet1")
    for x in range(len(data)):
        for y in range(len(data[x])):
            excelWorkSheet.write(x,y,data[x][y])
    today=date.today()
    today=today.strftime("%Y_%m_%d_")
    excelWorkBook.save(excelPath+'\\'+today+excelName+'.xls')

def readFromExcel():
    pass

def getExcelDBPath():
    return os.path.abspath("db_xls.xls")

def getExcelData(excelPath):
    productsDB = []
    excelWorkBook = xlrd.open_workbook(excelPath)
    print(excelWorkBook.sheet_names())
    sheetExcel = excelWorkBook.sheet_by_index(0)
    for row in range(sheetExcel.nrows):
        productsDB.append(sheetExcel.row_values(row))
    print(productsDB)
    return productsDB

def createSqlTable(name):
    pass

def connectToSql(name):
    pass

def insertToSql(name,data):
    pass

def selectSqlData(name,conditions):
    pass

def deleteSqlData(name,conditions):
    pass

def updateSqlData(nama, data):
    pass

if __name__=="__main__":
    pass
    #excelFile=getExcelData(r"C:\Users\User\OneDrive\Pulpit\b.xls")
