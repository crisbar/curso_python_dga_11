#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
@author: Luis Perez

Ejercicio de emision de señales propias.
'''

import sys
from PyQt4 import QtGui, QtCore

class UpdateButton(QtGui.QPushButton):

    counterUpdated = QtCore.pyqtSignal(int)


class PushUpdateDial(QtGui.QWidget):
  
    def __init__(self):
        super(PushUpdateDial, self).__init__()
        self.initUI()
        self.curval = 0
    
    def update_dial(self):
        self.curval = self.curval + 10
        self.btn.counterUpdated.emit(self.curval)

    def initUI(self):

        dial = QtGui.QDial()
        self.btn = UpdateButton("Pulsame!")

        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.btn)
        vbox.addWidget(dial)

        self.setLayout(vbox)
        self.btn.clicked.connect(self.update_dial)
        self.btn.counterUpdated.connect(dial.setValue)

        self.setWindowTitle('Signals y slots')
        self.resize(250, 150)


app = QtGui.QApplication(sys.argv)
ex = PushUpdateDial()
ex.show()
sys.exit(app.exec_())
