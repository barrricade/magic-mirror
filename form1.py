# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form4.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
import math
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
class Ui_MainWindow(object):
    def __int__(self):
        self.image = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 904)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 260, 481, 371))
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget_1 = QtWidgets.QWidget(self.centralwidget)
        self.widget_1.setGeometry(QtCore.QRect(370, 780, 371, 71))
        self.widget_1.setObjectName("widget_1")
        self.horizontalSlider = QtWidgets.QSlider(self.widget_1)
        self.horizontalSlider.setGeometry(QtCore.QRect(79, 40, 231, 22))
        self.horizontalSlider.setMinimum(-5)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setPageStep(5)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget_1)
        self.lcdNumber.setGeometry(QtCore.QRect(160, 10, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(370, 770, 371, 71))
        self.widget_2.setObjectName("widget_2")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.widget_2)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(79, 40, 231, 22))
        self.horizontalSlider_2.setMinimum(-8)
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setPageStep(5)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addAction(self.action_4)
        self.menu_2.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menu_2.addAction(self.action_7)
        self.widget_1.hide()
        self.widget_2.hide()
        self.horizontalSlider.valueChanged.connect(self.amplify)
        self.horizontalSlider_2.valueChanged.connect(self.distore)
        self.action.triggered.connect(self.start)
        self.action_2.triggered.connect(self.amplify)
        self.action_3.triggered.connect(self.distore)
        self.action_4.triggered.connect(self.triangle)
        self.action_5.triggered.connect(self.S)
        self.action_6.triggered.connect(self.wave)
        self.action_7.triggered.connect(self.trapezoid)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "开始"))
        self.menu_2.setTitle(_translate("MainWindow", "哈哈镜"))
        self.action.setText(_translate("MainWindow", "加载图片"))
        self.action_2.setText(_translate("MainWindow", "放大缩小"))
        self.action_3.setText(_translate("MainWindow", "水平凹凸"))
        self.action_4.setText(_translate("MainWindow", "三角形"))
        self.action_5.setText(_translate("MainWindow", "S形"))
        self.action_6.setText(_translate("MainWindow", "波浪型"))
        self.action_7.setText(_translate("MainWindow", "梯形"))
    def start(self):
        picture = QFileDialog.getOpenFileName()
        self.image = cv2.imread(str(picture[0]))
        (row, col, channel) = self.image.shape
        QImg = QtGui.QImage(self.image.data, row, col, 3 * col, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(QImg)
        self.label.resize(row, col)
        self.label.setPixmap(pixmap)
        self.label.move(350, 200)
    def amplify(self):             #放大缩小
        (row, col, channel) = self.image.shape
        self.widget_1.show()
        self.widget_2.hide()
        value = self.horizontalSlider.value()
        if value >=0:
            scale = value / 10 + 1
            self.lcdNumber.display(scale)
        elif value >= -5 and value < 0:
            scale = 1 + value / 10
            self.lcdNumber.display(scale)
        drow = round(scale * row)
        dcol = round(scale * col)
        dst = np.zeros((drow, dcol,channel), np.uint8)
        for i in range(drow - 1):
            for j in range(dcol - 1):
                srcx = round(i * (1 / scale))
                srcy = round(j * (1 / scale))
                dst[i, j] = self.image[srcx, srcy]
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        QImg = QtGui.QImage(dst.data, drow, dcol, 3 * dcol, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(QImg)
        self.label.resize(drow, dcol)
        self.label.setPixmap(pixmap)
        self.label.move(350 - value * 4, 200 - value * 4)

    def distore(self):
        '''self.image = cv2.imread('D:\pic\lena3.jpg')'''
        try:
        (row, col, channel) = self.image.shape
        centre_x = int(col / 2)
        centre_y = int(row / 2)
        distance = 0
        radiu = int(row * 0.4)
        self.widget_1.hide()
        self.widget_2.show()
        value = self.horizontalSlider_2.value()
        if value >=0:
            value = value / 10 + 1
        else:
            value = 1 + value / 10
        a = (1 - value) / (radiu * radiu)
        b = value
        dst = np.zeros((row, col, channel), np.uint8)
        for i in range(row - 2):
            for j in range(col - 2):
                distance = (i - centre_x) * (i - centre_x) + (j - centre_y) * (j - centre_y)
                if math.sqrt(distance) <= radiu and distance != 0:
                    scale = a * math.sqrt(distance) * math.sqrt(distance) + b
                    src_x = int((1 - scale) * (centre_x - i) + i)
                    src_y = int((1 - scale) * (centre_y - j) + j)
                    dst[i, j] = self.image[src_x, src_y]
                else:
                    dst[i, j] = self.image[i,j]
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        QImg = QtGui.QImage(dst.data, row, col, 3 * col, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(QImg)
        self.label.resize(row, col)
        self.label.setPixmap(pixmap)
        self.label.move(350, 200)
        except:

    def triangle(self):
        '''self.image = cv2.imread('D:\pic\lena3.jpg')'''
        (row, col, channel) = self.image.shape
        self.widget_1.hide()
        self.widget_2.hide()
        dst = np.zeros((row, col, channel), np.uint8)
        n = col / row
        for i in range(row):
            m = int(n * i + 0.5)
            for j in range(m):
                dst[i, j] = self.image[i, int(j * (col / m) + 0.5)]
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        QImg = QtGui.QImage(dst.data, row, col, 3 * col, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(QImg)
        self.label.resize(row, col)
        self.label.setPixmap(pixmap)
        self.label.move(350, 200)

    def S(self):
        '''self.image = cv2.imread('D:\pic\lena3.jpg')'''
        (row, col, channel) = self.image.shape
        self.widget_1.hide()
        self.widget_2.hide()
        dst = np.zeros((row + 60, col + 60, channel), np.uint8)
        for i in range(row - 1):
            x = i * (1.5 * math.pi / col)
            m = int(30 * math.sin(x) + 30 + 0.5)
            for j in range(col - 1):
                dst[i, j + m] = self.image[i, j]
        (row1, col1, channel) = dst.shape
        for i in range(row1):
            for j in range(col1):
                if dst[i, j, 0] == 0 and dst[i, j, 1] == 0 and dst[i, j, 2] == 0:
                    dst[i, j] = [240, 240, 240]
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        QImg = QtGui.QImage(dst.data, col1, row1, 3 * col1, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(QImg)
        self.label.resize(row1, col1)
        self.label.setPixmap(pixmap)
        self.label.move(350, 200)

    def wave(self):
        '''self.image = cv2.imread('D:\pic\lena3.jpg')'''
        (row, col, channel) = self.image.shape
        self.widget_1.hide()
        self.widget_2.hide()
        dst = np.zeros((row + 60, col + 60, channel), np.uint8)
        for j in range(col - 1):
            y = j * (2 * math.pi / row)
            m = int(30 * math.sin(y) + 30 + 0.5)
            for i in range(row - 1):
                dst[i + m, j] = self.image[i, j]
        (row1, col1, channel) = dst.shape
        for i in range(row1):
            for j in range(col1):
                if dst[i, j, 0] == 0 and dst[i, j, 1] == 0 and dst[i, j, 2] == 0:
                    dst[i, j] = [240, 240, 240]
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        QImg = QtGui.QImage(dst.data, col1, row1, 3 * col1, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(QImg)
        self.label.resize(row1, col1)
        self.label.setPixmap(pixmap)
        self.label.move(350, 200)

    def trapezoid(self):
        '''self.image = cv2.imread('D:\pic\lena3.jpg')'''
        (row, col, channel) = self.image.shape
        self.widget_1.hide()
        self.widget_2.hide()
        x1 = 0
        y1 = 0.3 * col
        x2 = 0
        y2 = 0.6 * col
        a1 = -row / (0.3 * col)
        b1 = row
        a2 = row / (0.4 * col)
        b2 = row - (row / 0.4)
        dst = np.zeros((row, col, channel), np.uint8)
        for i in range(row - 1):
            left = int((i - b1) / a1)
            right = int((i - b2) / a2)
            scale = (right - left) / col
            for j in range(left, right):
                srcy = round((j - left) * (1 / scale))
                dst[i, j] = self.image[i, srcy]

        for i in range(row):
            for j in range(col):
                if dst[i, j, 0] == 0 and dst[i, j, 1] == 0 and dst[i, j, 2] == 0:
                    dst[i, j] = [240, 240, 240]
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        QImg = QtGui.QImage(dst.data, col, row, 3 * col, QtGui.QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(QImg)
        self.label.resize(row, col)
        self.label.setPixmap(pixmap)
        self.label.move(350, 200)

