from PyQt5.QtWidgets import QWidget

from widgets.ForPasswordsWidget import Ui_Form


class ForPasswordsWidget(QWidget, Ui_Form):
    def __init__(self):
        super(ForPasswordsWidget, self).__init__()
        self.setupUi(self)
