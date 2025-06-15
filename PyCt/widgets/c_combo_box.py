#default libraries
from typing import Union, Tuple, Optional, Any

#installed libraries
from PySide6 import QtWidgets, QtGui, QtCore

#local libraries
from ..appearance import ThemeManager, ModeManager

# The purpose of this program is to provide a class for styled 
# comboboxes using QComboBox from PySide6 in connection to the 
# PyCt library
#
# Author: D. Liam Mc.
# Version: 0.0.3
# Date: June 15, 2025

class CComboBox(QtWidgets.QWidget):
    def __init__(
            self,
            master: Any,
            width: int = 140,
            height: int = 28,
            values: list = None,
            current_value: str = str(list[0]) if not None else "CComboBox",
            tooltip: Optional[str] = None,
            font_family: str = "Calibri",
            font_size: int = 12,
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

        match self._font_style:
            case "bold":
                self._font.setBold(True)
            case "Underline":
                self._font.setUnderline(True)
            case "italic":
                self._font.setItalic(True)
            case "strikeout":
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
    def values(self):
        return self._values
    
    @property
    def current_value(self):
        return self._current_value
    
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
    def menu_border_width(self):
        return self._menu_border_width
    
    @property
    def item_border_width(self):
        return self._item_border_width
    
    @property
    def corner_radius(self):
        return self._corner_radius
    
    @property
    def text_color(self):
        return self._text_color
    
    @property
    def background_color(self):
        return self._background_color
    
    @property
    def border_color(self):
        return self._border_color
    
    @property
    def hover_color(self):
        return self._hover_color
    
    @property
    def menu_background_color(self):
        return self._menu_background_color
    
    @property
    def menu_border_color(self):
        return self._menu_border_color
    
    @property
    def item_text_color(self):
        return self._item_text_color
    
    @property
    def item_background_color(self):
        return self._item_background_color
    
    @property
    def item_border_color(self):
        return self._item_border_color
    
    @property
    def item_hover_color(self):
        return self._item_hover_color
    
    @property
    def disabled_text_color(self):
        return self._disabled_text_color
    
    @property
    def disabled_background_color(self):
        return self._disabled_background_color
    
    @property
    def command(self):
        return self._command
    
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

    @values.setter
    def values(self, values:list = None):
        self._values = values

        self._combobox.addItems(self._values)

    @current_value.setter
    def current_value(
        self, current_value:str = str(list[0]) if not None else "CComboBox"
    ):
        self._current_value = current_value

        self._combobox.setCurrentText(self._current_value)

    @tooltip.setter
    def tooltip(self, tooltip: Optional[str] = None):
        self._tooltip = tooltip

        self._combobox.setToolTip(self._tooltip)

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
                self._font.setUnderLine(True)
            case "italic":
                self._font.setItalic(True)
            case "strikeout":
                self._font.setStrikeOut(True)

    @border_width.setter
    def border_width(self, border_width: Optional[int] = None):
        self._border_width = (
            ThemeManager.theme["CComboBox"]["border_width"] 
            if border_width is None else border_width
        )

        self._change_theme()

    @menu_border_width.setter
    def menu_border_width(self, menu_border_width: Optional[int] = None):
        self._menu_border_width = (
            ThemeManager.theme["CComboBox"]["menu_border_width"] 
            if menu_border_width is None else menu_border_width
        )

        self._change_theme()

    @item_border_width.setter
    def item_border_width(self, item_border_width: Optional[int] = None):
        self._item_border_width = (
            ThemeManager.theme["CComboBox"]["item_border_width"] 
            if item_border_width is None else item_border_width
        )

        self._change_theme()

    @corner_radius.setter
    def corner_radius(self, corner_radius: Optional[int] = None):
        self._corner_radius = (
            ThemeManager.theme["CComboBox"]["corner_radius"] 
            if corner_radius is None else corner_radius
        )

        self._change_theme()

    @text_color.setter
    def text_color(
        self, text_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._text_color = (
            ThemeManager.theme["CComboBox"]["text_color"] 
            if text_color is None else text_color
        )

        self._change_theme()

    @background_color.setter
    def background_color(
        self, background_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._background_color = (
            ThemeManager.theme["CComboBox"]["background_color"] 
            if background_color is None else background_color
        )

        self._change_theme()

    @border_color.setter
    def border_color(
        self, border_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._border_color = (
            ThemeManager.theme["CComboBox"]["border_color"] 
            if border_color is None else border_color
        )

        self._change_theme()

    @hover_color.setter
    def hover_color(
        self, hover_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._hover_color = (
            ThemeManager.theme["CComboBox"]["hover_color"] 
            if hover_color is None else hover_color
        )

        self._change_theme()

    @menu_background_color.setter
    def menu_background_color(
        self, menu_background_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._menu_background_color = (
            ThemeManager.theme["CComboBox"]["background_color"] 
            if menu_background_color is None else menu_background_color
        )

        self._change_theme()

    @menu_border_color.setter
    def menu_border_color(
        self, menu_border_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._menu_border_color = (
            ThemeManager.theme["CComboBox"]["border_color"] 
            if menu_border_color is None else menu_border_color
        )

        self._change_theme()

    @item_text_color.setter
    def item_text_color(
        self, item_text_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._item_text_color = (
            ThemeManager.theme["CComboBox"]["item_text_color"] 
            if item_text_color is None else item_text_color
        )

        self._change_theme()

    @item_background_color.setter
    def item_background_color(
        self, item_background_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._item_background_color = (
            ThemeManager.theme["CComboBox"]["item_background_color"] 
            if item_background_color is None else item_background_color
        )

        self._change_theme()

    @item_border_color.setter
    def item_border_color(
        self, item_border_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._item_border_color = (
            ThemeManager.theme["CComboBox"]["item_border_color"] 
            if item_border_color is None else item_border_color
        )

        self._change_theme()

    @item_hover_color.setter
    def item_hover_color(
        self, item_hover_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._item_hover_color = (
            ThemeManager.theme["CComboBox"]["item_hover_color"] 
            if item_hover_color is None else item_hover_color
        )

        self._change_theme()

    @disabled_text_color.setter
    def disabled_text_color(
        self, disabled_text_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._disabled_text_color = (
            ThemeManager.theme["CComboBox"]["disabled_text_color"] 
            if disabled_text_color is None else disabled_text_color
        )

        self._change_theme()

    @disabled_background_color.setter
    def disabled_background_color(
        self, disabled_background_color: Optional[Union[str, Tuple[str, str]]] = None
    ):
        self._disabled_background_color = (
            ThemeManager.theme["CComboBox"]["disabled_background_color"] 
            if disabled_background_color is None else disabled_background_color
        )

        self._change_theme()

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

        #set the stylesheet of combobox with new colors
        self._combobox.setStyleSheet(
                "QComboBox{"
                f"background-color: {new_colors["_background_color"]};"
                f"color: {new_colors["_text_color"]};"
                f"border: {self._border_width}px solid {new_colors["_border_color"]};"
                f"border-radius: {self._corner_radius}px"
                "}"

                "QComboBox:hover {"
                f"background-color: {new_colors["_hover_color"]}"
                "}"

                "QComboBox:disabled {" 
                f"color: {new_colors["_disabled_text_color"]};"
                f"background-color: {new_colors["_disabled_background_color"]}"
                "}"

                "QComboBox::drop-down {"
                "image: url('PyCt/widgets/images/down_arrow.png');"
                "width: 28px;"
                "height: 28px"
                "}"

                "QComboBox QAbstractItemView {"
                f"background-color: {new_colors["_menu_background_color"]};"
                f"border: {self._item_border_width}px solid {new_colors["_menu_border_color"]};"
                "outline: none"
                "}"

                "QComboBox QAbstractItemView::item {"
                f"background-color: {new_colors["_item_background_color"]};"
                f"color: {new_colors["_item_text_color"]};"
                f"border: {self._item_border_width}px solid {new_colors["_item_border_color"]};"
                "outline: none"
                "}"

                "QComboBox QAbstractItemView::item:hover {"
                f"background-color: {new_colors["_item_hover_color"]}"
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
        