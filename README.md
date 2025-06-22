<h1 align="center">CustomPyQt</h1>

![PyPI Version](https://img.shields.io/pypi/v/PyCt6)
![LICENSE](https://img.shields.io/pypi/l/PyCt6?color=blue)
![Python Version](https://img.shields.io/pypi/pyversions/PyCt6)
![Total Downloads](https://img.shields.io/pepy/dt/PyCt6)
![Monthly Downloads](https://img.shields.io/pypi/dm/PyCt6?label=monthly%20downloads)


CustomPyQt is a python GUI interface library built from the PySide6
library, providing a modern and consistant interface with styled widgets
and dark and light themes; all widget's colors can be styled in 
("light", "dark") format. CustomPyQt can also be used or integrated 
with PySide and PyQt versions as long as PySide6 is installed.

![](documentation_images/complex_example_windows_image.png)

| _`complex_example.py` on Windows 11 with dark mode and "blue" theme_

![](documentation_images/complex_example_ubuntu_image.png)

| _`complex_example.py` on Ubuntu 22.04 with light mode and "blue" theme_


## Requirements
* Python 3.9, 3.10, 3.11, 3.12, or 3.13
* Pyside6 (you can install with the command ```pip install PySide6```)
    
## Installation
```
pip install PyCt6
```
If there is any issues you can try ```python -m pip install PyCt6``` and if that still doesn't work you can also try ```python3.13 -m pip install PyCt6``` using whatever python version you have

## Documentation
The documentation can be found on this Github Wiki page:

[CustomPyQt Documentation and Tutorial](https://github.com/Dliammc/CustomPyQt/wiki)

## Example Program
Here is a simple example program with only one button to test the CustomPyQt library:

```python
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
```

which results in this window on Windows 11

<img src="documentation_images/simple_example_image.png" width="400"/>

You can find more example programs in the [examples folder](https://github.com/Dliammc/CustomPyQt/tree/main/examples) and in the [documentation](https://github.com/Dliammc/CustomPyQt/wiki/CustomPyQt-Documentation-and-Tutorial)

## Contribution

Feel free to donate with PayPal to help support and contribute to this project :) Thanks!

<a href="https://www.paypal.com/paypalme/DanielMcCraw135"><img src="documentation_images/paypal_button_image.png" width=170 alt="Paypal donation button"></a>
