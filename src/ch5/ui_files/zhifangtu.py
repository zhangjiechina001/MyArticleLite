# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhifangtu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1172, 746)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_10 = QtWidgets.QWidget(Form)
        self.widget_10.setObjectName("widget_10")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.widget_10)
        self.frame_2.setMinimumSize(QtCore.QSize(351, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(351, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.toolBox = QtWidgets.QToolBox(self.frame_2)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 329, 662))
        self.page.setObjectName("page")
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setGeometry(QtCore.QRect(0, 150, 321, 451))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.widget_5 = QtWidgets.QWidget(self.frame_3)
        self.widget_5.setGeometry(QtCore.QRect(10, 10, 301, 421))
        self.widget_5.setObjectName("widget_5")
        self.layoutWidget = QtWidgets.QWidget(self.widget_5)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 421))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lst_info = QtWidgets.QListWidget(self.layoutWidget)
        self.lst_info.setResizeMode(QtWidgets.QListView.Adjust)
        self.lst_info.setObjectName("lst_info")
        self.verticalLayout.addWidget(self.lst_info)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.tab_recongnizeInfo = QtWidgets.QTableWidget(self.layoutWidget)
        self.tab_recongnizeInfo.setObjectName("tab_recongnizeInfo")
        self.tab_recongnizeInfo.setColumnCount(3)
        self.tab_recongnizeInfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_recongnizeInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_recongnizeInfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_recongnizeInfo.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tab_recongnizeInfo)
        self.layoutWidget1 = QtWidgets.QWidget(self.page)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 50, 321, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rbn_module = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rbn_module.setObjectName("rbn_module")
        self.horizontalLayout_3.addWidget(self.rbn_module)
        self.rbn_svm = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rbn_svm.setObjectName("rbn_svm")
        self.horizontalLayout_3.addWidget(self.rbn_svm)
        self.rbn_cnn = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rbn_cnn.setObjectName("rbn_cnn")
        self.horizontalLayout_3.addWidget(self.rbn_cnn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.layoutWidget2 = QtWidgets.QWidget(self.page)
        self.layoutWidget2.setGeometry(QtCore.QRect(1, 1, 320, 43))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_connectOPC = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_connectOPC.setObjectName("btn_connectOPC")
        self.gridLayout_4.addWidget(self.btn_connectOPC, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.btn_disconnectOPC = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_disconnectOPC.setObjectName("btn_disconnectOPC")
        self.gridLayout_4.addWidget(self.btn_disconnectOPC, 1, 1, 1, 1)
        self.btn_reconginze = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_reconginze.setObjectName("btn_reconginze")
        self.gridLayout_4.addWidget(self.btn_reconginze, 1, 3, 1, 1)
        self.btn_openFile = QtWidgets.QPushButton(self.layoutWidget2)
        self.btn_openFile.setObjectName("btn_openFile")
        self.gridLayout_4.addWidget(self.btn_openFile, 1, 2, 1, 1)
        self.toolBox.addItem(self.page, "")
        self.gridLayout_3.addWidget(self.toolBox, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.v_Layout_dis = QtWidgets.QVBoxLayout()
        self.v_Layout_dis.setObjectName("v_Layout_dis")
        self.gridLayout_2.addLayout(self.v_Layout_dis, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.widget_10, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "????????????"))
        self.label_3.setText(_translate("Form", "????????????"))
        item = self.tab_recongnizeInfo.horizontalHeaderItem(0)
        item.setText(_translate("Form", "????????????"))
        item = self.tab_recongnizeInfo.horizontalHeaderItem(1)
        item.setText(_translate("Form", "????????????"))
        item = self.tab_recongnizeInfo.horizontalHeaderItem(2)
        item.setText(_translate("Form", "????????????"))
        self.label_7.setText(_translate("Form", "????????????"))
        self.rbn_module.setText(_translate("Form", "????????????"))
        self.rbn_svm.setText(_translate("Form", "SVM"))
        self.rbn_cnn.setText(_translate("Form", "CNN"))
        self.btn_connectOPC.setText(_translate("Form", "??????OPC"))
        self.label.setText(_translate("Form", "????????????"))
        self.btn_disconnectOPC.setText(_translate("Form", "??????OPC"))
        self.btn_reconginze.setText(_translate("Form", "????????????"))
        self.btn_openFile.setText(_translate("Form", "????????????"))

