import sys

import PyQt5
from PyQt5.QtWidgets import QMainWindow, QApplication
import sqlalchemy
from data import db_session
from windows import *
import os


WINDOWS = {"LoginDialog": LoginDialog, "RegisterDialog": RegisterDialog, "PasswordManager": PasswordManager}


class CurrentWindow:
    window = None


def change_window(next, password=None):
    CurrentWindow.window.close()
    if password:
        CurrentWindow.window = WINDOWS[next](change_window, password)
    else:
        CurrentWindow.window = WINDOWS[next](change_window)
    CurrentWindow.window.show()


if __name__ == "__main__":
    if not os.path.exists("User Data"):
        os.mkdir("User Data")
    db_session.global_init()
    app = QApplication(sys.argv)
    app.setStyleSheet("QHeaderView::section { background-color: rgb(36,41,45); border-width:2; border-radius:5px; font-size:12pt; }")
    CurrentWindow.window = LoginDialog(change_window)
    CurrentWindow.window.show()
    CurrentWindow.window.check()
    sys.exit(app.exec())
