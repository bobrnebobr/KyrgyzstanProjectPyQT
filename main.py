import sys

import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication
import sqlalchemy
from data import db_session
from windows import *


WINDOWS = {"LoginDialog": LoginDialog, "RegisterDialog": RegisterDialog, "PasswordManager": PasswordManager}


def change_window(next, user=None):
    try:
        global window
        window.close()
        if user:
            window = WINDOWS[next](change_window, user)
        else:
            window = WINDOWS[next](change_window)
        window.show()
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    db_session.global_init()
    app = QApplication(sys.argv)
    app.setStyleSheet("QHeaderView::section { background-color: rgb(36,41,45); border-width:2; border-radius:5px; font-size:12pt; }")
    window = LoginDialog(change_window)
    window.show()
    sys.exit(app.exec())
