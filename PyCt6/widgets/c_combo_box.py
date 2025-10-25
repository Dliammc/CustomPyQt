#default libraries
from typing import Union, Tuple, Optional, Any, Callable
from os import path
from pathlib import Path

#installed libraries
from PySide6 import QtWidgets, QtGui, QtCore

#local libraries
from ..appearance import ThemeManager, ModeManager

# The purpose of this program is to provide a class for styled 
# comboboxes using QComboBox from PySide6 in connection to the 
# PyCt6 library
#
# Author: D. Liam Mc.
# Version: 6.1.0
# Date: October 23, 2025

class CComboBox(QtWidgets.QWidget):
    def __init__(
            self,
            master: Any,
            width: int = 140,
            height: int = 28,
            values: list = None,
            current_value: str = str(list[0]) if not None else "CComboBox",
            tooltip: Optional[str] = None,
            font_family: str = "Verdana",
            font_size: int = 10,
            font_style: Optional[str] = None,
            border_width: Optional[int] = None,
            menu_border_width: Optional[int] = None,
            item_border_width: Optional[int] = None,
            corner_radius: Optional[int] = None,
            text_color: Optional[Union[str, Tuple[str, str]]] = None,
            background_color: Optional[Union[str, Tuple[str, str]]] = None,
            border_color: Optional[Union[str, Tuple[str, str]]] = None,
            hover_color: Optional[Union[str, Tuple[str, str]]] = None,
            menu_background_color: Optional[Union[str, Tuple[str, str]]] = None,
            menu_border_color: Optional[Union[str, Tuple[str, str]]] = None,
            item_text_color: Optional[Union[str, Tuple[str, str]]] = None,
            item_background_color: Optional[Union[str, Tuple[str, str]]] = None,
            item_border_color: Optional[Union[str, Tuple[str, str]]] = None,
            item_hover_color: Optional[Union[str, Tuple[str, str]]] = None,
            disabled_text_color: Optional[Union[str, Tuple[str, str]]] = None,
            disabled_background_color: Optional[Union[str, Tuple[str, str]]] = None 
    ):
        super().__init__()

        #initialize variables for class

        #default parameters and dimensions
        self._master = master
        self._height = height
        self._width = width

        #set values, default values, tooltip, and font parameters
        self._values = values
        self._current_value = current_value
        self._tooltip = tooltip
        self._font_family = font_family
        self._font_size = font_size
        self._font_style = font_style

        #set appearance and styling parameters
        self._border_width = (
            ThemeManager.theme["CComboBox"]["border_width"] 
            if border_width is None else border_width
        )
        self._menu_border_width = (
            ThemeManager.theme["CComboBox"]["menu_border_width"] 
            if menu_border_width is None else menu_border_width
        )
        self._item_border_width = (
            ThemeManager.theme["CComboBox"]["item_border_width"] 
            if item_border_width is None else item_border_width
        )
        self._corner_radius = (
            ThemeManager.theme["CComboBox"]["corner_radius"] 
            if corner_radius is None else corner_radius
        )
        self._text_color = (
            ThemeManager.theme["CComboBox"]["text_color"] 
            if text_color is None else text_color
        )
        self._background_color = (
            ThemeManager.theme["CComboBox"]["background_color"] 
            if background_color is None else background_color
        )
        self._hover_color = (
            ThemeManager.theme["CComboBox"]["hover_color"] 
            if hover_color is None else hover_color
        )
        self._border_color = (
            ThemeManager.theme["CComboBox"]["border_color"] 
            if border_color is None else border_color
        )
        self._menu_background_color = (
            ThemeManager.theme["CComboBox"]["menu_background_color"] 
            if menu_background_color is None else menu_background_color
        )
        self._menu_border_color = (
            ThemeManager.theme["CComboBox"]["menu_border_color"] 
            if menu_border_color is None else menu_border_color
        )
        self._item_text_color = (
            ThemeManager.theme["CComboBox"]["item_text_color"] 
            if item_text_color is None else item_text_color
        )
        self._item_background_color = (
            ThemeManager.theme["CComboBox"]["item_background_color"] 
            if item_background_color is None else item_background_color
        )
        self._item_hover_color = (
            ThemeManager.theme["CComboBox"]["item_hover_color"] 
            if item_hover_color is None else item_hover_color
        )
        self._item_border_color = (
            ThemeManager.theme["CComboBox"]["border_color"] 
            if item_border_color is None else item_border_color
        )
        self._disabled_text_color= (
            ThemeManager.theme["CComboBox"]["disabled_text_color"] 
            if disabled_text_color is None else disabled_text_color
        )
        self._disabled_background_color = (
            ThemeManager.theme["CComboBox"]["disabled_background_color"] 
            if disabled_background_color is None else disabled_background_color
        )
        
        #flags
        self._palette_changing = False

        #class variables
        self._layout = QtWidgets.QVBoxLayout()
        self._combobox = QtWidgets.QComboBox()

        #set font of combobox
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
        self.setMinimumSize(self._width + 10, self._height + 10)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.resize(self._width + 10, self._height + 10)

        #set content margins of layout
        self._layout.setContentsMargins(5,5,5,5)
        
        #set attributes of combobox
        if self._values is not None:
            self._combobox.addItems(self._values) 
        self._combobox.setCurrentText(self._current_value)
        self._combobox.setPlaceholderText("CComboBox")
        self._combobox.setToolTip(self._tooltip)
        self._combobox.setFont(self._font)

        self._combobox.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
        )

        self._change_theme()

        self._layout.addWidget(self._combobox)
        self.setLayout(self._layout)

    #method to access widget
    def combo_box(self):
        return self._combobox

    #method to update the theme of the combobox
    def _change_theme(self):

        #get styling of combobox and store it in a tuple with keys for variable
        variables = (
            ("_text_color", self._text_color),
            ("_background_color", self._background_color), 
            ("_border_color", self._border_color), 
            ("_hover_color", self._hover_color),
            ("_menu_background_color", self._menu_background_color), 
            ("_menu_border_color", self._menu_border_color),  
            ("_item_text_color", self._item_text_color),
            ("_item_background_color", self._item_background_color), 
            ("_item_border_color", self._item_border_color), 
            ("_item_hover_color", self._item_hover_color),
            ("_disabled_text_color", self._disabled_text_color), 
            ("_disabled_background_color", self._disabled_background_color)
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

        #get image path for down arrow
        main_directory = path.dirname(path.abspath(__file__))
        main_path = Path(main_directory).parent
        image_path = path.join(main_path, "widgets", "images", "down_arrow.png").replace("\\", "/")

        #set the stylesheet of combobox with new colors
        self._combobox.setStyleSheet(
                "QComboBox{"
                    f"background-color: {new_colors['_background_color']};"
                    f"color: {new_colors['_text_color']};"
                    f"border: {self._border_width}px solid {new_colors['_border_color']};"
                    f"border-radius: {self._corner_radius}px;"
                    f"width: {self._width}px;"
                    f"width: {self._height}px;"
                    "padding-left: 5px;"
                "}"

                "QComboBox:hover {"
                    f"background-color: {new_colors['_hover_color']};"
                "}"

                "QComboBox:disabled {" 
                    f"color: {new_colors['_disabled_text_color']};"
                    f"background-color: {new_colors['_disabled_background_color']};"
                "}"

                "QComboBox::drop-down {"
                    f"image: url({image_path});"
                    "width: 28px;"
                    "height: 28px;"
                "}"

                "QComboBox QAbstractItemView {"
                    f"background-color: {new_colors['_menu_background_color']};"
                    f"border: {self._item_border_width}px solid {new_colors['_menu_border_color']};"
                    "outline: none;"
                "}"

                "QComboBox QAbstractItemView::item {"
                    f"background-color: {new_colors['_item_background_color']};"
                    f"color: {new_colors['_item_text_color']};"
                    f"border: {self._item_border_width}px solid {new_colors['_item_border_color']};"
                    "outline: none;"
                "}"

                "QComboBox QAbstractItemView::item:hover {"
                    f"background-color: {new_colors['_item_hover_color']};"
                "}"
            )

    #method to change theme when system theme changes 
    def changeEvent(self, event): 
        
        #if the system combobox palette changes and palette is not already changing continue
        if (
            event.type() == QtCore.QEvent.Type.PaletteChange and not self._palette_changing
        ): 
            self._palette_changing = True       #update palette changing flag to true   
            self._change_theme()                #update combobox theme
            self._palette_changing = False      #update palette changing flag to false

        super().changeEvent(event)
        
