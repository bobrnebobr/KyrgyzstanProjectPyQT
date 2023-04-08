import PyQt5
from PyQt5.QtWidgets import QDialog
from werkzeug.security import check_password_hash
from data import db_session
from data.users import User

from widgets.LoginDialog import Ui_Dialog


class LoginDialog(QDialog, Ui_Dialog):
    def __init__(self, switch_function):
        super(LoginDialog, self).__init__()
        self.setupUi(self)
        self.switch_function = switch_function

        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(lambda: switch_function("RegisterDialog"))

    def login(self):
        self.enable_or_disable_form(False)
        if not self.passwordEdit.text() or not self.loginEdit.text():
            self.enable_or_disable_form(True)
            return self.label.setText("Необходимо указать и логин, и пароль")
        db_sess = db_session.create_session()
        current_user = db_sess.query(User).filter(User.login == self.loginEdit.text()
                                                  and check_password_hash(User.hashed_password,
                                                                          self.passwordEdit.text())).first()
        if not current_user:
            return self.label.setText("Неправильный логин или пароль")
        self.switch_function("PasswordManager", current_user)

    def enable_or_disable_form(self, need_to_enable: bool):
        self.loginButton.setEnabled(need_to_enable)
        self.registerButton.setEnabled(need_to_enable)
        self.loginEdit.setEnabled(need_to_enable)
        self.passwordEdit.setEnabled(need_to_enable)
