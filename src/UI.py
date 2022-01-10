

class Panel:
    evaluar = False

    def __init__(self, ventana):
        self.ventana = ventana
        ventana.geometry("1000x600")
        ventana.title("Slot tracker")
        ventana.resizable(False, False)
        ventana.config(bg="lightgreen")

    def detener(self):
        self.evaluar = False
        return

    def evaluar(self):
        self.evaluar = True
        return