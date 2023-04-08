from PyQt5.QtWidgets import QMainWindow

from widgets.MainWindow import Ui_MainWindow
from .new_note_dialog import NewNoteDialog


class PasswordManager(QMainWindow, Ui_MainWindow):
    def __init__(self, switch_function, user):
        super(PasswordManager, self).__init__()
        self.setupUi(self)
        self.switch_function = switch_function
        self.user = user

        self.quit.clicked.connect(self.close)
        self.addNote.clicked.connect(self.add_note)

    def add_note(self):
        self.new_note_widget = NewNoteDialog(self.user)
        self.new_note_widget.show()
