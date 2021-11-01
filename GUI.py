import tkinter as tk
from excelToSql import *


windowExcel = tk.Tk()

labelBrowseExcel = tk.Label(windowExcel, text='Wyszukaj plik Excel z bazą danych')
buttonBrowseExcel = tk.Button(windowExcel, text='Szukaj', command=lambda: getDBExcel())
buttonUpdateSql = tk.Button(windowExcel, text="Aktualizuj", command=lambda:updateSqlDB())
labelBrowseExcel.pack()
buttonBrowseExcel.pack()
buttonUpdateSql.pack()

windowExcel.mainloop()
