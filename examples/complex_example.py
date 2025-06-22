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
        super().__init__(width=825, height=435)


        self.main_layout = QHBoxLayout()


        self.left_frame = CFrame(self, width=200, height=435)
        self.left_frame.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)

        self.label1 = CLabel(self.left_frame, text="CustomPyQt", font_size=20)
        self.button1 = CButton(self.left_frame)
        self.button2 = CButton(self.left_frame)

        self.button3 = CButton(self.left_frame, text="Disabled CButton")
        self.button3.setDisabled(True)

        self.spacer_item1 = QSpacerItem(20, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

        self.label2 = CLabel(self, text="CCombobox 1", font_size=15)
        self.combo_box1 = CComboBox(self.left_frame, values=["Option 1", "Option 2", "Option 3"])

        self.label3 = CLabel(self.left_frame, text="CCombobox 2", font_size=15)
        self.combo_box2 = CComboBox(self.left_frame, values=["Red", "Green", "Blue", "Alpha"])

        self.center_frame = CFrame(self, corner_radius=0, width=525, height=435, background_color="none")

        lorum_ipsum = """
                Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien
            vitae pellentesque sem placerat. In id cursus mi pretium tellus duis convallis. 
            Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec 
            metus bibendum egestas. Iaculis massa nisl malesuada lacinia integer nunc 
            posuere. Ut hendrerit semper vel class aptent taciti sociosqu. Ad litora 
            torquent per conubia nostra inceptos himenaeos. Lorem ipsum dolor sit amet consectetur
            adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem placerat. In id
            cursus mi pretium tellus duis convallis.  Tempus leo eu aenean sed diam urna tempor.
            Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl 
            malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti
            sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos. Lorem ipsum dolor
            sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae pellentesque sem
            placerat. In id cursus mi pretium tellus duis convallis. Tempus leo eu aenean sed diam urna
            tempor. Pulvinar vivamus fringilla lacus nec metus bibendum egestas. Iaculis massa nisl 
            malesuada lacinia integer nunc posuere. Ut hendrerit semper vel class aptent taciti 
            sociosqu. Ad litora torquent per conubia nostra inceptos himenaeos.
        """

        self.text_box = CTextEdit(self, width=500, height=150, text=lorum_ipsum)
        self.slider1 = CSlider(self, width=500)

        self.spacer_item2 = QSpacerItem(20, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

        self.line_edit = CLineEdit(self, width=500)

        self.right_frame = CFrame(self, layout_type="horizontal", corner_radius=0, width=100, height=435, background_color="none")

        self.slider2 = CSlider(self, height=400, orientation="vertical")
        self.slider3 = CSlider(self, height=400, orientation="vertical", value=25)



        self.left_frame.addWidget(self.label1)
        self.left_frame.addWidget(self.button1)
        self.left_frame.addWidget(self.button2)
        self.left_frame.addWidget(self.button3)
        self.left_frame.addItem(self.spacer_item1)
        self.left_frame.addWidget(self.label2)
        self.left_frame.addWidget(self.combo_box1)
        self.left_frame.addWidget(self.label3)
        self.left_frame.addWidget(self.combo_box2)

        self.center_frame.addWidget(self.text_box)
        self.center_frame.addWidget(self.slider1)
        self.center_frame.addItem(self.spacer_item2)
        self.center_frame.addWidget(self.line_edit)

        self.right_frame.addWidget(self.slider2)
        self.right_frame.addWidget(self.slider3)


        self.main_layout.addWidget(self.left_frame)
        self.main_layout.addWidget(self.center_frame)
        self.main_layout.addWidget(self.right_frame)

        self.setLayout(self.main_layout)


app = QApplication(argv)
win = MainWindow()
win.show()
app.exec()
