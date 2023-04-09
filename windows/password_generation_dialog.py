from PyQt5.QtWidgets import QDialog
from widgets.PasswordGenerationDialog import Ui_Dialog
import utils
import pyperclip


class PasswordGenerator(QDialog, Ui_Dialog):
    def __init__(self):
        super(PasswordGenerator, self).__init__()
        self.setupUi(self)
        self.generate_password()

        self.repeatButton.clicked.connect(self.generate_password)
        self.copyButton.clicked.connect(self.copy_password)
        self.okButton.clicked.connect(self.close)

    def generate_password(self):
        self.lineEdit.setText(utils.generate_password(self.spinBox.value()))

    def copy_password(self):
        pyperclip.copy(self.lineEdit.text())
