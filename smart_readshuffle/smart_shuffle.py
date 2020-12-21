# -*- coding: utf-8 -*-

import nuke
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import Qt,Slot
import os
import sys
import random



class Shuffleconnect(QWidget):
    '''
    import sys
    from smart_readshuffle import smart_shuffle
    reload(smart_shuffle)
    '''

    def __init__(self,parent=None):
        QWidget.__init__(self)
        self.select_readnode = ['red_light', 'blue_Light', 'ornage_Light', 'green_Light']
        # window name
        self.window_name = 'shuffle read to connect'

        self.setWindowTitle(self.window_name)
        # suffle list1
        self.text1 = QLabel("Connect read name list1")
        self.btn1 = QPushButton("click1")

        # # merge list2
        self.text2 = QLabel("Connect shuffle merge list2")
        self.btn2 = QPushButton('click2')

        self.text1.setAlignment(Qt.AlignCenter)
        self.text2.setAlignment(Qt.AlignCenter)

        self.vb = QHBoxLayout()
        self.setLayout(self.vb)

        self.vbL = QVBoxLayout()
        self.vbR = QVBoxLayout()
        self.vb.addLayout(self.vbL)
        self.vb.addLayout(self.vbR)

        self.vb.addLayout(self.vbL)
        self.vb.addLayout(self.vbR)

        self.vbL.addWidget(self.text1)
        self.vbL.addWidget(self.btn1)
        self.vbR.addWidget(self.text2)
        self.vbR.addWidget(self.btn2)


        self.btn1.clicked.connect(self.magic)
        self.btn2.clicked.connect(self.magic)
        self.show()

    @Slot()
    def magic(self):
        self.text1.setText(random.choice(self.select_readnode))
        self.text2.setText(random.choice(self.select_readnode))





widget = Shuffleconnect()
widget.resize(800, 600)
widget.show()
