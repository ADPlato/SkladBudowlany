import excelToSql
from excelToSql import getExcelDBPath
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class mainGui(object):
    def __init__(self, master):
        self.master = master
        self.master.title("Porównywanie ofert")
        self.master.geometry("700x700")
        self.menuBar = tk.Menu(self.master)

        self.fileMenu = tk.Menu(self.menuBar, tearoff=0)
        self.dbMenu = tk.Menu(self.menuBar, tearoff=0)
        self.helpMenu = tk.Menu(self.menuBar, tearoff=0)

        self.fileMenu.add_command(label="Nowy", command=self.newtable)
        self.fileMenu.add_command(label="Zapisz")
        self.fileMenu.add_command(label="Wczytaj")
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

        #self.newTable = guiTable(guiWindow)

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

    def newtable(self):
        gui = guiTable(guiWindow)

class guiTable(mainGui):
    def __init__(self, master):
        super().__init__(master)
        print(self.dbFileSelected)
        self.master = master
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.tree = ttk.Treeview(master, column=("Producent", "Produkt", "Cena"), show='headings')
        self.tree.bind("<Button-3>", self.right_click)

        self.scrollbar = ttk.Scrollbar(self.master)

        self.scrollbar.configure(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.heading("#1", text="Producent")
        self.tree.heading("#2", text="Produkt")
        self.tree.heading("#3", text="Cena")

        for x in range(50):
            self.tree.insert('', 'end', text="1", values=[f'a {x}', f'b{x * x}', f'c{x + x}'])

        self.scrollbar.grid(column=1, row=0, sticky='ns')
        self.tree.grid(column=0, row=0, sticky='nsew')

        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

    def right_click(self, x):
        selectedItem = self.tree.focus()
        print(self.tree.item(selectedItem))
        self.tree.delete(selectedItem)


if __name__ == "__main__":
    guiWindow = tk.Tk()
    #gui = mainGui(guiWindow)
    gui = guiTable(guiWindow)
    guiWindow.mainloop()
