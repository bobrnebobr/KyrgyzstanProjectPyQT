import PyQt5
from PyQt5.QtWidgets import QDialog
from werkzeug.security import check_password_hash
from data import db_session
import os
import crypto

from widgets.LoginDialog import Ui_Dialog


class LoginDialog(QDialog, Ui_Dialog):
    def __init__(self, switch_function):
        super(LoginDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Логин")
        self.switch_function = switch_function

        self.loginButton.clicked.connect(self.login)

    def check(self):
        if not os.path.exists('Login Data'):
            self.switch_function("RegisterDialog")

    def login(self):
        if not self.passwordEdit.text():
            return self.label.setText("Введите логин")
        if crypto.check_password(self.passwordEdit.text()):
            self.switch_function("PasswordManager", self.passwordEdit.text())

    def enable_or_disable_form(self, need_to_enable: bool):
        self.loginButton.setEnabled(need_to_enable)
        self.registerButton.setEnabled(need_to_enable)
        self.loginEdit.setEnabled(need_to_enable)
        self.passwordEdit.setEnabled(need_to_enable)
