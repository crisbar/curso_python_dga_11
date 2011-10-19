#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
@author: Luis Pérez

Ejemplo de emisión de señales
'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


TEMPERATURES = [u"Frío", "Templado", "Calor"] 
TEMP_COLORS = ["blue", "orange", "red"]

class TemperatureLabel(QLabel):


    def __init__(self, parent=None):
        super(TemperatureLabel, self).__init__(parent)
        self.temperature_changed(0)

    def temperature_changed(self, level):
        self.setText(u"<span style='color:{1}'>{0}</span>".format(TEMPERATURES[level], TEMP_COLORS[level]))

class TemperatureDial(QDial):

    temperatureChanged = pyqtSignal(int)


class EmitingSignalsExample(QDialog):


    def __init__(self, parent=None):
        super(EmitingSignalsExample, self).__init__(parent)

        self.dial = TemperatureDial()
        spinner = QSpinBox()

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        label = TemperatureLabel()
        hbox.addWidget(self.dial)
        hbox.addWidget(spinner)
        vbox.addLayout(hbox)
        vbox.addWidget(label)
        self.setLayout(vbox)

        self.dial.valueChanged.connect(spinner.setValue)
        spinner.valueChanged.connect(self.emit_temperature_change)
        self.dial.temperatureChanged.connect(label.temperature_changed)

        self.setWindowTitle("Using default signals")
        self.resize(300, 100)

    def emit_temperature_change(self, value):

        level = min(int((float(value) / 100) * 3), 2)
        self.dial.temperatureChanged.emit(level)
        # equivalente old-style:  self.dial.emit(SIGNAL("temperatureChanged(int)"), level)

        

app = QApplication(sys.argv)
dialog = EmitingSignalsExample()
dialog.show()
sys.exit(app.exec_())
