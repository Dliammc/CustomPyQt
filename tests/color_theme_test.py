from PyCt6 import set_color_theme, get_color_theme, CMainWindow, CButton
from PySide6.QtWidgets import QVBoxLayout, QApplication

color = input("What color theme do you want? (use default colors or import .json file)\n")

set_color_theme(color)

print(f"Expected {color} and got {get_color_theme()}")

class MainWindow(CMainWindow):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()

        self.button = CButton(self, command=lambda:print(f"Current Color Theme: {get_color_theme()}"))

        self.main_layout.addWidget(self.button)

        self.setLayout(self.main_layout)


app = QApplication()
win = MainWindow()
win.show()
app.exec()
