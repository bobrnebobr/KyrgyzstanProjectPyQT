from PyQt5.QtWidgets import QWidget
from widgets.MasterPasswordWidget import Ui_Form


class InputMasterPasswordWidget(QWidget, Ui_Form):
    def __init__(self):
        super(InputMasterPasswordWidget, self).__init__()
        self.setupUi(self)
