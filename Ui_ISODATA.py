# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ENVY\Documents\eric\ISODATA.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_ISODATA(object):
    def setupUi(self, ISODATA):
        ISODATA.setObjectName("ISODATA")
        ISODATA.setEnabled(True)
        ISODATA.resize(1600, 950)
        ISODATA.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'icon.png')))
        ISODATA.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralWidget = QtWidgets.QWidget(ISODATA)
        self.centralWidget.setObjectName("centralWidget")
        self.iconLabel = QtWidgets.QLabel(self.centralWidget)
        self.iconLabel.setObjectName('iconLabel')
        self.iconLabel.setGeometry(QtCore.QRect(10, 5, 30, 30))
        self.iconLabel.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), 'icon.png')))
        self.titleLabel = QtWidgets.QLabel(self.centralWidget)
        self.titleLabel.setObjectName('titleLabel')
        self.titleLabel.setText('ISODATA 图像分类')
        self.titleLabel.setGeometry(QtCore.QRect(50, 5, 200, 30))
        self.pushButton_close = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_close.setObjectName('pushButton_close')
        self.pushButton_close.setGeometry(QtCore.QRect(1560, 5, 30, 30))
        self.pushButton_close.setIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'close.png')))
        self.pushButton_close.setFlat(True)
        self.pushButton_min = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_min.setObjectName('pushButton_min')
        self.pushButton_min.setGeometry(QtCore.QRect(1520, 5, 30, 30))
        self.pushButton_min.setIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), 'min.png')))
        self.pushButton_min.setFlat(True)
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 300, 601))
        self.groupBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.groupBox.setObjectName("groupBox")
        self.widget_2 = QtWidgets.QWidget(self.groupBox)
        self.widget_2.setGeometry(QtCore.QRect(10, 60, 281, 571))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_K = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_K.setObjectName("lineEdit_K")
        self.gridLayout.addWidget(self.lineEdit_K, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_thetaN = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_thetaN.setObjectName("lineEdit_thetaN")
        self.gridLayout.addWidget(self.lineEdit_thetaN, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_thetaS = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_thetaS.setObjectName("lineEdit_thetaS")
        self.gridLayout.addWidget(self.lineEdit_thetaS, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_thetaC = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_thetaC.setObjectName("lineEdit_thetaC")
        self.gridLayout.addWidget(self.lineEdit_thetaC, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.lineEdit_L = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_L.setObjectName("lineEdit_L")
        self.gridLayout.addWidget(self.lineEdit_L, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.lineEdit_I = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_I.setObjectName("lineEdit_I")
        self.gridLayout.addWidget(self.lineEdit_I, 5, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setGeometry(QtCore.QRect(990, 50, 600, 600))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 40, 598, 598))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_IMG = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_IMG.setObjectName("label_IMG")
        self.gridLayout_4.addWidget(self.label_IMG, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 670, 300, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_iterationnForOnce = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_iterationnForOnce.setEnabled(True)
        self.pushButton_iterationnForOnce.setObjectName("pushButton_iterationnForOnce")
        self.gridLayout_2.addWidget(self.pushButton_iterationnForOnce, 0, 0, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout_2.addWidget(self.pushButton_cancel, 3, 1, 1, 1)
        self.pushButton_iteration = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_iteration.setEnabled(False)
        self.pushButton_iteration.setObjectName("pushButton_iteration")
        self.gridLayout_2.addWidget(self.pushButton_iteration, 0, 1, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_save.setEnabled(False)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout_2.addWidget(self.pushButton_save, 1, 0, 1, 1)
        self.pushButton_changeParaments = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_changeParaments.setObjectName("pushButton_changeParaments")
        self.gridLayout_2.addWidget(self.pushButton_changeParaments, 3, 0, 1, 1)
        self.pushButton_changeColor = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_changeColor.setEnabled(False)
        self.pushButton_changeColor.setObjectName("pushButton_changeColor")
        self.gridLayout_2.addWidget(self.pushButton_changeColor, 1, 1, 1, 1)
        self.groupBox_color = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_color.setEnabled(False)
        self.groupBox_color.setGeometry(QtCore.QRect(990, 670, 601, 111))
        self.groupBox_color.setObjectName("groupBox_color")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_4.setGeometry(QtCore.QRect(330, 670, 601, 261))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_remove = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.gridLayout_3.addWidget(self.pushButton_remove, 1, 2, 1, 1)
        self.pushButton_display = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_display.setObjectName("pushButton_display")
        self.gridLayout_3.addWidget(self.pushButton_display, 2, 2, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout_3.addWidget(self.pushButton_add, 0, 2, 1, 1)
        self.listWidget_IMG = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_IMG.setObjectName("listWidget_IMG")
        self.gridLayout_3.addWidget(self.listWidget_IMG, 0, 0, 3, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_5.setGeometry(QtCore.QRect(990, 810, 601, 121))
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_progress = QtWidgets.QLabel(self.groupBox_5)
        self.label_progress.setAlignment(QtCore.Qt.AlignCenter)
        self.label_progress.setWordWrap(False)
        self.label_progress.setObjectName("label_progress")
        self.verticalLayout.addWidget(self.label_progress)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(330, 50, 600, 600))
        self.tabWidget.setObjectName("tabWidget")

        # ISODATA.setCentralWidget(self.centralWidget)

        self.retranslateUi(ISODATA)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ISODATA)

    def retranslateUi(self, ISODATA):
        _translate = QtCore.QCoreApplication.translate
        ISODATA.setWindowTitle(_translate("ISODATA", "ISODATA 图像分类"))
        self.groupBox.setTitle(_translate("ISODATA", "参数设置"))
        self.label.setText(_translate("ISODATA", "聚类中心数 "))
        self.label_2.setText(_translate("ISODATA", "最少样本数 "))
        self.label_3.setText(_translate("ISODATA", "组内标准差阈值"))
        self.label_4.setText(_translate("ISODATA", "归并系数"))
        self.label_5.setText(_translate("ISODATA", "最多归并类别"))
        self.label_6.setText(_translate("ISODATA", "最大迭代次数"))
        self.label_IMG.setText(_translate("ISODATA", "                              运算结果图像"))
        self.groupBox_2.setTitle(_translate("ISODATA", "操作选项"))
        self.pushButton_iterationnForOnce.setText(_translate("ISODATA", "默认参数"))
        self.pushButton_cancel.setText(_translate("ISODATA", "还原"))
        self.pushButton_iteration.setText(_translate("ISODATA", "迭代至结束"))
        self.pushButton_save.setText(_translate("ISODATA", "保存图片"))
        self.pushButton_changeParaments.setText(_translate("ISODATA", "修改参数"))
        self.pushButton_changeColor.setText(_translate("ISODATA", "更改配色"))
        self.groupBox_color.setTitle(_translate("ISODATA", "颜色分布"))
        self.groupBox_4.setTitle(_translate("ISODATA", "图层数据"))
        self.pushButton_remove.setText(_translate("ISODATA", "删除图层"))
        self.pushButton_display.setText(_translate("ISODATA", "清空图层"))
        self.pushButton_add.setText(_translate("ISODATA", "添加图层"))
        self.groupBox_5.setTitle(_translate("ISODATA", "运行进度"))
        self.label_progress.setText(_translate("ISODATA", "准备就绪"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ISODATA = QtWidgets.QMainWindow()
    ui = Ui_ISODATA()
    ui.setupUi(ISODATA)
    ISODATA.show()
    sys.exit(app.exec_())



