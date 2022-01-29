import tkinter
import xlsxwriter as xls
import pyautogui as au
from tkinter import Button, Label, Listbox, Scrollbar


class Panel:
    evaluar = False
    prizes = []

    def __init__(self, ventana):
        self.playing = True
        self.ventana = ventana
        ventana.geometry("400x225")
        ventana.title("Slot tracker")
        ventana.resizable(False, False)
        ventana.config(bg="lightgreen")
        # _____________ KEYS
        ventana.bind('<space>', self.key_press)


        # _____________ LABELS
        self.title = Label(ventana, text="LDOE Slot Machine", bg="lightgreen",
                           font=("Times New Roman", 20))
        self.title.place(x=100, y=10)

        # _____________ BOTONES
        self.bt_evaluar = Button(ventana, text="Scan", bg="lightblue", font=("Times New Roman", 20),
                                 activebackground="red", command=self.startAnalizeThrow
                                 )
        self.bt_evaluar.place(x=60, y=150)

        self.bt_resultados = Button(ventana, text="Listo", bg="lightblue", font=("Times New Roman", 20),
                                    activebackground="red", command=self.getRecords
                                    )
        self.bt_resultados.place(x=255, y=150)

        # _____________ LABELS
        self.lastThrowString = tkinter.StringVar()
        self.lastThrowString.set("Waiting...")
        self.lastThrow = Label(ventana, font=("Times New Roman", 20),
                               textvariable=self.lastThrowString)
        self.lastThrow.place(x=10, y=80)

    def key_press(self, e):

        self.startAnalizeThrow()
        return

    def startAnalizeThrow(self):
        self.check()
        last = self.prizes[len(self.prizes) - 1]
        string = f"{last[0]}, {last[1]} y {last[2]}"
        self.lastThrowString.set(string)
        return

    def getRecords(self):
        workbook = xls.Workbook('PrizesLDOE01.xlsx')
        worksheet = workbook.add_worksheet(name="Resultados1")
        cell_format = workbook.add_format()
        cell_format.set_bold()
        cell_format.set_bg_color('red')

        row = 0
        col = 0
        for item1, item2, item3, win in self.prizes:
            if win:
                worksheet.write(row, col, item1, cell_format)
                worksheet.write(row, col + 1, item2, cell_format)
                worksheet.write(row, col + 2, item3, cell_format)
            else:
                worksheet.write(row, col, item1)
                worksheet.write(row, col + 1, item2)
                worksheet.write(row, col + 2, item3)
            row += 1

        workbook.close()
        return

    def winnerThrow(self, throw):
        if throw[0] == throw[1] or throw[0] == throw[2] or throw[1] == throw[2]:
            return True
        return False

    def verificar1(self):
        if au.locateOnScreen("../images/latas/latas1.png", region=(595, 400, 690, 500), confidence=0.75):
            return "latas"
        elif au.locateOnScreen("../images/c4/c42.png", region=(595, 400, 690, 500), confidence=0.75):
            return "C-4"
        elif au.locateOnScreen("../images/chanchos/chancho3.png", region=(595, 400, 690, 500), confidence=0.75):
            return "chanchos"
        elif au.locateOnScreen("../images/cintas/cintas4.png", region=(595, 400, 690, 500), confidence=0.75):
            return "cintas"
        elif au.locateOnScreen("../images/energias/energia4.png", region=(595, 400, 690, 500), confidence=0.75):
            return "Energias"
        elif au.locateOnScreen("../images/jack/jack4.png", region=(595, 400, 690, 500), confidence=0.75):
            return "Jackpot"
        elif au.locateOnScreen("../images/pavos/pavos2.png", region=(595, 400, 690, 500), confidence=0.75):
            return "Pavos"
        return False

    def verificar2(self):
        if au.locateOnScreen("../images/latas/latas1.png", region=(700, 360, 795, 455), confidence=0.75):
            return "latas"
        elif au.locateOnScreen("../images/c4/c42.png", region=(700, 360, 795, 455), confidence=0.75):
            return "C-4"
        elif au.locateOnScreen("../images/chanchos/chancho3.png", region=(700, 360, 795, 455), confidence=0.75):
            return "chanchos"

        elif au.locateOnScreen("../images/jack/jack4.png", region=(700, 360, 795, 455), confidence=0.75):
            return "Jackpot"
        elif au.locateOnScreen("../images/pavos/pavos2.png", region=(700, 360, 795, 455), confidence=0.75):
            return "Pavos"
        elif au.locateOnScreen("../images/energias/energia4.png", region=(700, 360, 795, 455), confidence=0.85):
            return "Energias"
        elif au.locateOnScreen("../images/cintas/cintas4.png", region=(700, 360, 795, 455), confidence=0.85):
            return "cintas"
        return False

    def verificar3(self):
        if au.locateOnScreen("../images/latas/latas1.png", region=(800, 345, 895, 435), confidence=0.75):
            return "latas"
        elif au.locateOnScreen("../images/c4/c42.png", region=(800, 345, 895, 435), confidence=0.75):
            return "C-4"
        elif au.locateOnScreen("../images/chanchos/chancho3.png", region=(800, 345, 895, 435), confidence=0.75):
            return "chanchos"
        elif au.locateOnScreen("../images/cintas/cintas4.png", region=(800, 345, 895, 435), confidence=0.75):
            return "cintas"
        elif au.locateOnScreen("../images/energias/energia4.png", region=(800, 345, 895, 435), confidence=0.75):
            return "Energias"
        elif au.locateOnScreen("../images/jack/jack4.png", region=(800, 345, 895, 435), confidence=0.75):
            return "Jackpot"
        elif au.locateOnScreen("../images/pavos/pavos2.png", region=(800, 345, 895, 435), confidence=0.75):
            return "Pavos"
        return False

    def check(self):
        throw = [self.verificar1(), self.verificar2(), self.verificar3()]
        if self.winnerThrow(throw):
            throw.append(True)
        else:
            throw.append(False)
        self.prizes.append(throw)
        return
