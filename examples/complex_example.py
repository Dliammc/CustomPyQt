from PyCt6 import (
    CMainWindow,
    CButton, 
    CComboBox, 
    CFrame, 
    CLabel, 
    CLineEdit, 
    CSlider, 
    CTextEdit, 
    set_appearance_mode, 
    set_color_theme)

from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QSizePolicy, QSpacerItem
from PySide6.QtCore import Qt

from sys import argv

class MainWindow(CMainWindow):
    def __init__(self):
        super().__init__(width=1100, height=580)

        self.setMaximumSize(1100, 580)

        self.main_layout = QHBoxLayout()


        self.left_frame = CFrame(self, corner_radius=0, width=200, height=580)

        self.label1 = CLabel(self, text="CustomPyQt", font_size=20)
        self.button1 = CButton(self)
        self.button2 = CButton(self)

        self.button3 = CButton(self, text="Disabled CButton")
        self.button3.setDisabled(True)

        self.spacer_item1 = QSpacerItem(20, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

        self.label2 = CLabel(self, text="CCombobox 1", font_size=15)
        self.combo_box1 = CComboBox(self, values=["Option 1", "Option 2", "Option 3"])

        self.label3 = CLabel(self, text="CCombobox 2", font_size=15)
        self.combo_box2 = CComboBox(self, values=["Red", "Green", "Blue", "Alpha"])

        #self.center_frame = CFrame(self, corner_radius=0, width=600, height=580)

        #self.text_box = CTextEdit(self, width=600, height=300)

        #self.center_frame.addWidget()

        self.left_frame.addWidget(self.label1)
        self.left_frame.addWidget(self.button1)
        self.left_frame.addWidget(self.button2)
        self.left_frame.addWidget(self.button3)
        self.left_frame.addItem(self.spacer_item1)
        self.left_frame.addWidget(self.label2)
        self.left_frame.addWidget(self.combo_box1)
        self.left_frame.addWidget(self.label3)
        self.left_frame.addWidget(self.combo_box2)

        self.main_layout.addWidget(self.left_frame)

        self.setLayout(self.main_layout)


app = QApplication(argv)
win = MainWindow()
win.show()
app.exec()



