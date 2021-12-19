import sys

from numpy import imag
from sleep import *
from os import path
import pyautogui
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread

from webbrowser import get
timer=3600

class WorkerThread(QThread):
    def run(self):
        global timer
        url='https://app.bombcrypto.io/'
        get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(url)

        sleep(3)   
        #boton=pyautogui.locateOnScreen(mi_app.p_connect)

        pixmap=QtGui.QPixmap(mi_app.p_connect)
        imagen = pixmap.toImage()
        imagen.save('imagenpix.png')
        boton=pyautogui.locateOnScreen('imagenpix.png')

        while not boton:
            boton=pyautogui.locateOnScreen('imagenpix.png')
            sleep(1)
        #im = pyautogui.screenshot('imagen.png',region=(550,510, 285, 125))

        sleep(1)
        pyautogui.moveTo(boton.left+int(boton.width/2),boton.top+int(boton.height/2))
        pyautogui.click()

        pyautogui.moveTo(boton.left+int(boton.width/2),438)
        pyautogui.click()
        print("busncando firmar")
        pixmap=QtGui.QPixmap(mi_app.p_firmar)
        imagen = pixmap.toImage()
        imagen.save('imagenpix.png')
        sleep(5)
        b_firmar= pyautogui.locateOnScreen('imagenpix.png')

        while not b_firmar:
            b_firmar= pyautogui.locateOnScreen('imagenpix.png')
            sleep(1)

        pyautogui.moveTo(b_firmar.left+int(b_firmar.width/2),b_firmar.top+int(b_firmar.height/2))
        pyautogui.click()
        timer1=0
        #Presionar en Heroes
        print("Buscando heroes")
        pixmap=QtGui.QPixmap(mi_app.p_heroes)
        imagen = pixmap.toImage()
        imagen.save('imagenpix.png')
        b_heroes=pyautogui.locateOnScreen('imagenpix.png')

        while not b_heroes:
            b_heroes= pyautogui.locateOnScreen('imagenpix.png')
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

        #Verificación de la cuenta
        pixmap=QtGui.QPixmap(mi_app.p_codigo)
        imagen = pixmap.toImage()
        imagen.save('imagenpix.png')
        b_codigo=pyautogui.locateOnScreen('imagenpix.png')

        if not b_codigo:
            print("esta no es tu cuenta")
            pyautogui.keyDown("ctrl")
            pyautogui.press("w")
            pyautogui.keyUp("ctrl")
            self.run()

        else:
            print("verificado")



        bombers=4
        pixmap=QtGui.QPixmap(mi_app.p_work)
        imagen = pixmap.toImage()
        imagen.save('imagenpix.png')
        b_work=pyautogui.locateOnScreen('imagenpix.png')

        while b_work:
            pyautogui.moveTo(b_work.left+int(b_work.width/2),b_work.top+int(b_work.height/2))
            pyautogui.click()
            b_work=pyautogui.locateOnScreen('imagenpix.png')
            sleep(1)
        print("sali de los trabajadores")


        pixmap=QtGui.QPixmap(mi_app.p_back)
        imagen = pixmap.toImage()
        imagen.save('imagenpix.png')
        b_back=pyautogui.locateOnScreen('imagenpix.png')
        while not b_back:
            b_back=pyautogui.locateOnScreen('imagenpix.png')
            sleep(2)
            print("no encuentro el back")

        pyautogui.moveTo(b_back.left+int(b_back.width/2),b_back.top+int(b_back.height/2))
        pyautogui.click()

        pixmap=QtGui.QPixmap(mi_app.p_treasure)
        imagen = pixmap.toImage()
        imagen.save('imagenpix.png')
        b_treasure=pyautogui.locateOnScreen('imagenpix.png')

        while not b_treasure:
            b_treasure=pyautogui.locateOnScreen('imagenpix.png')
            sleep(2)
        pyautogui.moveTo(b_treasure.left+int(b_treasure.width/2),b_treasure.top+int(b_treasure.height/2))
        pyautogui.click()

        #Loop esperando ...
        tim=0
        while tim<=timer:
            pixmap=QtGui.QPixmap(mi_app.p_unknown)
            imagen = pixmap.toImage()
            imagen.save('imagenpix.png')
            b_unknown=pyautogui.locateOnScreen('imagenpix.png')

            if b_unknown:
                tim=0
                pyautogui.keyDown("ctrl")
                pyautogui.press("w")
                pyautogui.keyUp("ctrl")
                self.run()
            
            else:
                sleep(5)
                tim=tim+5
                b_unknown=pyautogui.locateOnScreen('imagenpix.png')
                print(tim)
            pixmap=QtGui.QPixmap(mi_app.p_newmap)
            imagen = pixmap.toImage()
            imagen.save('imagenpix.png')
            b_newmap=pyautogui.locateOnScreen('imagenpix.png')
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
        self.uibomb.b_cerrar.clicked.connect(self.prueba)
        self.uibomb.le_horas.editingFinished.connect(self.cambiartimer)
        self.uibomb.le_min.editingFinished.connect(self.cambiartimer)
        self.uibomb.le_seg.editingFinished.connect(self.cambiartimer)
        

    def iniciar(self):
        self.uibomb.b_iniciar.setEnabled(False)
        
        self.uibomb.b_iniciar.setStyleSheet("QPushButton {background: qlineargradient(spread:pad, x1:1, y1:0.739, x2:1, y2:0.5, stop:0 #777, stop:1 #999);}")
        
        self.worker=WorkerThread()
        self.worker.start()
        self.worker.finished.connect(self.detener)
        
         

    def detener(self):
        print("Se termino el programa")
        

    def prueba(self):
        pixmap=QtGui.QPixmap(":/imagenes/firmar.png")
        imagen = pixmap.toImage()
        imagen.save('imagenpix.png')

    def cambiartimer(self):
        
        global timer

        try:
            horas = int(self.uibomb.le_horas.text())
        except:
            print("insete horas validas")
            horas=0
        
        try:
            min =  int(self.uibomb.le_min.text())
        except:
            print("insete minutos validos")
            min=0

        try:
            seg = int(self.uibomb.le_seg.text())
        except:
            print("insete seg validos")
            seg=0

        
        timer = horas*3600 + min * 60 + seg
        print("El tiempo en segundos es de: "+str(timer))
    def cargarpath(self):
        
        self.p_connect=":/imagenes/imagen.png"
        self.p_firmar=':/imagenes/firmar.png'
        self.p_heroes=':/imagenes/heroes.png'
        self.p_work=':/imagenes/work.png'
        self.p_back=':/imagenes/back.png'
        self.p_treasure=':/imagenes/treasure.png'
        self.p_newmap=':/imagenes/newmap.png'
        self.p_unknown=':/imagenes/unknown.png'
        self.p_codigo=':/imagenes/codigo.png'


if __name__ == "__main__":
    mi_aplicacion=QApplication(sys.argv)
    mi_app = Ventana()
    sys.exit(mi_aplicacion.exec_())


#Claudia Francavilla
#3415694590