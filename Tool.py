# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 23:21:57 2019

@author: hp
"""
import sys
import cv2
import matplotlib.pyplot as plt
import utils
from  PyQt5 import QtGui as gui
import PyQt5.QtWidgets as widgets
from PyQt5.QtWidgets import QApplication as app
from PyQt5.QtWidgets import QWidget as widget
import  PyQt5.QtCore as QtCore

class Window(widget):
    def __init__(self):
        super(Window,self).__init__()
        self.dims={'left':50,'right':50,'top':10,'width':500,'height':500}
        self.GridCell={'verticle':self.dims['height']/20,'horizontal':self.dims['width']/20}
        self.setWindowTitle("TransformTool")
        self.Image_cv2=cv2.imread('./Test.jpg',cv2.IMREAD_GRAYSCALE)
        self.Image=widgets.QLabel(self)
        self.currentTransform=''
        self.Home()
        
    
    def Home(self):
        Button=widgets.QPushButton('Transform',self)
        self.InputField=widgets.QLineEdit(self)
        InputLabel=widgets.QLabel('Transform Function:',self)
        
        im=gui.QImage(self.Image_cv2.data,self.Image_cv2.shape[1],self.Image_cv2.shape[0],gui.QImage.Format_RGB888)
        PixMap=gui.QPixmap(im)
        PixMap=PixMap.scaled(self.GridCell['horizontal']*18,self.GridCell['verticle']*13)
        #laying out widgets
        self.setGeometry(self.dims['left'],self.dims['top'],self.dims['width'],self.dims['height'])
        self.Image.setPixmap(PixMap)
        self.Image.resize(self.GridCell['horizontal']*18,self.GridCell['verticle']*13)
        self.Image.move(self.GridCell['horizontal']*1,self.GridCell['verticle']*2)
        InputLabel.move(self.GridCell['horizontal']*1,self.GridCell['verticle']*15)
        self.InputField.resize(self.GridCell['horizontal']*18,self.GridCell['verticle']*1.5)
        self.InputField.move(self.GridCell['horizontal']*1,self.GridCell['verticle']*16)
        Button.move(self.GridCell['horizontal']*1,self.GridCell['verticle']*18)
        #actions
        Button.clicked.connect(self.TransformToolAction)
        self.show()    
    
    def TransformToolAction(self):
            updatedim=utils.transform_Image(self.Image_cv2,self.InputField.text())
            im=gui.QImage(updatedim,self.Image_cv2.shape[1],self.Image_cv2.shape[0],gui.QImage.Format_RGB888)
            PixMap=gui.QPixmap(im)
            PixMap=PixMap.scaled(self.GridCell['horizontal']*18,self.GridCell['verticle']*13)        
            self.Image.setPixmap(PixMap)
    
if __name__ == '__main__':
    w=Window()
    App=app(sys.argv)
    sys.exit(App.exec_())
    

