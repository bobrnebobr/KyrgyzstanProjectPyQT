import PyQt5
from PyQt5.QtGui import QMovie
import re
from PyQt5.QtWidgets import QDialog
from data import db_session
from werkzeug.security import check_password_hash, generate_password_hash
import crypto

from widgets.RegisterDialog import Ui_Dialog


DIGITS = '1234567890'
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщ'
EMAIL_CHECK = regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))"
                                 r"+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")


class RegisterDialog(QDialog, Ui_Dialog):
    def __init__(self, switch_function):
        super(RegisterDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Регистрация")
        self.switch_function = switch_function

        self.registerButton.clicked.connect(self.register)

    def register(self):
        self.enable_or_disable_form(False)
        if not self.passwordEdit.text():
            self.enable_or_disable_form(True)
            return self.label.setText("Укажите мастер-пароль")
        if self.passwordEdit.text() != self.repeatPasswordEdit.text():
            self.enable_or_disable_form(True)
            return self.label.setText("Пароли не совпадают")
        if self.passwordEdit.text() != self.repeatPasswordEdit.text():
            self.enable_or_disable_form(True)
            return self.label.setText("Пароли не совпадают")
        if not re.findall(r'[0-9]', self.passwordEdit.text()):
            self.enable_or_disable_form(True)
            return self.label.setText("Пароль должен содержать хотя бы одну цифру")
        if len(self.passwordEdit.text()) < 10:
            self.enable_or_disable_form(True)
            return self.label.setText("Пароль должен содержать хотя бы 10 символов")
        if not re.findall(r'\W', self.passwordEdit.text()) and not self.passwordEdit.text().count("_"):
            self.enable_or_disable_form(True)
            return self.label.setText("Пароль должен содержать хотя бы один символ")
        crypto.create_login_data(self.passwordEdit.text())
        self.switch_function("LoginDialog")

    def enable_or_disable_form(self, need_to_enable: bool):
        self.registerButton.setEnabled(need_to_enable)
        self.passwordEdit.setEnabled(need_to_enable)
        self.repeatPasswordEdit.setEnabled(need_to_enable)
