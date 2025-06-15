#default libraries
from typing import Union, Tuple, Optional, Any

#installed libraries
from PySide6 import QtWidgets, QtGui, QtCore

#local libraries
from ..appearance import ThemeManager, ModeManager

# The purpose of this program is to provide a class for styled 
# line edits using QLineEdit from PySide6 in connection to the 
# PyCt library
#
# Author: D. Liam Mc.
# Version: 0.0.3
# Date: June 15, 2025

class CLineEdit(QtWidgets.QWidget):
    def __init__(
            self,
            master: Any,
            width: int = 140,
            height: int = 28,
            text: Optional[str] = None,
            placeholder_text: str = "CLineEdit",
            tooltip: Optional[str] = None,
            font_family: str = "Calibri",
            font_size: int = 12,
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

        match self._font_style:
            case "bold":
                self._font.setBold(True)
            case "underline":
                self._font.setUnderline(True)
            case "italic":
                self._font.setItalic(True)
            case "strikeout":
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

    @property
    def master(self):
        return self._master
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @property
    def text(self):
        return self._text
    
    @property
    def placeholder_text(self):
        return self._placeholder_text
    
    @property
    def tooltip(self):
        return self._tooltip
    
    @property
    def font_family(self):
        return self._font_family
    
    @property
    def font_size(self):
        return self._font_size
    
    @property
    def font_style(self):
        return self._font_style
    
    @property
    def border_width(self):
        return self._border_width
    
    @property
    def corner_radius(self):
        return self._corner_radius
    
    @property
    def text_color(self):
        return self._text_color
    
    @property
    def placeholder_text_color(self):
        return self._placeholder_text_color
    
    @property
    def background_color(self):
        return self._background_color
    
    @property
    def border_color(self):
        return self._border_color
    
    @property
    def disabled_text_color(self):
        return self._disabled_text_color
    
    @property
    def disabled_background_color(self):
        return self._disabled_background_color
    
    @master.setter
    def master(self, master: Any):
        self._master = master

        self.setParent(self._master)

    @width.setter
    def width(self, width: int = 140):
        self._width = width

        self.setMinimumSize(self._width + 10, self._height + 10)
        self.resize(self._width + 10, self._height + 10)

    @height.setter
    def height(self, height: int = 28):
        self._height = height

        self.setMinimumSize(self._width + 10, self._height + 10)
        self.resize(self._width + 10, self._height + 10)

    @height.setter
    @width.setter
    def size(self, width: int = 140, height: int = 28):
        self._width = width
        self._height = height

        self.setMinimumSize(self._width + 10, self._height + 10)
        self.resize(self._width + 10, self._height + 10)

    @text.setter
    def text(self, text: str = "CLineEdit"):
        self._text = text

        self._line_edit.setText(self._text)

    @placeholder_text.setter
    def placeholder_text(self, placeholder_text: Optional[str] = None):
        self._placeholder_text = placeholder_text

        self._line_edit.setPlaceholderText(self._placeholder_text)


    @tooltip.setter
    def tooltip(self, tooltip: Optional[str] = None):
        self._tooltip = tooltip

        self._line_edit.setToolTip(self._tooltip)

    @font_family.setter
    def font_family(self, font_family: str = "Calibri"):
        self._font_family = font_family

        self._font = QtGui.QFont(self._font_family, self._font_size)

        self.setFont(self._font)

    @font_size.setter
    def font_size(self, font_size: int = 10):
        self._font_size = font_size

        self._font = QtGui.QFont(self._font_family, self._font_size)

        self.setFont(self._font)

    @font_style.setter
    def font_style(self, font_style: Optional[str] = None):
        self._font_style = font_style

        match self._font_style:
            case "bold":
                self._font.setBold(True)
            case "underline":
                self._font.setUnderline(True)
            case "italic":
                self._font.setItalic(True)
            case "strikeout":
                self._font.setStrikeOut(True)

    @border_width.setter
    def border_width(self, border_width: Optional[int] = None):
        self._border_width = (
            ThemeManager.theme["CLineEdit"]["border_width"] 
            if border_width is None else border_width
        )

        self._change_theme()

    @corner_radius.setter
    def corner_radius(self, corner_radius: Optional[int] = None):
        self._corner_radius = (
            ThemeManager.theme["CLineEdit"]["corner_radius"] 
            if corner_radius is None else corner_radius
        )
        
        self._change_theme()

    @text_color.setter
    def text_color(
        self, text_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._text_color = (
            ThemeManager.theme["CLineEdit"]["text_color"] 
            if text_color is None else text_color
        )
        
        self._change_theme()

    @placeholder_text_color.setter
    def placeholder_text_color(
        self, placeholder_text_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._placeholder_text_color = (
            ThemeManager.theme["CLineEdit"]["placeholder_text_color"] 
            if placeholder_text_color is None else placeholder_text_color
        )

        self._change_theme()

    @background_color.setter
    def background_color(
        self, background_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._background_color = (
            ThemeManager.theme["CLineEdit"]["background_color"] 
            if background_color is None else background_color
        )
        
        self._change_theme()

    @border_color.setter
    def border_color(
        self, border_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._border_color = (
            ThemeManager.theme["CLineEdit"]["border_color"] 
            if border_color is None else border_color
        )
        
        self._change_theme()

    @disabled_text_color.setter
    def disabled_text_color(
        self, disabled_text_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._disabled_text_color= (
            ThemeManager.theme["CLineEdit"]["disabled_text_color"] 
            if disabled_text_color is None else disabled_text_color
        )

        self._change_theme()

    @disabled_background_color.setter
    def disabled_background_color(
        self, disabled_background_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._disabled_background_color = (
            ThemeManager.theme["CLineEdit"]["disabled_background_color"] 
            if disabled_background_color is None else disabled_background_color
        )

        self._change_theme()

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
                f"background-color: {new_colors["_background_color"]};"
                f"color: {new_colors["_text_color"]};"
                f"border: {self._border_width}px solid {new_colors["_border_color"]};"
                f"border-radius: {self._corner_radius}px"
                "}"

                "QLineEdit::placeholder {"
                f"color: {new_colors["_placeholder_text_color"]}"
                "}"

                "QLineEdit:disabled {" 
                f"color: {new_colors["_disabled_text_color"]};"
                f"background-color: {new_colors["_disabled_background_color"]}"
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
