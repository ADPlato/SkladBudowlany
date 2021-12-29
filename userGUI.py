from excelToSql import getExcelDBPath, saveToExcel
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pickle

class mainGui(object):
    def __init__(self, master):
        self.master = master
        self.master.title("Porównywanie ofert")
        self.master.geometry("700x400")
        self.menuBar = tk.Menu(self.master)

        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.dbMenu = tk.Menu(self.menuBar, tearoff=0)
        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)

        self.fileMenu.add_command(label="Nowy", command=self.newTable)
        self.fileMenu.add_command(label="Zapisz", command = self.saveTable)
        self.fileMenu.add_command(label="Wczytaj", command = self.loadTable)
        self.fileMenu.add_command(label="Drukuj")
        self.fileMenu.add_command(label="Zamknij", command=self.master.destroy)

        self.dbMenu.add_command(label="Wybierz baze danych", command=self.setDBLocalization)
        self.dbMenu.add_command(label="Wybrana baza danych", command=self.checkDBLocalization)

        self.helpMenu.add_command(label="Pomoc",
                                  command=lambda: messagebox.showinfo("Pomoc", "W razie problemów prosze dzwonić "
                                                                               "pod nr telefonu xxx"))
        self.helpMenu.add_command(label="Informacje", command=self.printInfo)

        self.menuBar.add_cascade(label="Plik", menu=self.fileMenu)
        self.menuBar.add_cascade(label="Baza Producentów", menu=self.dbMenu)
        self.menuBar.add_cascade(label="Info", menu=self.helpMenu)

        self.master.config(menu=self.menuBar)
        self.dbFileSelected = getExcelDBPath()

    def setDBLocalization(self):
        self.dbFileSelected = filedialog.askopenfilename()

    def checkDBLocalization(self):
        messagebox.showinfo("Ścieżka do bazy danych", self.dbFileSelected)

    def getDBLocalization(self):
        return self.dbFileSelected

    def printInfo(self):
        infoFile = open('info.txt', 'r', encoding='utf-8')
        progInfo = []
        for infoline in infoFile:
            progInfo.append(infoline)
        progInfo = ''.join(progInfo)
        messagebox.showinfo("Informacje", progInfo)

    def newTable(self):
        self.newTable=guiTable(self.master)


    def saveTable(self):

        self.excelFilePath=filedialog.askdirectory()
        recordTable=[]
        items=self.newTable.tree.get_children()
        recordTable.append(self.newTable.tableColumns)

        for x in items:
            record=self.newTable.tree.item(x)
            recordTable.append(record['values'])
        saveToExcel('a',self.excelFilePath,recordTable)

    def loadTable(self):
        sub=subWindow(tk.Tk())

class subWindow(mainGui):
    def __init__(self, mast):
        self.mast=mast
        self.mast.title("dodaj")
        self.mast.geometry("700x100")

class guiTable(mainGui):

    def __init__ (self, master):
        self.master = master
        self.style = ttk.Style()
        self.style.theme_use('clam')


        self.tableColumns = ["Producent", "Produkt", "Cena"]
        self.tree = ttk.Treeview(master, column=self.tableColumns, show='headings')

        self.scrollbar = ttk.Scrollbar(self.master)

        self.scrollbar.configure(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.heading("#1", text="Producent")
        self.tree.heading("#2", text="Produkt")
        self.tree.heading("#3", text="Cena")

        for x in range(5):
            self.tree.insert('', 'end', text="1", values=(f'{x}:{x}', f'{x}:{x+x}', f'{x}:{x*x}'))

        self.scrollbar.grid(column=3, row=0, sticky='ns')
        self.tree.grid(column=0, row=0, columnspan=3, sticky='nsew')

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        self.newButton = tk.Button(self.master,text='Dodaj')
        self.deleteButton = tk.Button(self.master, text='Usuń', command = self.removeRow)

        self.newButton.grid(column =0 , row=1, columnspan=4, sticky ='ew')
        self.deleteButton.grid(column =0 , row=2, columnspan=4, sticky ='ew')

    def removeRow(self):
        selected=self.tree.focus()
        if selected != '':
            self.tree.delete(selected)



if __name__ == "__main__":
    guiWindow = tk.Tk()
    frame=mainGui(guiWindow)
    guiWindow.mainloop()
