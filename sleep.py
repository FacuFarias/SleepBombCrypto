# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sleep.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SleepBomb(object):
    def setupUi(self, SleepBomb):
        SleepBomb.setObjectName("SleepBomb")
        SleepBomb.resize(620, 350)
        SleepBomb.setStyleSheet("QLabel#Titulo\n"
"{\n"
"color:white;\n"
"}\n"
"\n"
"\n"
"QPushButton\n"
"{\n"
"background: qlineargradient(spread:pad, x1:1, y1:0.739, x2:1, y2:0.25, stop:0 #ee7624, stop:1 #f5a322);\n"
"border-radius:5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-color: #f56e22;\n"
"color:white;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background: qlineargradient(spread:pad, x1:1, y1:0.739, x2:1, y2:0.5, stop:0 #ee7624, stop:1 #f5a322);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(SleepBomb)
        self.centralwidget.setObjectName("centralwidget")
        self.Menu = QtWidgets.QFrame(self.centralwidget)
        self.Menu.setGeometry(QtCore.QRect(310, 60, 261, 241))
        self.Menu.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Menu.setObjectName("Menu")
        self.b_iniciar = QtWidgets.QPushButton(self.Menu)
        self.b_iniciar.setGeometry(QtCore.QRect(80, 120, 101, 41))
        font = QtGui.QFont()
        font.setFamily("BankGothic Lt BT")
        font.setPointSize(12)
        self.b_iniciar.setFont(font)
        self.b_iniciar.setObjectName("b_iniciar")
        self.b_cerrar = QtWidgets.QPushButton(self.Menu)
        self.b_cerrar.setGeometry(QtCore.QRect(80, 170, 101, 41))
        font = QtGui.QFont()
        font.setFamily("BankGothic Lt BT")
        font.setPointSize(12)
        self.b_cerrar.setFont(font)
        self.b_cerrar.setObjectName("b_cerrar")
        self.Titulo_2 = QtWidgets.QLabel(self.Menu)
        self.Titulo_2.setGeometry(QtCore.QRect(90, 3, 161, 20))
        font = QtGui.QFont()
        font.setFamily("BankGothic Lt BT")
        font.setPointSize(23)
        self.Titulo_2.setFont(font)
        self.Titulo_2.setObjectName("Titulo_2")
        self.label_2 = QtWidgets.QLabel(self.Menu)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 81, 21))
        font = QtGui.QFont()
        font.setFamily("BankGothic Lt BT")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.le_horas = QtWidgets.QLineEdit(self.Menu)
        self.le_horas.setGeometry(QtCore.QRect(30, 60, 41, 21))
        self.le_horas.setMaxLength(1)
        self.le_horas.setObjectName("le_horas")
        self.label = QtWidgets.QLabel(self.Menu)
        self.label.setGeometry(QtCore.QRect(0, 0, 261, 241))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/imagenes/rec2.png"))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.Menu)
        self.label_4.setGeometry(QtCore.QRect(73, 60, 21, 21))
        font = QtGui.QFont()
        font.setFamily("BankGothic Lt BT")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.le_min = QtWidgets.QLineEdit(self.Menu)
        self.le_min.setGeometry(QtCore.QRect(90, 60, 41, 21))
        self.le_min.setMaxLength(2)
        self.le_min.setObjectName("le_min")
        self.label_5 = QtWidgets.QLabel(self.Menu)
        self.label_5.setGeometry(QtCore.QRect(133, 60, 31, 21))
        font = QtGui.QFont()
        font.setFamily("BankGothic Lt BT")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.le_seg = QtWidgets.QLineEdit(self.Menu)
        self.le_seg.setGeometry(QtCore.QRect(170, 61, 41, 21))
        self.le_seg.setText("")
        self.le_seg.setMaxLength(2)
        self.le_seg.setObjectName("le_seg")
        self.label_6 = QtWidgets.QLabel(self.Menu)
        self.label_6.setGeometry(QtCore.QRect(213, 60, 41, 21))
        font = QtGui.QFont()
        font.setFamily("BankGothic Lt BT")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label.raise_()
        self.b_iniciar.raise_()
        self.b_cerrar.raise_()
        self.Titulo_2.raise_()
        self.label_2.raise_()
        self.le_horas.raise_()
        self.label_4.raise_()
        self.le_min.raise_()
        self.label_5.raise_()
        self.le_seg.raise_()
        self.label_6.raise_()
        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(30, 20, 371, 31))
        font = QtGui.QFont()
        font.setFamily("BankGothic Md BT")
        font.setPointSize(22)
        self.Titulo.setFont(font)
        self.Titulo.setObjectName("Titulo")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 621, 341))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/imagenes/bomb-background.png"))
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.Menu.raise_()
        self.Titulo.raise_()
        SleepBomb.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SleepBomb)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")
        SleepBomb.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SleepBomb)
        self.statusbar.setObjectName("statusbar")
        SleepBomb.setStatusBar(self.statusbar)

        self.retranslateUi(SleepBomb)
        QtCore.QMetaObject.connectSlotsByName(SleepBomb)

    def retranslateUi(self, SleepBomb):
        _translate = QtCore.QCoreApplication.translate
        SleepBomb.setWindowTitle(_translate("SleepBomb", "MainWindow"))
        self.b_iniciar.setText(_translate("SleepBomb", "Iniciar"))
        self.b_cerrar.setText(_translate("SleepBomb", "Cerrar"))
        self.Titulo_2.setText(_translate("SleepBomb", "Menu"))
        self.label_2.setText(_translate("SleepBomb", "refresh:"))
        self.le_horas.setText(_translate("SleepBomb", "3"))
        self.label_4.setText(_translate("SleepBomb", "H"))
        self.label_5.setText(_translate("SleepBomb", "min"))
        self.label_6.setText(_translate("SleepBomb", "seg"))
        self.Titulo.setText(_translate("SleepBomb", "Sleep Bomb Crypto"))
import imagenes


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SleepBomb = QtWidgets.QMainWindow()
    ui = Ui_SleepBomb()
    ui.setupUi(SleepBomb)
    SleepBomb.show()
    sys.exit(app.exec_())
