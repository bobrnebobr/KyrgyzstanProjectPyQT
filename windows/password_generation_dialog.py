from PyQt5.QtWidgets import QDialog
from widgets.PasswordGenerationDialog import Ui_Dialog
import random
import string


class PasswordGenerator(QDialog, Ui_Dialog):
    def __init__(self):
        super(PasswordGenerator, self).__init__()
        self.setupUi(self)

        self.repeatButton.clicked.connect(self.generate_password)
        self.copyButton.clicked.connect(self.copy_password)
        self.okButton.clicked.connect(self.close)

    def generate_password(self):
        digits = string.digits
        lowercase = string.ascii_lowercase
        punctuation = string.punctuation
        uppercase = string.ascii_uppercase

    def copy_password(self):
        pass
