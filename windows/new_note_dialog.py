import PyQt5
from PyQt5.QtWidgets import QDialog

from widgets.NewNoteDialog import Ui_Dialog
from .for_notes_widget import ForNotesWidget
from .for_passwords_widget import ForPasswordsWidget
import datetime
from data import db_session
from data.notes import Note
from data.users import User
from data.password import Password


class NewNoteDialog(QDialog, Ui_Dialog):
    def __init__(self, user, function_when_access):
        super(NewNoteDialog, self).__init__()
        self.setupUi(self)
        self.setFixedSize(420, 375)
        self.type = 0
        self.user = user
        self.function_when_access = function_when_access

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
            self.errorInfoLabel.setText("Укажите, пожалуйста, все поля")
        db_sess = db_session.create_session()
        if db_sess.query(Note).filter(Note.name == self.formWidget.children()[1].text()).all():
            return self.errorInfoLabel.setText("Название должно быть уникальнаым")
        new_note = Note(name=self.formWidget.children()[1].text(), text=self.formWidget.children()[-1].toPlainText(),
                        creator_id=self.user.id, datetime=datetime.datetime.now())
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
        new_password = Password(name=self.formWidget.children()[1].text(),
                                username=self.formWidget.children()[3].text(),
                                password=self.formWidget.children()[5].text(),
                                URL=self.formWidget.children()[7].text(),
                                description=self.formWidget.children()[9].toPlainText(),
                                creator_id=self.user.id,
                                datetime=datetime.datetime.now())
        db_sess.add(new_password)
        db_sess.commit()
        self.function_when_access(self.type)
        self.close()

    def switch_to_note(self):
        self.change_form_widget(self)
        self.setFixedSize(420, 375)
        self.current_widget = ForNotesWidget(self.formWidget)

    def switch_to_password(self):
        self.change_form_widget(self)
        self.setFixedSize(488, 440)
        self.current_widget = ForPasswordsWidget(self.formWidget)
