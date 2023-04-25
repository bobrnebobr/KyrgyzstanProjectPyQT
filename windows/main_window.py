import PyQt5
from PyQt5.QtWidgets import QMainWindow

from widgets.MainWindow import Ui_MainWindow
from .new_note_dialog import NewNoteDialog
from data import db_session
from data.password import Password
from data.notes import Note
from .password_generation_dialog import PasswordGenerator
from .note_view_dialog import NoteViewDialog
from .password_view_dialog import PasswordViewDialog
from .master_password_widget import InputMasterPasswordWidget
import crypto


class PasswordManager(QMainWindow, Ui_MainWindow):
    def __init__(self, switch_function, password):
        super(PasswordManager, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Менеджер паролей")
        self.switch_function = switch_function
        self.show_notes()
        self.type = 0
        self.password = password

        self.quit.clicked.connect(self.close_app)
        self.addNote.clicked.connect(self.add_note)
        self.generateNewPasswordButton.clicked.connect(self.generation_password_dialog)
        self.comboBox.activated.connect(self.refresh_table)
        self.treeWidget.itemDoubleClicked.connect(self.show_view_of_object)
        self.deleteDataButton.clicked.connect(self.open_master_password_widget)

    def add_note(self):
        self.new_note_widget = NewNoteDialog(self.password, self.refresh_table)
        self.new_note_widget.show()
        self.refresh_table()

    def show_notes(self):
        self.treeWidget.setColumnCount(2)
        self.treeWidget.clear()
        db_sess = db_session.create_session()
        notes = db_sess.query(Note).all()
        index = 1
        for note in notes:
            temp_item = PyQt5.QtWidgets.QTreeWidgetItem(self.treeWidget)
            temp_item.setText(0, str(index))
            temp_item.setText(1, note.name)
            index += 1

    def show_passwords(self):
        self.treeWidget.setColumnCount(3)
        self.treeWidget.clear()
        db_sess = db_session.create_session()
        passwords = db_sess.query(Password).all()
        index = 1
        for password in passwords:
            temp_item = PyQt5.QtWidgets.QTreeWidgetItem(self.treeWidget)
            temp_item.setText(0, str(index))
            temp_item.setText(1, password.name)
            temp_item.setText(2, password.URL)
            index += 1

    def refresh_table(self, type):
        if type == 0:
            self.show_notes()
        elif type == 1:
            self.show_passwords()
        self.type = type

    def generation_password_dialog(self):
        self.generation_password_dialog = PasswordGenerator()
        self.generation_password_dialog.show()

    def show_view_of_object(self, item: PyQt5.QtWidgets.QTreeWidgetItem, column):
        if self.type == 0:
            self.viewWidget = NoteViewDialog(item.text(1), self.password)
        elif self.type == 1:
            self.viewWidget = PasswordViewDialog(item.text(1), self.password)
        self.refresh_table()

    def open_master_password_widget(self):
        self.temp_widget = InputMasterPasswordWidget()
        self.temp_widget.pushButton_2.clicked.connect(self.temp_widget.close)
        self.temp_widget.pushButton.clicked.connect(self.check_master_password)
        self.temp_widget.show()

    def check_master_password(self):
        if not self.temp_widget.passwordEdit.text():
            return self.temp_widget.label.setText("Введите логин")
        if crypto.check_password(self.temp_widget.passwordEdit.text()):
            self.temp_widget.close()
            self.delete_data()
            self.refresh_table(self.type)
        else:
            return self.temp_widget.label.setText("Неверный пароль")

    def delete_data(self):
        db_sess = db_session.create_session()
        db_sess.query(Password).delete()
        db_sess.query(Note).delete()
        db_sess.commit()

    @staticmethod
    def close_app():
        exit(0)
