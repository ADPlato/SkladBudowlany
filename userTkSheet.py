import tkinter as tk
import tksheet


def createRow():
    sheet.insert_row(values = None, idx = "end", height = None, deselect_all = False, add_columns = False, redraw = True)


def tksheetInit():

    columnNumber=5
    sheetHeaders=['Nazwa','cos','dupa']
    sheet.headers(sheetHeaders)

    sheet.set_sheet_data([["" for x in range(columnNumber)]])
    sheet.enable_bindings(("single_select",
                           "arrowkeys",
                           "row_select",
                           "rc_delete_row",
                           "right_click_popup_menu",
                           "rc_select",
                           "edit_cell"))


def tksheetPopUpMenuInit():
    sheet.popup_menu_add_command("Nowy wiersz", func=createRow, table_menu = True, index_menu = True, header_menu = True)

top = tk.Tk()
sheet = tksheet.Sheet(top, width=650,height=500, )
sheet.grid()

tksheetPopUpMenuInit()
tksheetInit()


top.mainloop()
