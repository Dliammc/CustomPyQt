from platform import system, release
from typing import Union, Tuple, Optional, Any, Callable

from PySide6 import QtWidgets, QtGui, QtCore

from ..appearance import ThemeManager, ModeManager

class CButton(QtWidgets.QFrame):
    def __init__(self,
                 master: QtWidgets.QWidget,
                 text: str = "CButton",
                 image: Optional[str] = None,
                 image_size: Union[int, Tuple[int, int]] = None,
                 tooltip: Optional[str] = None,
                 width: int = 140,
                 height: int = 28,
                 corner_radius: int = 6,
                 border_width: Optional[int] = None,
                 text_color: Union[str, Tuple[str, str]] = None,
                 background_color: Union[str, Tuple[str, str]] = None,
                 border_color: Union[str, Tuple[str, str]] = None,
                 hover_color: Union[str, Tuple[str, str]] = None,
                 pressed_color: Union[str, Tuple[str, str]] = None,
                 command: Union[Callable[[], Any], None] = None):
        super().__init__()

        self.button = QtWidgets.QPushButton()

        self.mainLayout = QtWidgets.QHBoxLayout()

        self._master = master
        self._text = text
        self._image = image
        self._image_size = image_size
        self._tooltip = tooltip
        self._width = width
        self._height = height

        self._corner_radius: int = ThemeManager.theme["CButton"]["corner_radius"] if corner_radius is None else corner_radius
        self._border_width: int = ThemeManager.theme["CButton"]["border_width"] if border_width is None else border_width
        
        self._text_color: Union[str, Tuple[str, str]] = ThemeManager.theme["CButton"]["text_color"] if text_color is None else text_color
        self._background_color: Union[str, Tuple[str, str]] = ThemeManager.theme["CButton"]["background_color"] if background_color is None else background_color
        self._border_color: Union[str, Tuple[str, str]] = ThemeManager.theme["CButton"]["border_color"] if border_color is None else border_color
        self._hover_color: Union[str, Tuple[str, str]] = ThemeManager.theme["CButton"]["hover_color"] if hover_color is None else hover_color
        self._pressed_color: Union[str, Tuple[str, str]] = ThemeManager.theme["CButton"]["pressed_color"] if pressed_color is None else pressed_color

        self._command = command

        self.setFixedSize(self._width + 10, self._height + 10)
        self.mainLayout.setContentsMargins(QtCore.QMargins(5, 5, 5, 5))

        self.button.setFont(QtGui.QFont("Segoe UI Variable", 10))

        self.button.setParent(self._master)
        self.button.setText(self._text)
        self.button.setIcon(QtGui.QIcon(self._image))
        self.button.setToolTip(self._tooltip)
        self.button.clicked.connect(self._command)
        self.button.pressed.connect(self.__shrink_size)
        self.button.released.connect(self.__grow_size)

        self.button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        if self._image_size != None:
            self.button.setIconSize(QtCore.QSize(self._image_size[0], self._image_size[1]))

        self.__change_theme()

        self.mainLayout.addWidget(self.button)
        self.setLayout(self.mainLayout)

    def __shrink_size(self):
        self.mainLayout.setContentsMargins(QtCore.QMargins(6, 6, 6, 6))

        self.button.setFont(QtGui.QFont("Segoe UI Variable", 9))

        if self._image_size != None:
            self.button.setIconSize(QtCore.QSize(self._image_size[0] - 1, self._image_size[1] - 1))
        

    def __grow_size(self):
        self.mainLayout.setContentsMargins(QtCore.QMargins(5, 5, 5, 5))

        self.button.setFont(QtGui.QFont("Segoe UI Variable", 10))

        if self._image_size != None:
            self.button.setIconSize(QtCore.QSize(self._image_size[0], self._image_size[1]))

    def __change_theme(self):
        variables = [self._text_color, self._background_color, self._border_color, self._hover_color, self._pressed_color]
        for i in range(len(variables)):
            if isinstance(variables[i], list):
                if ModeManager.mode == "dark":
                    variables[i] = variables[i][1]
                    print(self._background_color)
                elif ModeManager.mode == "light":
                    variables[i] = variables[i][0]
                    print(self._background_color)
                else:
                    if QtGui.QGuiApplication.styleHints().colorScheme() == QtCore.Qt.ColorScheme.Dark:
                        variables[i] = variables[i][1]
                        print(self._background_color)
                    else:
                        variables[i] = variables[i][0]
                        print(self._background_color)

        self.setStyleSheet(
                "QPushButton {"
                f"background-color: {self._background_color};"
                f"color: {self._text_color};"
                f"border: {self._border_width}px solid {self._border_color};"
                f"border-radius: {self._corner_radius}px;"
                "}"

                "QPushButton:hover {"
                f"background-color: {self._hover_color}"
                "}"

                "QPushButton:pressed {"
                f"background-color {self._pressed_color}"
                "}"
            )

    def changeEvent(self, event): 
        if event.type() == QtCore.QEvent.Type.ThemeChange: 
            self.__change_theme()


        

        