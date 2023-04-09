# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/password_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(613, 326)
        Dialog.setStyleSheet("background-color:rgb(43,49,55);")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"background-color:rgb(255,0,0);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.okButton = QtWidgets.QPushButton(Dialog)
        self.okButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(47,187,79);\n"
"background-color:rgb(47,187,79);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 3)
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
        self.label.setStyleSheet("color:rgb(255,255,255)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.URLEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.URLEdit.setFont(font)
        self.URLEdit.setStyleSheet("border-width:2;border-radius:5px;background-color:rgb(36,41,45);color:rgb(255,255,255);")
        self.URLEdit.setReadOnly(True)
        self.URLEdit.setObjectName("URLEdit")
        self.gridLayout.addWidget(self.URLEdit, 3, 1, 1, 1)
        self.nameLabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet("color:rgb(255,255,255)")
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)
        self.usernameLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet("color:rgb(255,255,255)")
        self.usernameLabel.setObjectName("usernameLabel")
        self.gridLayout.addWidget(self.usernameLabel, 1, 0, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.passwordEdit.setFont(font)
        self.passwordEdit.setStyleSheet("border-width:2;border-radius:5px;background-color:rgb(36,41,45);color:rgb(255,255,255);")
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setReadOnly(True)
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout.addWidget(self.passwordEdit, 2, 1, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setStyleSheet("color:rgb(255,255,255)")
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 2, 0, 1, 1)
        self.usernameEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.usernameEdit.setFont(font)
        self.usernameEdit.setStyleSheet("border-width:2;border-radius:5px;background-color:rgb(36,41,45);color:rgb(255,255,255);")
        self.usernameEdit.setReadOnly(True)
        self.usernameEdit.setObjectName("usernameEdit")
        self.gridLayout.addWidget(self.usernameEdit, 1, 1, 1, 1)
        self.descriptionLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setStyleSheet("color:rgb(255,255,255)")
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.gridLayout.addWidget(self.descriptionLabel, 4, 0, 1, 1)
        self.URLLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.URLLabel.setFont(font)
        self.URLLabel.setStyleSheet("color:rgb(255,255,255)")
        self.URLLabel.setObjectName("URLLabel")
        self.gridLayout.addWidget(self.URLLabel, 3, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.nameEdit.setFont(font)
        self.nameEdit.setStyleSheet("border-width:2;border-radius:5px;background-color:rgb(36,41,45);color:rgb(255,255,255);")
        self.nameEdit.setReadOnly(True)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.copyDescriptionButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyDescriptionButton.sizePolicy().hasHeightForWidth())
        self.copyDescriptionButton.setSizePolicy(sizePolicy)
        self.copyDescriptionButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.copyDescriptionButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI\\../images/CopyIcon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.copyDescriptionButton.setIcon(icon)
        self.copyDescriptionButton.setObjectName("copyDescriptionButton")
        self.gridLayout_3.addWidget(self.copyDescriptionButton, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 3, 1, 1)
        self.editDescriptionButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editDescriptionButton.sizePolicy().hasHeightForWidth())
        self.editDescriptionButton.setSizePolicy(sizePolicy)
        self.editDescriptionButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.editDescriptionButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("UI\\../images/EditIcon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editDescriptionButton.setIcon(icon1)
        self.editDescriptionButton.setObjectName("editDescriptionButton")
        self.gridLayout_3.addWidget(self.editDescriptionButton, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 4, 2, 1, 1)
        self.descriptionEdit = QtWidgets.QTextEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.descriptionEdit.setFont(font)
        self.descriptionEdit.setStyleSheet("border-width:2;border-radius:5px;background-color:rgb(36,41,45);color:rgb(255,255,255);")
        self.descriptionEdit.setReadOnly(True)
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.gridLayout.addWidget(self.descriptionEdit, 4, 1, 1, 1)
        self.copyNameEdit = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyNameEdit.sizePolicy().hasHeightForWidth())
        self.copyNameEdit.setSizePolicy(sizePolicy)
        self.copyNameEdit.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.copyNameEdit.setText("")
        self.copyNameEdit.setIcon(icon)
        self.copyNameEdit.setObjectName("copyNameEdit")
        self.gridLayout.addWidget(self.copyNameEdit, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.watchPasswordButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.watchPasswordButton.sizePolicy().hasHeightForWidth())
        self.watchPasswordButton.setSizePolicy(sizePolicy)
        self.watchPasswordButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.watchPasswordButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("UI\\../images/EyeIcon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.watchPasswordButton.setIcon(icon2)
        self.watchPasswordButton.setObjectName("watchPasswordButton")
        self.horizontalLayout_2.addWidget(self.watchPasswordButton)
        self.copyPasswordButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyPasswordButton.sizePolicy().hasHeightForWidth())
        self.copyPasswordButton.setSizePolicy(sizePolicy)
        self.copyPasswordButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.copyPasswordButton.setText("")
        self.copyPasswordButton.setIcon(icon)
        self.copyPasswordButton.setObjectName("copyPasswordButton")
        self.horizontalLayout_2.addWidget(self.copyPasswordButton)
        self.regeneratePasswordButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regeneratePasswordButton.sizePolicy().hasHeightForWidth())
        self.regeneratePasswordButton.setSizePolicy(sizePolicy)
        self.regeneratePasswordButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.regeneratePasswordButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("UI\\../images/RefreshICon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.regeneratePasswordButton.setIcon(icon3)
        self.regeneratePasswordButton.setObjectName("regeneratePasswordButton")
        self.horizontalLayout_2.addWidget(self.regeneratePasswordButton)
        self.editPasswordButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editPasswordButton.sizePolicy().hasHeightForWidth())
        self.editPasswordButton.setSizePolicy(sizePolicy)
        self.editPasswordButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.editPasswordButton.setText("")
        self.editPasswordButton.setIcon(icon1)
        self.editPasswordButton.setObjectName("editPasswordButton")
        self.horizontalLayout_2.addWidget(self.editPasswordButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.copyURLButtton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.copyURLButtton.sizePolicy().hasHeightForWidth())
        self.copyURLButtton.setSizePolicy(sizePolicy)
        self.copyURLButtton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.copyURLButtton.setText("")
        self.copyURLButtton.setIcon(icon)
        self.copyURLButtton.setObjectName("copyURLButtton")
        self.horizontalLayout_3.addWidget(self.copyURLButtton)
        self.editURLButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editURLButton.sizePolicy().hasHeightForWidth())
        self.editURLButton.setSizePolicy(sizePolicy)
        self.editURLButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.editURLButton.setText("")
        self.editURLButton.setIcon(icon1)
        self.editURLButton.setObjectName("editURLButton")
        self.horizontalLayout_3.addWidget(self.editURLButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.copyUsernameButton = QtWidgets.QPushButton(Dialog)
        self.copyUsernameButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.copyUsernameButton.setText("")
        self.copyUsernameButton.setIcon(icon)
        self.copyUsernameButton.setObjectName("copyUsernameButton")
        self.horizontalLayout_7.addWidget(self.copyUsernameButton)
        self.editUsernameButton = QtWidgets.QPushButton(Dialog)
        self.editUsernameButton.setStyleSheet("border-radius:5px;\n"
"border-width:2px;\n"
"padding:6px;\n"
"border-color:rgb(13,116,231);\n"
"background-color:rgb(13,116,231);\n"
"color:rgb(255,255,255);\n"
"font-size:12pt;")
        self.editUsernameButton.setText("")
        self.editUsernameButton.setIcon(icon1)
        self.editUsernameButton.setObjectName("editUsernameButton")
        self.horizontalLayout_7.addWidget(self.editUsernameButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 2, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancelButton.setText(_translate("Dialog", "Отмена"))
        self.okButton.setText(_translate("Dialog", "Ок"))
        self.label.setText(_translate("Dialog", "Пароль"))
        self.nameLabel.setText(_translate("Dialog", "Название"))
        self.usernameLabel.setText(_translate("Dialog", "Имя пользователя"))
        self.passwordLabel.setText(_translate("Dialog", "Пароль"))
        self.descriptionLabel.setText(_translate("Dialog", "Описание"))
        self.URLLabel.setText(_translate("Dialog", "URL"))