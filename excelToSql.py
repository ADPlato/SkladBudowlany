import xlrd
import os
import sqlite3


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
    excelFile=getExcelData(r"C:\Users\User\OneDrive\Pulpit\b.xls")

