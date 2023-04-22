from widgets.PasswordViewDialog import Ui_Dialog
from PyQt5.QtWidgets import QDialog
import pyperclip
from utils import generate_password
from data import db_session
from data.password import Password
import crypto
from windows.master_password_widget import InputMasterPasswordWidget


class PasswordViewDialog(QDialog, Ui_Dialog):
    def __init__(self, name, password):
        super(PasswordViewDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Просмотр данных пароля")
        self.master_password = password

        self.db_sess = db_session.create_session()
        self.password = self.db_sess.query(Password).filter(Password.name == name).first()

        if self.password.to_ask_master_password:
            self.temp_widget = InputMasterPasswordWidget()
            self.temp_widget.pushButton_2.clicked.connect(self.close)
            self.temp_widget.pushButton.clicked.connect(self.check_master_password)
            self.temp_widget.show()
        else:
            self.show_widget()

    def show_widget(self):
        self.decrypted_password = crypto.decode_message((self.password.password_salt,
                                                         self.password.password_cipher_text,
                                                         self.password.password_nonce,
                                                         self.password.password_auth_tag),
                                                        self.master_password)
        self.decrypted_username = crypto.decode_message((self.password.username_salt,
                                                         self.password.username_cipher_text,
                                                         self.password.username_nonce,
                                                         self.password.username_auth_tag),
                                                        self.master_password)
        self.decrypted_description = crypto.decode_message((self.password.description_salt,
                                                           self.password.description_cipher_text,
                                                           self.password.description_nonce,
                                                           self.password.description_auth_tag),
                                                          self.master_password)

        self.nameEdit.setText(self.password.name)
        self.passwordEdit.setText(self.decrypted_password)
        self.URLEdit.setText(self.password.URL)
        self.usernameEdit.setText(self.decrypted_username)
        self.descriptionEdit.setText(self.decrypted_description)

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
        self.show()

    def check_master_password(self):
        if not self.temp_widget.passwordEdit.text():
            return self.label.setText("Введите логин")
        if crypto.check_password(self.temp_widget.passwordEdit.text()):
            self.temp_widget.close()
            self.show_widget()
        else:
            return self.label.setText("Неверный пароль")

    def change_echo_mode(self):
        if self.passwordEdit.echoMode() == 2:
            self.passwordEdit.setEchoMode(0)
        else:
            self.passwordEdit.setEchoMode(2)

    def change_password(self):
        if self.decrypted_password != self.passwordEdit.text() or self.decrypted_username != self.usernameEdit.text() \
                or self.password.URL != self.URLEdit.text() or\
                self.decrypted_description != self.descriptionEdit.toPlainText():
            self.password.password_salt, self.password.password_cipher_text,\
                self.password.password_nonce, self.password.password_auth_tag \
                = crypto.encode_message(self.passwordEdit.text(), self.master_password)
            self.password.username_salt, self.password.username_cipher_text,\
                self.password.username_nonce, self.password.username_auth_tag \
                = crypto.encode_message(self.usernameEdit.text(), self.master_password)
            self.password.URL = self.URLEdit.text()
            self.password.description_salt, self.password.description_cipher_text,\
                self.password.description_nonce, self.password.description_auth_tag \
                = crypto.encode_message(self.descriptionEdit.toPlainText(), self.master_password)
            self.db_sess.commit()
            self.close()
        self.close()
