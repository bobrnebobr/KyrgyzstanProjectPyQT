import PyQt5
from PyQt5.QtWidgets import QDialog

from widgets.NewNoteDialog import Ui_Dialog
from .for_notes_widget import ForNotesWidget
from .for_passwords_widget import ForPasswordsWidget
from data import db_session
from data.notes import Note
from data.users import User


class NewNoteDialog(QDialog, Ui_Dialog):
    def __init__(self, user):
        super(NewNoteDialog, self).__init__()
        self.setupUi(self)
        self.setFixedSize(420, 360)
        self.type = "note"

        self.current_widget = ForNotesWidget(self.formWidget)

        self.cancelButton.clicked.connect(self.close)

    def change_type(self, choice):
        pass

    def submit(self):
        pass
