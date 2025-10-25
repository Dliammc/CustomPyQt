#default libraries
from sys import argv

#installed libraries
from PySide6.QtWidgets import QApplication

# The purpose of this class is to provide
# a quick way to create a application
# instance from QApplication
#
# Author: D. Liam Mc.
# Version: 6.1.0
# Date: October 23, 2025

class CApplication(QApplication):
    def __init__(self, use_argv=True, style=None):

        args = argv if use_argv else []
        
        super().__init__(args)

        # Set the application style
        self.setStyle(style)

