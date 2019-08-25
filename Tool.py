# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 23:21:57 2019

@author: hp
"""
import sys
import cv2
#import matplotlib.pyplot as plt
import utils
from  PyQt5 import QtGui as gui
import PyQt5.QtWidgets as widgets
from PyQt5.QtWidgets import QApplication as app
from PyQt5.QtWidgets import QWidget as widget
import  PyQt5.QtCore as QtCore

class Window(widget):
    def __init__(self):
        super(Window,self).__init__()
        self.dims={'left':50,'right':50,'top':10,'width':500,'height':550}
        self.GridCell={'verticle':self.dims['height']/20,'horizontal':self.dims['width']/20}
        self.setWindowTitle("TransformTool")
        self.Image_cv2=cv2.imread('./Test.jpg')
        self.original=cv2.imread('./Test.jpg')
        self.Image=widgets.QLabel(self)
        self.currentTransform=''
        self.setGeometry(self.dims['left'],self.dims['top'],self.dims['width'],self.dims['height'])
        self.Load()
        self.Home()
    
    def save(self):
        pass

        
    def Load(self):
        self.setWindowTitle("Pick An Image")
        Prompt=widgets.QLabel('Pick an Image')
        Prompt.move(self.GridCell['horizontal']*1,self.GridCell['verticle']*2)
       # Load_btn=widgets.QPushButton('Load',self)
        picker_name=widgets.QFileDialog.getOpenFileName(self)
        self.Image_cv2=cv2.imread(picker_name[0])
        self.original=cv2.imread(picker_name[0])
        self.build_img()
    
    def build_img(self):
        self.pmi=gui.QImage(self.Image_cv2.data,self.Image_cv2.shape[1],self.Image_cv2.shape[0],self.Image_cv2.shape[1]*3,gui.QImage.Format_RGB888)
        self.PixMap=gui.QPixmap(self.pmi)
        self.PixMap=self.PixMap.scaled(self.GridCell['horizontal']*18,self.GridCell['verticle']*13)
        self.Image.setPixmap(self.PixMap)

    def Home(self):
        self.setWindowTitle("TransformTool")
        Button=widgets.QPushButton('Transform',self)
        Load_btn=widgets.QPushButton('Load ',self)
        Reset_button=widgets.QPushButton('Reset',self)
        self.InputField=widgets.QLineEdit(self)
        InputLabel=widgets.QLabel('Transform Function( ƒ(x) ):',self)
        self.build_img()
        #laying out widgets
        self.Image.resize(self.GridCell['horizontal']*18,self.GridCell['verticle']*13)
        self.Image.move(self.GridCell['horizontal']*1,self.GridCell['verticle']*3)
        Load_btn.move(self.GridCell['horizontal']*1,self.GridCell['verticle']*1)
        InputLabel.move(self.GridCell['horizontal']*1,self.GridCell['verticle']*15)
        self.InputField.resize(self.GridCell['horizontal']*18,self.GridCell['verticle']*1.5)
        self.InputField.move(self.GridCell['horizontal']*1,self.GridCell['verticle']*16)
        Button.move(self.GridCell['horizontal']*1,self.GridCell['verticle']*18)
        Reset_button.move(self.GridCell['horizontal']*15.5,self.GridCell['verticle']*18)
        #actions
        Reset_button.clicked.connect(self.Reset)
        Load_btn.clicked.connect(self.Load)
        Button.clicked.connect(self.TransformToolAction)
    
    def Reset(self):
        self.Image_cv2=self.original
        self.build_img()
        
    
    def TransformToolAction(self):
        updatedim=utils.transform_Image(self.Image_cv2,self.InputField.text())
        self.Image_cv2=updatedim
        self.build_img()

if __name__ == '__main__':
    App=app(sys.argv)
    w=Window()
    w.show()
    sys.exit(App.exec_())
    

