import tkinter
import UI as ui
import pyautogui as au

def verificar1():
    if au.locateOnScreen("../images/c4/c41.png",region=(280, 400, 360, 490), confidence=0.7):
        return True
    return False

def verificar2():
    return

def verificar3():
    return

def main():
    while True:
        if gui.evaluar:
            print(verificar1())
            #gui.detener()
    return


if __name__ == '__main__':
    ventanaPrincipal = tkinter.Tk()
    gui = ui.Panel(ventanaPrincipal)
    main()

    ventanaPrincipal.mainloop()