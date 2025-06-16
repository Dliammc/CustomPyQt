from PyCt6 import CMainWindow, CButton, set_appearance_mode, set_color_theme
from PySide6.QtWidgets import QApplication, QVBoxLayout
from PySide6.QtCore import Qt

set_appearance_mode("system")
set_color_theme("blue")

class MainWindow(CMainWindow):
    def __init__(self):
        super().__init__(width=400, height=250, title="CMainWindow", background_color="rgb(30,30,30)")

        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button = CButton(master=self, text="CButton", command=self.command)

        self.main_layout.addWidget(self.button)
        self.setLayout(self.main_layout)

    def command(self):
        print("Button Clicked!")

app = QApplication()
win = MainWindow()
win.show()
app.exec()