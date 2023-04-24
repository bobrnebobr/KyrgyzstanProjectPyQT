import PyQt5
from PyQt5.QtWidgets import QDialog

from widgets.NewNoteDialog import Ui_Dialog
from .for_notes_widget import ForNotesWidget
from .for_passwords_widget import ForPasswordsWidget
import datetime
from data import db_session
from data.notes import Note
from data.password import Password
import crypto


class NewNoteDialog(QDialog, Ui_Dialog):
    def __init__(self, password, function_when_access):
        super(NewNoteDialog, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Новая запись")
        self.setFixedSize(420, 375)
        self.type = 0
        self.function_when_access = function_when_access
        self.password = password

        self.current_widget = ForNotesWidget(self.formWidget)

        self.cancelButton.clicked.connect(self.close)
        self.acceptButton.clicked.connect(self.submit)
        self.comboBox.activated.connect(self.change_type)

    def change_type(self, choice):
        if choice == self.type:
            return
        if choice == 0:
            self.switch_to_note()
        if choice == 1:
            self.switch_to_password()
        self.type = choice

    def submit(self):
        if self.type == 0:
            self.add_note()
        elif self.type == 1:
            self.add_password()

    def add_note(self):
        if not self.formWidget.children()[-1].toPlainText() or not self.formWidget.children()[1].text():
            return self.errorInfoLabel.setText("Укажите, пожалуйста, все поля")
        db_sess = db_session.create_session()
        if db_sess.query(Note).filter(Note.name == self.formWidget.children()[1].text()).all():
            return self.errorInfoLabel.setText("Название должно быть уникальным")
        encrypted_message = crypto.encode_message(self.formWidget.children()[-1].toPlainText(), self.password)
        new_note = Note(name=self.formWidget.children()[1].text(),
                        salt=encrypted_message[0],
                        cipher_text=encrypted_message[1],
                        nonce=encrypted_message[2],
                        auth_tag=encrypted_message[3],
                        to_ask_master_password=self.checkBox.isChecked())
        db_sess.add(new_note)
        db_sess.commit()
        self.function_when_access(self.type)
        self.close()

    def add_password(self):
        if not self.formWidget.children()[1].text() or not self.formWidget.children()[5].text():
            return self.errorInfoLabel.setText("Пожалуйста, укажите название записи и пароль")
        db_sess = db_session.create_session()
        if db_sess.query(Password).filter(Password.name == self.formWidget.children()[1].text()).all():
            return self.errorInfoLabel.setText("Название должно быть уникальным")
        encrypted_password = crypto.encode_message(self.formWidget.children()[5].text(), self.password)
        encrypted_username = crypto.encode_message(self.formWidget.children()[3].text(), self.password)
        encrypted_description = crypto.encode_message(self.formWidget.children()[9].toPlainText(), self.password)
        password = Password(name=self.formWidget.children()[1].text(),
                            username_salt=encrypted_username[0],
                            username_cipher_text=encrypted_username[1],
                            username_nonce=encrypted_username[2],
                            username_auth_tag=encrypted_username[3],
                            password_salt=encrypted_password[0],
                            password_cipher_text=encrypted_password[1],
                            password_nonce=encrypted_password[2],
                            password_auth_tag=encrypted_password[3],
                            description_salt=encrypted_description[0],
                            description_cipher_text=encrypted_description[1],
                            description_nonce=encrypted_description[2],
                            description_auth_tag=encrypted_description[3],
                            URL=self.formWidget.children()[7].text(),
                            to_ask_master_password=self.checkBox.isChecked())
        db_sess.add(password)
        db_sess.commit()
        # self.function_when_access(self.type)
        self.close()


    def switch_to_nte(self):
        self.change_form_widget(self)
        self.setFixedSize(420, 375)
        self.current_widget = ForNotesWidget(self.formWidget)

    def switch_to_password(self):
        try:
            self.change_form_widget(self)
            self.setFixedSize(488, 440)
            self.current_widget = ForPasswordsWidget(self.formWidget)
        except Exception as exc:
            print(exc)
