#default libraries
from typing import Union, Tuple, Optional, Any

#installed libraries
from PySide6 import QtWidgets, QtGui, QtCore

#local libraries
from ..appearance import ThemeManager, ModeManager

# The purpose of this program is to provide a class for styled 
# labels using QLabel from PySide6 in connection to the 
# PyCt6 library
#
# Author: D. Liam Mc.
# Version: 6.1.0
# Date: November 8, 2025

class CLabel(QtWidgets.QWidget):
    def __init__(
            self,
            master: Any,
            width: int = 70,
            height: int = 28,
            text: str = "CLabel",
            tooltip: Optional[str] = None,
            icon: Optional[Union[str, Tuple[str, str]]] = None,
            icon_size: Tuple[int, int] = None,
            font_family: str = "Verdana",
            font_size: int = 11,
            font_style: Optional[str] = None,
            border_width: Optional[int] = None,
            corner_radius: Optional[int] = None,
            background_color: Optional[Union[str, Tuple[str, str]]] = None,
            text_color: Optional[Union[str, Tuple[str, str]]] = None,
            border_color: Optional[Union[str, Tuple[str, str]]] = None,
            disabled_background_color: Optional[Union[str, Tuple[str, str]]] = None,
            disabled_text_color: Optional[Union[str, Tuple[str, str]]] = None, 
    ):

        super().__init__()

        #initialize variables for class

        #default parameters and dimensions
        self._master = master
        self._width = width
        self._height = height
        
        #set text, icon, tooltip, and font parameters
        self._text = text
        self._icon = icon
        self._tooltip = tooltip
        self._icon_size = icon_size
        self._font_family = font_family
        self._font_size = font_size
        self._font_style = font_style

        #set appearance and styling parameters
        self._border_width = (
            ThemeManager.theme["CLabel"]["border_width"] 
            if border_width is None else border_width
        )
        self._corner_radius = (
            ThemeManager.theme["CLabel"]["corner_radius"] 
            if corner_radius is None else corner_radius
        )
        self._text_color = (
            ThemeManager.theme["CLabel"]["text_color"] 
            if text_color is None else text_color
        )
        self._disabled_text_color = (
            ThemeManager.theme["CLabel"]["disabled_text_color"] 
            if disabled_text_color is None else disabled_text_color
        )

        self._background_color = background_color
        self._border_color = border_color
        self._disabled_background_color = disabled_background_color

        #flags
        self._palette_changing = False

        #class variables
        self._layout = QtWidgets.QVBoxLayout()
        self._label = QtWidgets.QLabel()

        #set font of label
        self._font = QtGui.QFont(self._font_family, self._font_size)

        if self._font_style == "bold":
            self._font.setBold(True)
        elif self._font_style == "Underline":
            self._font.setUnderline(True)
        elif self._font_style == "italic":
            self._font.setItalic(True)
        elif self._font_style == "strikeout":
            self._font.setStrikeOut(True)

        #set content margins of layout
        self._layout.setContentsMargins(5,5,5,5)

        #set attributes of class
        self.setParent(self._master)
        self.setMinimumSize(self._width + 10, self._height + 10)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.resize(self._width + 10, self._height + 10)

        #set attributes of label
        self._label.setText(self._text)
        self._label.setToolTip(self._tooltip)
        self._label.setFont(self._font)
        self._label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self._label.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
        )

        self._layout.addWidget(self._label)
        self.setLayout(self._layout)

    def label(self):
        return self._label

    #method to update the theme of the label
    def _change_theme(self):

        #get styling of label and store it in a tuple with keys for variable
        variables = (
            ("_text_color", self._text_color),
            ("_background_color", self._background_color), 
            ("_border_color", self._border_color),
            ("_disabled_text_color", self._disabled_text_color), 
            ("_disabled_background_color", self._disabled_background_color),
            ("_icon", self._icon)
            )
        
        new_colors = {}     #dictionary to store new colors fot styling theme

        for attribute, color in variables:

            #if specified color is a list or a tuple continue
            if isinstance(color, list) or isinstance(color, tuple):

                #if the mode is dark set the new color with
                #the specified attribute to the dark color
                if ModeManager.mode == "dark":
                    new_colors[attribute] = color[1]

                #if the mode is light do the same but with the light color
                elif ModeManager.mode == "light":
                    new_colors[attribute] = color[0]

                #otherwise check the system theme
                else:
                    #if the system theme is dark, set the new color with the specified
                    #attribute to the dark color
                    if (
                        QtGui.QGuiApplication.styleHints().colorScheme() == QtCore.Qt.ColorScheme.Dark
                    ):
                        new_colors[attribute] = color[1]

                    #otherwise use the light color
                    else:
                        new_colors[attribute] = color[0] 

            #otherwise it is a string and set the 
            #new color to that specified color
            else:
                new_colors[attribute] = color

        #set icon of label and resize label if there is an icon size
        if self._icon != None:
            pixmap = QtGui.QPixmap(new_colors["_icon"])
            self._label.setPixmap(pixmap)

            if self._icon_size != None:
                self._label.resize(self.icon_size[0], self.icon_size[1])

        #set the stylesheet of label with new colors
        self._label.setStyleSheet(
                "QLabel {"
                    f"background-color: {new_colors['_background_color']};"
                    f"color: {new_colors['_text_color']};"
                    f"border: {self._border_width}px solid {new_colors['_border_color']};"
                    f"border-radius: {self._corner_radius}px;"
                "}"

                "QLabel:disabled {" 
                    f"color: {new_colors['_disabled_text_color']};"
                    f"background-color: {new_colors['_disabled_background_color']};"
                "}"
            )
        
    #method to change theme when system theme changes 
    def changeEvent(self, event): 
        
        #if the system label palette changes and palette is not already changing continue
        if (
            event.type() == QtCore.QEvent.Type.PaletteChange and not self._palette_changing
        ): 
            self._palette_changing = True       #update palette changing flag to true   
            self._change_theme()               #update label theme
            self._palette_changing = False      #update palette changing flag to false

        super().changeEvent(event)
