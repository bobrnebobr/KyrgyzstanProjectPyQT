# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:rgb(43,49,55);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.addNote = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.addNote.setFont(font)
        self.addNote.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(47,187,79);\n"
"background-color:rgb(47,187,79);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.addNote.setObjectName("addNote")
        self.horizontalLayout_2.addWidget(self.addNote)
        self.quit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.quit.setFont(font)
        self.quit.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(255,0,0);\n"
"background-color:rgb(255,0,0);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.quit.setObjectName("quit")
        self.horizontalLayout_2.addWidget(self.quit)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.treeWidget.setFont(font)
        self.treeWidget.setStyleSheet("color:rgb(255,255,255);border-width:2;\n"
"border-radius:6px;\n"
"background-color:rgb(36,41,45);\n"
"font-size:12\n"
"")
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        self.treeWidget.headerItem().setFont(3, font)
        self.treeWidget.header().setVisible(False)
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.profileButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.profileButton.setFont(font)
        self.profileButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.profileButton.setObjectName("profileButton")
        self.horizontalLayout.addWidget(self.profileButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.settingsAction = QtWidgets.QAction(MainWindow)
        self.settingsAction.setObjectName("settingsAction")
        self.quitAction = QtWidgets.QAction(MainWindow)
        self.quitAction.setObjectName("quitAction")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addNote.setText(_translate("MainWindow", "Добавить запись"))
        self.quit.setText(_translate("MainWindow", "Выйти"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "id"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "имя"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "описание"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "дата и время создания"))
        self.profileButton.setText(_translate("MainWindow", "Профиль"))
        self.settingsAction.setText(_translate("MainWindow", "Настройки"))
        self.quitAction.setText(_translate("MainWindow", "Выйти"))
