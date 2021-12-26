import xlrd
import os


def getExcelDBPath():
    return os.path.abspath("db_xls.xls")


def getDBExcel():
    productsDB = []
    databaseExcel = xlrd.open_workbook(getExcelDBPath())
    sheetExcel = databaseExcel.sheet_by_index(0)
    for row in range(sheetExcel.nrows):
        productsDB.append(sheetExcel.row_values(row))
    print(productsDB)
    return productsDB

