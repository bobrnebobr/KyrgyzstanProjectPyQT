import PyQt5
from PyQt5.QtGui import QMovie
import re
from PyQt5.QtWidgets import QDialog
from data import db_session
from data.users import User
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

from widgets.RegisterDialog import Ui_Dialog


DIGITS = '1234567890'
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщ'
EMAIL_CHECK = regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))"
                                 r"+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")


class RegisterDialog(QDialog, Ui_Dialog):
    def __init__(self, switch_function):
        super(RegisterDialog, self).__init__()
        self.setupUi(self)
        self.switch_function = switch_function

        self.registerButton.clicked.connect(self.register)
        self.loginButton.clicked.connect(lambda: switch_function("LoginDialog"))

    def register(self):
        self.enable_or_disable_form(False)
        if not self.loginEdit.text() or not self.emailEdit.text() or not self.passwordEdit.text() or not\
                self.repeatPasswordEdit.text():
            self.enable_or_disable_form(True)
            return self.label.setText("Необходимо указать все поля")
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
            return self.label.setText("Пароль должен содержать хотя бы одну не цифру и не букву")
        if not re.fullmatch(EMAIL_CHECK, self.emailEdit.text()):
            self.enable_or_disable_form(True)
            return self.label.setText("Укажите правильный email")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.login == self.loginEdit.text()).all() or\
                db_sess.query(User).filter(User.email == self.emailEdit.text()).all():
            self.enable_or_disable_form(True)
            return self.label.setText("Логин и почта должны быть уникальными")

        register_user = User(login=self.loginEdit.text(),
                             email=self.emailEdit.text(),
                             hashed_password=generate_password_hash(self.passwordEdit.text()),
                             created_date=datetime.datetime.now())

        db_sess.add(register_user)
        db_sess.commit()

        self.switch_function("LoginManager")

    def enable_or_disable_form(self, need_to_enable: bool):
        self.registerButton.setEnabled(need_to_enable)
        self.loginButton.setEnabled(need_to_enable)
        self.passwordEdit.setEnabled(need_to_enable)
        self.repeatPasswordEdit.setEnabled(need_to_enable)
        self.emailEdit.setEnabled(need_to_enable)
        self.loginEdit.setEnabled(need_to_enable)
