# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import platform
import sys
import time

import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import *
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog, QLabel

import camera
from concentration import attendance_percentage, total_concentration_percentage


class Ui_MainWindow(object):
    
 
    def setupUi(self, MainWindow):

        self.main_window = MainWindow

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1174, 769)
        MainWindow.setStyleSheet("background-color: rgb(92, 53, 102);\n"
                                "background-color: rgb(206, 92, 0);\n"
                                "background-color: rgb(205, 204,229);")  

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 0, 461, 101))
        font = QtGui.QFont()
        font.setFamily("MathJax_Math")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(92, 53, 102);\n"
                                "color: rgb(32, 74, 135);\n"
                                "")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_browse = QtWidgets.QPushButton(self.centralwidget)
        self.btn_browse.setGeometry(QtCore.QRect(430, 160, 151, 41))
        self.btn_browse.setStyleSheet("background-color: rgb(92, 53, 102);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 15px;\n"
                                        "border-color: black;\n"
                                        "border-color: black;\n"
                                        "padding: 4px;\n"
                                        "font: bold 18px;\n"
                                        "color: white")


        self.btn_browse.setObjectName("btn_browse")

        self.btn_browse.clicked.connect(self.file_dialog)

        self.te_broswe = QtWidgets.QLineEdit(self.centralwidget)
        self.te_broswe.setGeometry(QtCore.QRect(40, 160, 361, 41))
        self.te_broswe.setObjectName("te_broswe")
        self.btn_analyze = QtWidgets.QPushButton(self.centralwidget)
        self.btn_analyze.setGeometry(QtCore.QRect(150, 260, 171, 51))
        self.btn_analyze.setStyleSheet("background-color: rgb(92, 53, 102);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 15px;\n"
                                        "border-color: black;\n"
                                        "border-color: black;\n"
                                        "padding: 4px;\n"
                                        "font: bold 18px;\n"
                                        "color: white")
        self.btn_analyze.setObjectName("btn_analyze")


        self.btn_analyze.clicked.connect(self.analyze)


        self.btn_open_camera = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_camera.setGeometry(QtCore.QRect(890, 160, 211, 61))
        self.btn_open_camera.setStyleSheet("background-color: rgb(92, 53, 102);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 15px;\n"
                                        "border-color: black;\n"
                                        "border-color: black;\n"
                                        "padding: 4px;\n"
                                        "font: bold 18px;\n"
                                        "color: white")
        self.btn_open_camera.setObjectName("btn_open_camera")
        self.btn_open_camera.clicked.connect(self.open_cam_window)





        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 340, 1081, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.text_result = QtWidgets.QTextBrowser(self.centralwidget)
        self.text_result.setGeometry(QtCore.QRect(30, 370, 1081, 351))
        self.text_result.setObjectName("text_result")
        self.text_result.setStyleSheet("font: 20px")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 471, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(92, 53, 102);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1174, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label_student = QtWidgets.QLabel(self.centralwidget)
        self.label_student.setGeometry(QtCore.QRect(360, 230,300,50))
        self.label_student.setText('Enter the Number of students')
        self.label_student.setFont(font)
        self.label_student.setStyleSheet("color: rgb(92, 53, 102);")
        self.te_students = QtWidgets.QLineEdit(self.centralwidget)
        self.te_students.setGeometry(QtCore.QRect(360, 270, 200, 41))
        self.te_students.setObjectName("te_broswe")
        self.te_students.setFont(font)
        


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Focus Analysis"))
        self.btn_browse.setText(_translate("MainWindow", "Browse"))
        self.btn_analyze.setText(_translate("MainWindow", "Analyze "))
        self.btn_open_camera.setText(_translate("MainWindow", "Open Camera"))
        self.text_result.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'PowerlineSymbols Medium\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Please choose the path for the videos directory"))

    def open_cam_window(self):
     
        self.cam_window = Cam_Window()
        self.cam_window.show()
        # self.cam_window.open_cam()

        # print(camera.camera_concentration())
 
    def file_dialog(self):
        fileName = QFileDialog.getExistingDirectory(self.main_window, 'Select Directory')
        self.te_broswe.setText(fileName)
        print(fileName)

    def analyze(self):

        vid_folder = str(self.te_broswe.text())

        if platform.system() =='Linux':
            vid_folder += '/'
        elif platform.system() == 'Windows':
            vid_folder += '\\'
        else:
            print("We don't support Mac OS")
            

        print(vid_folder)
        percentages,res = total_concentration_percentage(vid_folder,self)
 
        num_of_students = int(self.te_students.text() )
        attendance = attendance_percentage(num_of_students, vid_folder)

        for entry in percentages:
            s = f' {entry[0]} has concentration of:  {entry[1]}%'
            self.text_result.append(s)

        res_str = f'The Average concentration for all people is: {res}%'

        self.text_result.append(res_str)

        attendance_str = f'The Attendance for all people is: {attendance}%'

        self.text_result.append(attendance_str)

        print(percentages, attendance)








class Thread(QThread):


    def __init__(self):
        super().__init__()
        self._run_flag = True


    changePixmap = pyqtSignal(QImage)

    def run(self):
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            time.sleep(0.05)
            ret, frame = cap.read()
            if ret:
                
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)

        cap.release()
            

    def stop(self):

        self._run_flag = False
        self.wait()


class Cam_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.COUNTER=0.0
        self.SUM= 0.0
        self.setWindowTitle("Qt static label demo")


        self.setObjectName("MainWindow")
        self.resize(1174, 769)
        self.setStyleSheet("background-color: rgb(92, 53, 102);\n"
                                "background-color: rgb(206, 92, 0);\n"
                                "background-color: rgb(205, 204,229);")



        self.disply_width = 640
        self.display_height = 480
        self.image_label = QLabel(self)
        self.image_label.resize(self.disply_width, self.display_height)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setGeometry(QtCore.QRect(210, 40, 640, 480))




        self.status = QtWidgets.QLabel(self)
        self.status.setGeometry(QtCore.QRect(210, 600, 471, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setStyleSheet("color: rgb(92, 53, 102);")
        self.status.setAlignment(QtCore.Qt.AlignCenter)

        self.status.setText('Processing........')






        self.btn_close = QtWidgets.QPushButton(self)
        self.btn_close.setGeometry(QtCore.QRect(900, 700, 151, 41))
        self.btn_close.setStyleSheet("background-color: rgb(92, 53, 102);\n"
                                        "border-style: outset;\n"
                                        "border-width: 2px;\n"
                                        "border-radius: 15px;\n"
                                        "border-color: black;\n"
                                        "border-color: black;\n"
                                        "padding: 4px;\n"
                                        "font: bold 18px;\n"
                                        "color: white")
        self.btn_close.setText('Finish') 

        self.btn_close.clicked.connect(self.close_window)

        
        
        self.th = Thread()
        self.th.changePixmap.connect(self.setImage)
        self.th.start()
        
    
    def qimage_to_array(self,image):
        size = image.size()
        s = image.bits().asstring(size.width() * size.height() * image.depth() // 8)
        arr = np.fromstring(s, dtype=np.uint8).reshape((size.height(), size.width(), image.depth() // 8))
        return arr


    @pyqtSlot(QImage)
    def setImage(self, image):
        
        self.COUNTER +=1
        converted_image =   self.qimage_to_array(image)
        self.SUM += camera.camera_concentration(converted_image)
        self.image_label.setPixmap(QPixmap.fromImage(image))



    def closeEvent(self, event):
        self.th.stop()
        event.accept()


    def close_window(self):
        self.th.stop()

        avg = str (  round(self.SUM / self.COUNTER,2 )  )
        avg_str = f' The Average Concentration is:{avg}% '
       
        self.status.setText(avg_str)
        # event.accept()
        # self.th.exit()
        #self.close()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
