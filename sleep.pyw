import sys
from sleep import *
from os import path
import pyautogui
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread

from webbrowser import get

class WorkerThread(QThread):
    def run(self):

        url='https://app.bombcrypto.io/'
        get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)

        sleep(3)   
        #boton=pyautogui.locateOnScreen(mi_app.p_connect)
        boton=pyautogui.locateOnScreen(mi_app.p_connect)

        while not boton:
            boton=pyautogui.locateOnScreen(mi_app.p_connect)
            sleep(1)
        #im = pyautogui.screenshot('imagen.png',region=(550,510, 285, 125))

        sleep(1)
        pyautogui.moveTo(boton.left+int(boton.width/2),boton.top+int(boton.height/2))
        pyautogui.click()

        pyautogui.moveTo(boton.left+int(boton.width/2),438)
        pyautogui.click()


        b_firmar= pyautogui.locateOnScreen(mi_app.p_firmar)

        while not b_firmar:
            b_firmar= pyautogui.locateOnScreen(mi_app.p_firmar)
            sleep(1)

        pyautogui.moveTo(b_firmar.left+int(b_firmar.width/2),b_firmar.top+int(b_firmar.height/2))
        pyautogui.click()
        timer1=0
        #Presionar en Heroes
        b_heroes=pyautogui.locateOnScreen(mi_app.p_heroes)

        while not b_heroes:
            b_heroes= pyautogui.locateOnScreen(mi_app.p_heroes)
            sleep(1)
            timer1=timer1+1
            if timer1>=30:
                timer1=0
                pyautogui.keyDown("ctrl")
                pyautogui.press("w")
                pyautogui.keyUp("ctrl")
                self.run()

        pyautogui.moveTo(b_heroes.left+int(b_heroes.width/2),b_heroes.top+int(b_heroes.height/2))
        pyautogui.click()

        sleep(3)
        bombers=4
        b_work=pyautogui.locateOnScreen(mi_app.p_work)

        while b_work:
            pyautogui.moveTo(b_work.left+int(b_work.width/2),b_work.top+int(b_work.height/2))
            pyautogui.click()
            b_work=pyautogui.locateOnScreen(mi_app.p_work)
            sleep(2)
        print("sali de los trabajadores")
        b_back=pyautogui.locateOnScreen(mi_app.p_back)
        while not b_back:
            b_back=pyautogui.locateOnScreen(mi_app.p_back)
            sleep(2)
            print("no encuentro el back")

        pyautogui.moveTo(b_back.left+int(b_back.width/2),b_back.top+int(b_back.height/2))
        pyautogui.click()


        b_treasure=pyautogui.locateOnScreen(mi_app.p_treasure)

        while not b_treasure:
            b_treasure=pyautogui.locateOnScreen(mi_app.p_treasure)
            sleep(2)
        pyautogui.moveTo(b_treasure.left+int(b_treasure.width/2),b_treasure.top+int(b_treasure.height/2))
        pyautogui.click()

        #Loop esperando ...
        timer=0
        while timer<=3600:
            
            b_unknown=pyautogui.locateOnScreen(mi_app.p_unknown)

            if b_unknown:
                timer=0
                self.run()
            
            else:
                sleep(5)
                timer=timer+5
                b_unknown=pyautogui.locateOnScreen(mi_app.p_unknown)
                print(timer)

            b_newmap=pyautogui.locateOnScreen(mi_app.p_newmap)
            if b_newmap:
                pyautogui.moveTo(b_newmap.left+int(b_newmap.width/2),b_newmap.top+int(b_newmap.height/2))
                pyautogui.click()

        pyautogui.keyDown("ctrl")
        pyautogui.press("w")
        pyautogui.keyUp("ctrl")
        self.run()



class Ventana():
    def __init__(self):
        super().__init__()
        
        self.bomb = QtWidgets.QMainWindow()
        self.uibomb = Ui_SleepBomb()
        self.uibomb.setupUi(self.bomb)
        self.bomb.show()
        self.thread={}
        self.cargarpath()
        self.uibomb.b_iniciar.clicked.connect(self.iniciar)
        self.uibomb.b_cerrar.clicked.connect(self.bomb.close)
        url='https://google.com'
        get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)
        

    def iniciar(self):
        self.uibomb.b_iniciar.setEnabled(False)
        
        self.uibomb.b_iniciar.setStyleSheet("QPushButton {background: qlineargradient(spread:pad, x1:1, y1:0.739, x2:1, y2:0.5, stop:0 #777, stop:1 #999);}")
        
        self.worker=WorkerThread()
        self.worker.start()
        self.worker.finished.connect(self.detener)
        
         

    def detener(self):
        print("Se termino el programa")

    def cargarpath(self):
        
        self.p_connect=path.abspath('SleepBombCrypto/imagen.png')
        print(self.p_connect)
        self.p_firmar=path.abspath('SleepBombCrypto/firmar.png')
        
        self.p_heroes=path.abspath('SleepBombCrypto/heroes.png')
        self.p_work=path.abspath('SleepBombCrypto/work.png')
        self.p_back=path.abspath('SleepBombCrypto/back.png')
        self.p_treasure=path.abspath('SleepBombCrypto/treasure.png')
        self.p_newmap=path.abspath('SleepBombCrypto/newmap.png')
        self.p_unknown=path.abspath('SleepBombCrypto/unknown.png')


if __name__ == "__main__":
    mi_aplicacion=QApplication(sys.argv)
    mi_app = Ventana()
    sys.exit(mi_aplicacion.exec_())
