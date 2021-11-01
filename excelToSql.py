from tkinter import filedialog
import xlrd
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    auth_plugin='mysql_native_password'
)

def getExcelDBPath():
    excelDatabaseFile = filedialog.askopenfile(mode='r', filetypes=[('Excel Files', '*.xls')])
    if excelDatabaseFile:
        return excelDatabaseFile.name


def getDBExcel():
    productsDB=[]
    databaseExcel = xlrd.open_workbook(getExcelDBPath())
    sheetExcel = databaseExcel.sheet_by_index(0)
    for row in range(sheetExcel.nrows):
        productsDB.append(sheetExcel.row_values(row))
    return productsDB


def updateSqlDB():

