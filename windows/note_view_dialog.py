from widgets.NoteViewDialog import Ui_Dialog
from PyQt5.QtWidgets import QDialog
import pyperclip
from data import db_session
from data.notes import Note
from windows.master_password_widget import InputMasterPasswordWidget
import crypto


class NoteViewDialog(QDialog, Ui_Dialog):
    def __init__(self, name, password):
        super(NoteViewDialog, self).__init__()
        self.setupUi(self)
        self.password = password
        self.setWindowTitle("Просмотр заметки")

        self.db_sess = db_session.create_session()
        self.note = self.db_sess.query(Note).filter(Note.name == name).first()

        if self.note.to_ask_master_password:
            self.temp_widget = InputMasterPasswordWidget()
            self.temp_widget.pushButton_2.clicked.connect(self.close_windows)
            self.temp_widget.pushButton.clicked.connect(self.check_master_password)
            self.temp_widget.show()
        else:
            self.show_widget()

    def close_windows(self):
        self.temp_widget.close()
        self.close()

    def check_master_password(self):
        if not self.temp_widget.passwordEdit.text():
            return self.temp_widget.label.setText("Введите логин")
        if crypto.check_password(self.temp_widget.passwordEdit.text()):
            self.temp_widget.close()
            self.show_widget()
        else:
            return self.temp_widget.label.setText("Неверный пароль")

    def show_widget(self):
        self.decrypted_description = crypto.decode_message((self.note.salt, self.note.cipher_text, self.note.nonce,
                                                            self.note.auth_tag), self.password)
        self.nameEdit.setText(self.note.name)
        self.descriptionEdit.setText(self.decrypted_description)
        self.copyNameEdit.clicked.connect(lambda: pyperclip.copy(self.nameEdit.text()))
        self.copyDescriptionButton.clicked.connect(lambda: pyperclip.copy(self.descriptionEdit.toPlainText()))
        self.cancelButton.clicked.connect(self.close)
        self.editButton.clicked.connect(lambda: self.descriptionEdit.setReadOnly(not self.descriptionEdit.isReadOnly()))
        self.okButton.clicked.connect(self.change_note)
        self.show()

    def change_note(self):
        if self.decrypted_description != self.descriptionEdit.toPlainText():
            encrypted_description = crypto.encode_message(self.descriptionEdit.toPlainText(), self.password)
            self.note.salt = encrypted_description[0]
            self.note.cipher_text = encrypted_description[1]
            self.note.nonce = encrypted_description[2]
            self.note.auth_tag = encrypted_description[3]
            self.db_sess.commit()
        self.close()
