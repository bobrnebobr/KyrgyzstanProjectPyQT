from PyQt5.QtWidgets import QWidget

from widgets.ForNotesWidget import Ui_Form


class ForNotesWidget(QWidget, Ui_Form):
    def __init__(self, parent):
        super(ForNotesWidget, self).__init__()
        self.setupUi(parent)
