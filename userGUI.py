from excelToSql import getExcelDBPath, saveToExcel, readFromExcel
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class mainGui(object):
    def __init__(self, master):
        self.master = master
        self.master.title("Porównywanie ofert")
        self.master.iconbitmap('SKSM_logo.ico')
        self.menuBar = tk.Menu(self.master)


        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.dbMenu = tk.Menu(self.menuBar, tearoff=0)
        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)

        self.fileMenu.add_command(label="Nowy", command=self.createNewTable)
        self.fileMenu.add_command(label="Zapisz", command=self.saveTable)
        self.fileMenu.add_command(label="Wczytaj", command=self.loadTable)
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

    def getDBHeadings(self):
        self.tableColumns = ["Producent", "Produkt", "Wycena"]

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

    def createNewTable(self):
        self.newTable = guiTable(self.master)

    def saveTable(self):

        excelFilePath = filedialog.askdirectory()
        recordTable = []
        items = self.tree.get_children()
        recordTable.append(self.tableColumns)

        for x in items:
            record = self.tree.item(x)
            recordTable.append(record['values'])
        saveToExcel('a', excelFilePath, recordTable)

    def loadTable(self):
        self.newTable = guiTable(self.master)
        excelFilePath = filedialog.askopenfilename()
        excelLoadedData=readFromExcel(excelFilePath)
        self.excelLoadedHeadings=excelLoadedData[0]
        excelLoadedData=excelLoadedData[1:]
        for rows in excelLoadedData:
            self.newTable.tree.insert('', 'end', text="1", values=(rows))


class guiTable(mainGui):

    def __init__(self, master):
        #mainGui.__init__(self, master)
        mainGui.getDBHeadings(self)
        self.master = master
        self.style = ttk.Style()
        self.style.theme_use('clam')


        self.tree = ttk.Treeview(master, column=self.tableColumns, show='headings')
        self.scrollbar = ttk.Scrollbar(self.master)
        self.scrollbar.configure(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        for nr, head in enumerate(self.tableColumns):
            self.tree.heading(f'#{nr+1}', text=head)

        self.scrollbar.grid(column=3, row=0, sticky='ns')
        self.tree.grid(column=0, row=0, columnspan=3, sticky='nsew')

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        self.newButton = tk.Button(self.master, text='Dodaj', command=self.addrecord)
        self.deleteButton = tk.Button(self.master, text='Usuń', command=self.removeRow)

        self.newButton.grid(column=0, row=1, columnspan=4, sticky='ew')
        self.deleteButton.grid(column=0, row=2, columnspan=4, sticky='ew')

    def removeRow(self):
        selected = self.tree.focus()
        if selected != '':
            self.tree.delete(selected)

    def addrecord(self):
        addWindow(self.master,self.tree)

    def addrow(self, values):
        self.tree.insert('', 'end', text="1", values=(values))



class addWindow(guiTable):
    def __init__(self, master, tree):
        self.tree=tree
        super().getDBHeadings()
        self.master = master
        self.addWindow = tk.Toplevel(master)
        self.addWindow.title("Dodaj record")

        self.labels = []
        self.entryLabels = []
        for columns in self.tableColumns:
            self.entryLabels.append(tk.Entry(self.addWindow))
            self.labels.append(tk.Label(self.addWindow, text=columns))
        for griding in range(len(self.tableColumns)):
            self.labels[griding].grid(column=griding, row=0)
            self.entryLabels[griding].grid(column=griding, row=1, sticky='nswe')

        entryButton=tk.Button(self.addWindow, text="Dodaj", command=self.addValues)
        entryButton.grid(column=0, row=2, columnspan=len(self.tableColumns), sticky='we')

    def addValues(self):
        record=[]
        for label in self.entryLabels:
            record.append(label.get())
        guiTable.addrow(self,record)



if __name__ == "__main__":
    guiWindow = tk.Tk()
    frame = mainGui(guiWindow)
    guiWindow.mainloop()
