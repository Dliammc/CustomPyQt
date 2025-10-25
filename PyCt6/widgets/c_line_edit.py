#default libraries
from typing import Union, Tuple, Optional, Any

#installed libraries
from PySide6 import QtWidgets, QtGui, QtCore

#local libraries
from ..appearance import ThemeManager, ModeManager

# The purpose of this program is to provide a class for styled 
# line edits using QLineEdit from PySide6 in connection to the 
# PyCt6 library
#
# Author: D. Liam Mc.
# Version: 6.1.0
# Date: October 23, 2025

class CLineEdit(QtWidgets.QWidget):
    def __init__(
            self,
            master: Any,
            width: int = 140,
            height: int = 28,
            text: Optional[str] = None,
            placeholder_text: str = "CLineEdit",
            tooltip: Optional[str] = None,
            font_family: str = "Verdana",
            font_size: int = 10,
            font_style: Optional[str] = None,
            border_width: Optional[int] = None,
            corner_radius: Optional[int] = None,
            text_color: Optional[Union[str, Tuple[str, str]]] = None,
            placeholder_text_color: Optional[Union[str, Tuple[str, str]]] = None,
            border_color: Optional[Union[str, Tuple[str, str]]] = None,
            background_color: Optional[Union[str, Tuple[str, str]]] = None,
            disabled_text_color: Optional[Union[str, Tuple[str, str]]] = None,
            disabled_background_color: Optional[Union[str, Tuple[str, str]]] = None,
    ):
        super().__init__()

        #initialize variables for class

        #default parameters and dimensions
        self._master = master
        self._width = width
        self._height = height

        #set text, placeholder text, tooltip, icon, icon size, and font parameters
        self._text = text
        self._placeholder_text = placeholder_text
        self._tooltip = tooltip
        self._font_family = font_family
        self._font_size = font_size
        self._font_style = font_style
        
        #set appearance and styling parameters
        self._border_width = (
            ThemeManager.theme["CLineEdit"]["border_width"] 
            if border_width is None else border_width
        )
        self._corner_radius = (
            ThemeManager.theme["CLineEdit"]["corner_radius"] 
            if corner_radius is None else corner_radius
        )
        self._text_color = (
            ThemeManager.theme["CLineEdit"]["text_color"] 
            if text_color is None else text_color
        )
        self._placeholder_text_color = (
            ThemeManager.theme["CLineEdit"]["placeholder_text_color"] 
            if placeholder_text_color is None else placeholder_text_color
        )
        self._background_color = (
            ThemeManager.theme["CLineEdit"]["background_color"] 
            if background_color is None else background_color
        )
        self._border_color = (
            ThemeManager.theme["CLineEdit"]["border_color"] 
            if border_color is None else border_color
        )
        self._disabled_text_color= (
            ThemeManager.theme["CLineEdit"]["disabled_text_color"] 
            if disabled_text_color is None else disabled_text_color
        )
        self._disabled_background_color = (
            ThemeManager.theme["CLineEdit"]["disabled_background_color"] 
            if disabled_background_color is None else disabled_background_color
        )
        
        #flags
        self._palette_changing = False

        #class variables
        self._layout = QtWidgets.QVBoxLayout()
        self._line_edit = QtWidgets.QLineEdit()

        #set font of line edit
        self._font = QtGui.QFont(self._font_family, self._font_size)

        if self._font_style == "bold":
            self._font.setBold(True)
        elif self._font_style == "Underline":
            self._font.setUnderline(True)
        elif self._font_style == "italic":
            self._font.setItalic(True)
        elif self._font_style == "strikeout":
            self._font.setStrikeOut(True)

        #set attributes of class
        self.setParent(self._master), 
        self.resize(self._width + 10, self._height + 10)
        self.setMinimumSize(self._width + 10, self._height + 10)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )

        #set content margins of layout
        self._layout.setContentsMargins(5,5,5,5)

        #set attributes of line edit
        self._line_edit.setText(self._text)
        self._line_edit.setPlaceholderText(self._placeholder_text)
        self._line_edit.setToolTip(self._tooltip)
        self._line_edit.setFont(self._font)

        self._line_edit.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
        )

        self._line_edit.textChanged.connect(self.__change_text)

        self._change_theme()

        self._layout.addWidget(self._line_edit)
        self.setLayout(self._layout)

    def line_edit(self):
        return self._line_edit

    def __change_text(self):
        self._text = self._line_edit.text()
    
    #method to update the theme of the line edit
    def _change_theme(self):

        #get styling of line edit and store it in a tuple with keys for variable
        variables = (
            ("_text_color", self._text_color),
            ("_placeholder_text_color", self._placeholder_text_color),
            ("_background_color", self._background_color), 
            ("_border_color", self._border_color), 
            ("_disabled_text_color", self._disabled_text_color), 
            ("_disabled_background_color", self._disabled_background_color)
            )
        
        new_colors = {}     #dictionary to store new colors for styling theme

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

        #set the stylesheet of line edit with new colors
        self._line_edit.setStyleSheet(
                "QLineEdit {"
                "padding-left: 5px;"
                f"background-color: {new_colors['_background_color']};"
                f"color: {new_colors['_text_color']};"
                f"border: {self._border_width}px solid {new_colors['_border_color']};"
                f"border-radius: {self._corner_radius}px;"
                "}"

                "QLineEdit::placeholder {"
                f"color: {new_colors['_placeholder_text_color']};"
                "}"

                "QLineEdit:disabled {" 
                f"color: {new_colors['_disabled_text_color']};"
                f"background-color: {new_colors['_disabled_background_color']};"
                "}"
            )

    #method to change theme when system theme changes 
    def changeEvent(self, event): 

        #if the system line edit palette changes and palette is not already changing continue
        if (
            event.type() == QtCore.QEvent.Type.PaletteChange and not self._palette_changing
        ): 
            self._palette_changing = True       #update palette changing flag to true   
            self._change_theme()               #update line edit theme
            self._palette_changing = False      #update palette changing flag to false

        super().changeEvent(event)
