#default libraries
from typing import Union, Tuple, Optional, Any

#installed libraries
from PySide6 import QtWidgets, QtGui, QtCore

#local libraries
from ..appearance import ThemeManager, ModeManager

# The purpose of this program is to provide a class for styled 
# text edits using QTextEdit from PySide6 in connection to the 
# PyCt6 library
#
# Author: D. Liam Mc.
# Version: 6.1.0
# Date: October 23, 2025

class CTextEdit(QtWidgets.QWidget):
    def __init__(
            self,
            master: Any,
            width: int = 280,
            height: int = 140,
            text: Optional[str] = None,
            placeholder_text: str = "CTextEdit",
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

        #set text, placeholder text, tooltip, and font parameters
        self._text = text
        self._placeholder_text = placeholder_text
        self._tooltip = tooltip
        self._font_family = font_family
        self._font_size = font_size
        self._font_style = font_style
        
        #set appearance and styling parameters
        self._border_width = (
            ThemeManager.theme["CTextEdit"]["border_width"] 
            if border_width is None else border_width
        )
        self._corner_radius = (
            ThemeManager.theme["CTextEdit"]["corner_radius"] 
            if corner_radius is None else corner_radius
        )
        self._text_color = (
            ThemeManager.theme["CTextEdit"]["text_color"] 
            if text_color is None else text_color
        )
        self._placeholder_text_color = (
            ThemeManager.theme["CTextEdit"]["placeholder_text_color"] 
            if placeholder_text_color is None else placeholder_text_color
        )
        self._background_color = (
            ThemeManager.theme["CTextEdit"]["background_color"] 
            if background_color is None else background_color
        )
        self._border_color = (
            ThemeManager.theme["CTextEdit"]["border_color"] 
            if border_color is None else border_color
        )
        self._disabled_text_color= (
            ThemeManager.theme["CTextEdit"]["disabled_text_color"] 
            if disabled_text_color is None else disabled_text_color
        )
        self._disabled_background_color = (
            ThemeManager.theme["CTextEdit"]["disabled_background_color"] 
            if disabled_background_color is None else disabled_background_color
        )

        self._scroll_bar_color = ThemeManager.theme["CScrollBar"]["background_color"]
        self._scroll_bar_hover_color = ThemeManager.theme["CScrollBar"]["hover_color"]
        self._scroll_bar_pressed_color = ThemeManager.theme["CScrollBar"]["pressed_color"]
        
        #flags
        self._palette_changing = False

        #class variables
        self._layout = QtWidgets.QVBoxLayout()
        self._text_edit = QtWidgets.QTextEdit()

        #set font of text edit
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
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

        #set content margins of layout
        self._layout.setContentsMargins(5,5,5,5)

        #set attributes of text edit
        self._text_edit.setText(self._text)
        self._text_edit.setPlaceholderText(self._placeholder_text)
        self._text_edit.setToolTip(self._tooltip)
        #self._text_edit.setTextMargins(QtCore.QMargins(5, 3, 5, 3))
        self._text_edit.setFont(self._font)
        self._text_edit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self._text_edit.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self._text_edit.textChanged.connect(self.__change_text)

        self._change_theme()

        self._layout.addWidget(self._text_edit)
        self.setLayout(self._layout)

    def text_edit(self):
        return self._text_edit

    def __change_text(self):
        self._text = self._text_edit.toPlainText()
    
    #method to update the theme of the text edit
    def _change_theme(self):

        #get styling of text edit and store it in a tuple with keys for variable
        variables = (
            ("_text_color", self._text_color),
            ("_placeholder_text_color", self._placeholder_text_color),
            ("_background_color", self._background_color), 
            ("_border_color", self._border_color), 
            ("_disabled_text_color", self._disabled_text_color), 
            ("_disabled_background_color", self._disabled_background_color),
            ("_scroll_bar_color", self._scroll_bar_color),
            ("_scroll_bar_hover_color", self._scroll_bar_hover_color),
            ("_scroll_bar_pressed_color", self._scroll_bar_pressed_color)
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

        #set the stylesheet of text edit with new colors
        self._text_edit.setStyleSheet(
                "QTextEdit {"
                    f"background-color: {new_colors['_background_color']};"
                    f"color: {new_colors['_text_color']};"
                    f"border: {self._border_width}px solid {new_colors['_border_color']};"
                    f"border-radius: {self._corner_radius}px;"
                    "padding: 2px;"
                "}"

                "QTextEdit::placeholder {"
                    f"color: {new_colors['_placeholder_text_color']};"
                "}"

                "QTextEdit:disabled {" 
                    f"color: {new_colors['_disabled_text_color']};"
                    f"background-color: {new_colors['_disabled_background_color']};"
                "}"

                "QScrollArea {"
                    f"background-color: {new_colors['_background_color']};"
                "}"

                "QScrollBar:vertical {"
                    "border: none;"
                    f"background-color: {new_colors['_background_color']};"
                    "width: 8px;"
                    "border-radius: 4px;"
                "}"

                "QScrollBar::handle:vertical {"	
                    f"background-color: {new_colors['_scroll_bar_color']};"
                    "min-height: 30px;"
                    "border-radius: 4px;"

                "}"

                "QScrollBar::handle:vertical:hover{"
                    f"background-color: {new_colors['_scroll_bar_hover_color']};"
                "}"

                "QScrollBar::handle:vertical:pressed {"	
                    f"background-color: {new_colors['_scroll_bar_pressed_color']};"
                "}"

                "QScrollBar::sub-line:vertical:hover {"	
                    f"background-color: {new_colors['_scroll_bar_hover_color']};"
                "}"

                "QScrollBar::sub-line:vertical:pressed {"	
                    f"background-color: {new_colors['_scroll_bar_pressed_color']};"
                "}"

                "QScrollBar::add-line:vertical {"
                    "border: none;"
                    "background-color: transparent;"
                    "height: 15px;"
                    "border-bottom-left-radius: 4px;"
                    "border-bottom-right-radius: 4px;"
                    "subcontrol-position: bottom;"
                    "subcontrol-origin: margin;"
                    "border-radius: 4px;"
                "}"

                "QScrollBar::add-line:vertical:hover {"	
                    f"background-color: {new_colors['_scroll_bar_hover_color']};"
                "}"

                "QScrollBar::add-line:vertical:pressed {"	
                    f"background-color: {new_colors['_scroll_bar_pressed_color']};"
                "}"

                "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {"
                    f"background-color: {new_colors['_background_color']};"
                "}"

                "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {"
                    f"background-color: {new_colors['_background_color']};"
                "}"
            )

    #method to change theme when system theme changes 
    def changeEvent(self, event): 

        #if the system text edit palette changes and palette is not already changing continue
        if (
            event.type() == QtCore.QEvent.Type.PaletteChange and not self._palette_changing
        ): 
            self._palette_changing = True       #update palette changing flag to true   
            self._change_theme()               #update text edit theme
            self._palette_changing = False      #update palette changing flag to false

        super().changeEvent(event)
