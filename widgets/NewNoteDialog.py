# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/new_note.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(488, 425)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet("background-color:rgb(36,41,45);\n"
"border-radius:5px;\n"
"border-width:2px;")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(255,0,0);\n"
"background-color:rgb(255,0,0);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.acceptButton = QtWidgets.QPushButton(Dialog)
        self.acceptButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(47,187,79);\n"
"background-color:rgb(47,187,79);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.acceptButton.setObjectName("acceptButton")
        self.horizontalLayout.addWidget(self.acceptButton)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255,255,255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.horizontalWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalWidget_2.setStyleSheet("background-color:rgb(43,49,55);\n"
"border-width:2;border-radius:5px;")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.typeLabel = QtWidgets.QLabel(self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeLabel.sizePolicy().hasHeightForWidth())
        self.typeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.typeLabel.setFont(font)
        self.typeLabel.setStyleSheet("color:rgb(255,255,255)")
        self.typeLabel.setObjectName("typeLabel")
        self.horizontalLayout_2.addWidget(self.typeLabel)
        self.comboBox = QtWidgets.QComboBox(self.horizontalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color:rgb(255,255,255);background-color:rgb(36,41,45);font-size:12pt;\n"
"border-radius:5px;\n"
"border-width:2px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.gridLayout.addWidget(self.horizontalWidget_2, 1, 0, 1, 3)
        self.formWidget = QtWidgets.QWidget(Dialog)
        self.formWidget.setStyleSheet("border-width:2;border-radius:5px;background-color:rgb(43,49,55);")
        self.formWidget.setObjectName("formWidget")
        self.gridLayout.addWidget(self.formWidget, 2, 0, 1, 3)
        self.errorInfoLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.errorInfoLabel.setFont(font)
        self.errorInfoLabel.setStyleSheet("color:rgb(255,0,0);")
        self.errorInfoLabel.setText("")
        self.errorInfoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.errorInfoLabel.setObjectName("errorInfoLabel")
        self.gridLayout.addWidget(self.errorInfoLabel, 3, 0, 1, 3)
        self.gridLayout.setRowStretch(2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancelButton.setText(_translate("Dialog", "Отмена"))
        self.acceptButton.setText(_translate("Dialog", "Создать"))
        self.label.setText(_translate("Dialog", "Создать новую запись"))
        self.typeLabel.setText(_translate("Dialog", "Тип"))
        self.comboBox.setItemText(0, _translate("Dialog", "Записка"))
        self.comboBox.setItemText(1, _translate("Dialog", "Логин и пароль"))

    def change_form_widget(self, Dialog):
        self.formWidget = QtWidgets.QWidget(Dialog)
        self.formWidget.setStyleSheet("border-width:2;border-radius:5px;background-color:rgb(43,49,55);")
        self.formWidget.setObjectName("formWidget")
        self.gridLayout.addWidget(self.formWidget, 2, 0, 1, 3)
