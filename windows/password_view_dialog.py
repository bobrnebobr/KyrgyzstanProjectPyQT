from widgets.PasswordViewDialog import Ui_Dialog
from PyQt5.QtWidgets import QDialog
import pyperclip
from utils import generate_password
from data import db_session
from data.password import Password


class PasswordViewDialog(QDialog, Ui_Dialog):
    def __init__(self, name):
        super(PasswordViewDialog, self).__init__()
        self.setupUi(self)

        self.db_sess = db_session.create_session()
        self.password = self.db_sess.query(Password).filter(Password.name == name).first()

        self.nameEdit.setText(self.password.name)
        self.passwordEdit.setText(self.password.password)
        self.URLEdit.setText(self.password.URL)
        self.usernameEdit.setText(self.password.username)
        self.descriptionEdit.setText(self.password.description)

        self.copyNameEdit.clicked.connect(lambda: pyperclip.copy(self.nameEdit.text()))
        self.copyPasswordButton.clicked.connect(lambda: pyperclip.copy(self.passwordEdit.text()))
        self.copyUsernameButton.clicked.connect(lambda: pyperclip.copy(self.usernameEdit.text()))
        self.copyURLButtton.clicked.connect(lambda: pyperclip.copy(self.URLEdit.text()))
        self.copyDescriptionButton.clicked.connect(lambda: pyperclip.copy(self.descriptionEdit.toPlainText()))

        self.editPasswordButton.clicked.connect(
            lambda: self.passwordEdit.setReadOnly(not self.passwordEdit.isReadOnly()))
        self.editUsernameButton.clicked.connect(
            lambda: self.usernameEdit.setReadOnly(not self.usernameEdit.isReadOnly()))
        self.editURLButton.clicked.connect(lambda: self.URLEdit.setReadOnly(not self.URLEdit.isReadOnly()))
        self.editDescriptionButton.clicked.connect(
            lambda: self.descriptionEdit.setReadOnly(not self.descriptionEdit.isReadOnly()))

        self.regeneratePasswordButton.clicked.connect(lambda: self.passwordEdit.setText(generate_password(15)))

        self.watchPasswordButton.clicked.connect(self.change_echo_mode)

        self.cancelButton.clicked.connect(self.close)
        self.okButton.clicked.connect(self.change_password)

    def change_echo_mode(self):
        if self.passwordEdit.echoMode() == 2:
            self.passwordEdit.setEchoMode(0)
        else:
            self.passwordEdit.setEchoMode(2)

    def change_password(self):
        if self.password.password != self.passwordEdit.text() or self.password.username != self.usernameEdit.text() \
                or self.password.URL != self.URLEdit.text() or\
                self.password.description != self.descriptionEdit.toPlainText():
            self.password.password = self.passwordEdit.text()
            self.password.username = self.usernameEdit.text()
            self.password.URL = self.URLEdit.text()
            self.password.description = self.descriptionEdit.toPlainText()
            self.db_sess.commit()
            self.close()
        return
