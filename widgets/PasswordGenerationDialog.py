# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/password_generation.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(324, 187)
        Dialog.setStyleSheet("background-color:rgb(43,49,55)")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color:rgb(255,255,255);background-color:rgb(36,41,45);border-width:2;border-radius:5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.copyButton = QtWidgets.QPushButton(Dialog)
        self.copyButton.setMinimumSize(QtCore.QSize(32, 32))
        self.copyButton.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.copyButton.setFont(font)
        self.copyButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.copyButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI\\../images/CopyIcon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copyButton.setIcon(icon)
        self.copyButton.setIconSize(QtCore.QSize(16, 16))
        self.copyButton.setObjectName("copyButton")
        self.horizontalLayout.addWidget(self.copyButton)
        self.repeatButton = QtWidgets.QPushButton(Dialog)
        self.repeatButton.setMinimumSize(QtCore.QSize(32, 32))
        self.repeatButton.setMaximumSize(QtCore.QSize(32, 32))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.repeatButton.setFont(font)
        self.repeatButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.repeatButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI\\../images/RefreshICon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.repeatButton.setIcon(icon1)
        self.repeatButton.setObjectName("repeatButton")
        self.horizontalLayout.addWidget(self.repeatButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255,255,255)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(47,187,79);\n"
"background-color:rgb(47,187,79);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.okButton.setObjectName("okButton")
        self.horizontalLayout_2.addWidget(self.okButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.countSymbolsLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.countSymbolsLabel.setFont(font)
        self.countSymbolsLabel.setStyleSheet("color:rgb(255,255,255)")
        self.countSymbolsLabel.setObjectName("countSymbolsLabel")
        self.horizontalLayout_3.addWidget(self.countSymbolsLabel)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("border-width:2;border-radius:5px;color:rgb(255,255,255);background-color:rgb(36,41,45)")
        self.spinBox.setMinimum(8)
        self.spinBox.setMaximum(100)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Генерация паролей"))
        self.okButton.setText(_translate("Dialog", "Ок"))
        self.countSymbolsLabel.setText(_translate("Dialog", "Кол-во символов"))
