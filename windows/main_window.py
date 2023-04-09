import PyQt5
from PyQt5.QtWidgets import QMainWindow

from widgets.MainWindow import Ui_MainWindow
from .new_note_dialog import NewNoteDialog
from data import db_session
from data.password import Password
from data.notes import Note


class PasswordManager(QMainWindow, Ui_MainWindow):
    def __init__(self, switch_function, user):
        super(PasswordManager, self).__init__()
        self.setupUi(self)
        self.switch_function = switch_function
        self.user = user
        self.show_notes()

        self.quit.clicked.connect(self.close)
        self.addNote.clicked.connect(self.add_note)
        self.generateNewPasswordButton.clicked.connect()

    def add_note(self):
        self.new_note_widget = NewNoteDialog(self.user, self.refresh_table)
        self.new_note_widget.show()

    def show_notes(self):
        self.treeWidget.setColumnCount(3)
        self.treeWidget.clear()
        db_sess = db_session.create_session()
        notes = db_sess.query(Note).filter(Note.creator_id == self.user.id).all()
        index = 1
        for note in notes:
            temp_item = PyQt5.QtWidgets.QTreeWidgetItem(self.treeWidget)
            temp_item.setText(0, str(index))
            temp_item.setText(1, note.name)
            temp_item.setText(2, str(note.datetime)[:-7])
            index += 1

    def show_passwords(self):
        self.treeWidget.setColumnCount(4)
        self.treeWidget.clear()
        db_sess = db_session.create_session()
        passwords = db_sess.query(Password).filter(Password.creator_id == self.user.id).all()
        index = 1
        for password in passwords:
            temp_item = PyQt5.QtWidgets.QTreeWidgetItem(self.treeWidget)
            temp_item.setText(0, str(index))
            temp_item.setText(1, password.name)
            temp_item.setText(2, password.URL)
            temp_item.setText(3, str(password.datetime)[:-7])
            index += 1

    def refresh_table(self, type):
        if type == 0:
            self.show_notes()
        elif type == 1:
            self.show_passwords()

    def generation_password_dialog(self):
        pass
