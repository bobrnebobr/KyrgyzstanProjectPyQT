from widgets.NoteViewDialog import Ui_Dialog
from PyQt5.QtWidgets import QDialog
import pyperclip
from data import db_session
from data.notes import Note


class NoteViewDialog(QDialog, Ui_Dialog):
    def __init__(self, name):
        super(NoteViewDialog, self).__init__()
        self.setupUi(self)

        self.db_sess = db_session.create_session()
        self.note = self.db_sess.query(Note).filter(Note.name == name).first()

        self.nameEdit.setText(self.note.name)
        self.descriptionEdit.setText(self.note.text)
        self.copyNameEdit.clicked.connect(lambda: pyperclip.copy(self.nameEdit.text()))
        self.copyDescriptionButton.clicked.connect(lambda: pyperclip.copy(self.descriptionEdit.toPlainText()))
        self.cancelButton.clicked.connect(self.close)
        self.editButton.clicked.connect(lambda: self.descriptionEdit.setReadOnly(not self.descriptionEdit.isReadOnly()))
        self.okButton.clicked.connect(self.change_note)

    def change_note(self):
        if self.note.text != self.descriptionEdit.toPlainText():
            self.note.text = self.descriptionEdit.toPlainText()
            self.db_sess.commit()
            self.close()
        return
