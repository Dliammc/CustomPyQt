#default libraries
from platform import system, release
from typing import Union, Tuple, Optional, Any, Callable

#installed libraries
from PySide6 import QtWidgets, QtGui, QtCore

#local libraries
from ..appearance import ThemeManager, ModeManager

# The purpose of this program is to provide a class for styled 
# buttons using QPushButton from PySide6 in connection to the 
# CPyQt library
#
# Author: D. Liam Mc.
# Version: 0.0.2
# Date: May 8, 2025

class CButton(QtWidgets.QWidget):
    def __init__(
                self,
                master: Any,
                width: int = 140,
                height: int = 28,
                text: str = "CButton",
                icon: Optional[str] = None,
                font_family: str = "Arial",
                font_size: int = 10,
                font_style: Optional[str] = None,
                border_width: Optional[int] = None,
                corner_radius: Optional[int] = None,
                text_color: Optional[Union[str, Tuple[str, str]]] = None,
                background_color: Optional[Union[str, Tuple[str, str]]] = None,
                border_color: Optional[Union[str, Tuple[str, str]]] = None,
                hover_color: Optional[Union[str, Tuple[str, str]]] = None,
                pressed_color: Optional[Union[str, Tuple[str, str]]] = None,
                disabled_text_color: Optional[Union[str, Tuple[str, str]]] = None,
                disabled_background_color: Optional[Union[str, Tuple[str, str]]] = None,  
                command: Union[Callable[[], Any], None] = None      
    ):
        super().__init__()

        #initialize variables for class

        #default parameters and dimensions
        self._master = master
        self._width = width
        self._height = height
        self._command = command

        #set text, icon and font parameters
        self._text = text
        self._icon = icon
        self._font_family = font_family
        self._font_size = font_size
        self._font_style = font_style

        #set appearance and styling parameters
        self._border_width = (
            ThemeManager.theme["CButton"]["border_width"] if border_width is None else border_width
            )
        self._corner_radius = (
            ThemeManager.theme["CButton"]["corner_radius"] if corner_radius is None else corner_radius
            )
        self._text_color = (
            ThemeManager.theme["CButton"]["text_color"] if text_color is None else text_color
            )
        self._background_color = (
            ThemeManager.theme["CButton"]["background_color"] if background_color is None else background_color
            )
        self._border_color = (
            ThemeManager.theme["CButton"]["border_color"] if border_color is None else border_color
            )
        self._hover_color = (
            ThemeManager.theme["CButton"]["hover_color"] if hover_color is None else hover_color
            )
        self._pressed_color = (
            ThemeManager.theme["CButton"]["pressed_color"] if pressed_color is None else pressed_color
            )
        self._disabled_text_color= (
            ThemeManager.theme["CButton"]["disabled_text_color"] if disabled_text_color is None else disabled_text_color
            )
        self._disabled_background_color = (
            ThemeManager.theme["CButton"]["disabled_background_color"] if disabled_background_color is None else disabled_background_color
            )

        #flags
        self._palette_changing = False

        #class variables
        self._layout = QtWidgets.QVBoxLayout()
        self._button = QtWidgets.QPushButton()

        #set font of button
        self._font = QtGui.QFont(self._font_family, self._font_size)

        match self._font_style:
            case "bold":
                self._font.setBold(True)
            case "underline":
                self._font.setUnderLine(True)
            case "italic":
                self._font.setItalic(True)
            case "strikeout":
                self._font.setStrikeOut(True)

        #set attributes of class
        self.setParent(self._master), 
        self.setFixedSize(self._width + 10, self._height + 10)

        #set content margins of layout
        self._layout.setContentsMargins(5,5,5,5)
        
        #set attributes of button
        self._button.setText(self._text)
        self._button.setIcon(QtGui.QIcon(self._icon))
        self._button.setFont(self._font)

        self._button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        #add commands and methods to button on certain events
        if command != None:
            self._button.clicked.connect(self._command)
            self._button.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)

        self._button.pressed.connect(self.__shrink_size)
        self._button.released.connect(self.__grow_size)

        self.__change_theme()

        self._layout.addWidget(self._button)
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
    def icon(self):
        return self._icon
    
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
    def background_color(self):
        return self._background_color
    
    @property
    def border_color(self):
        return self._border_color
    
    @property
    def hover_color(self):
        return self._hover_color
    
    @property
    def pressed_color(self):
        return self._pressed_color
    
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

        self.setFixedSize(self._width + 10, self._height + 10)

    @height.setter
    def height(self, height: int = 28):
        self._height = height

        self.setFixedSize(self.width + 10, self._height + 10)

    @height.setter
    @width.setter
    def size(self, width: int = 140, height: int = 28):
        self._width = width
        self._height = height

        self.setFixedSize(self.width + 10, self._height + 10)

    @text.setter
    def text(self, text: str = "CButton"):
        self._text = text

        self._button.setText(self._text)

    @icon.setter
    def icon(self, icon: Optional[str] = None):
        self._icon = icon

        self._button.setIcon(QtGui.QIcon(self._icon))

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
        self._border_width = ThemeManager.theme["CButton"]["border_width"] if border_width is None else border_width

        self.__change_theme()

    @corner_radius.setter
    def corner_radius(self, corner_radius: Optional[int] = None):
        self._corner_radius = ThemeManager.theme["CButton"]["corner_radius"] if corner_radius is None else corner_radius

        self.__change_theme()

    @text_color.setter
    def text_color(self, text_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._text_color = ThemeManager.theme["CButton"]["text_color"] if text_color is None else text_color

        self.__change_theme()

    @background_color.setter
    def background_color(self, background_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._background_color = ThemeManager.theme["CButton"]["background_color"] if background_color is None else background_color

        self.__change_theme()

    @border_color.setter
    def border_color(self, border_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._border_color = ThemeManager.theme["CButton"]["border_color"] if border_color is None else border_color

        self.__change_theme()

    @hover_color.setter
    def hover_color(self, hover_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._hover_color = ThemeManager.theme["CButton"]["hover_color"] if hover_color is None else hover_color

        self.__change_theme()

    @text_color.setter
    def pressed_color(self, pressed_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._pressed_color = ThemeManager.theme["CButton"]["pressed_color"] if pressed_color is None else pressed_color

        self.__change_theme()

    @text_color.setter
    def disabled_text_color(self, disabled_text_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._disabled_text_color = ThemeManager.theme["CButton"]["text_color"] if disabled_text_color is None else disabled_text_color

        self.__change_theme()

    @disabled_background_color.setter
    def disabled_background_color(self, disabled_background_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._disabled_background_color = ThemeManager.theme["CButton"]["disabled_background_color"] if disabled_background_color is None else disabled_background_color

        self.__change_theme()

    @command.setter
    def command(self, command: Union[Callable[[], Any], None] = None):
        self._command = command

        self._button.clicked.connect(self._command)

    #method to shrink the size of the button when button is held down
    def __shrink_size(self):
        self._layout.setContentsMargins(6,6,6,6)        #increase content margins to shrink button

        self._font.setPointSize(self._font_size - 1)        #decrease font point size of button

        self._button.setFont(self._font)        #update font of button

        self._corner_radius -= 1        #decrease corner radius of button

        self.__change_theme()       #update button theme 

    #method to resize button to original size when button is released
    def __grow_size(self):
        self._layout.setContentsMargins(5,5,5,5)        #reset contents margins of button

        self._font.setPointSize(self._font_size)        #reset point size of button

        self._button.setFont(self._font)        #update font of button

        self._corner_radius += 1        #reset corner radius of button

        self.__change_theme()       #update button theme

    #method to update the theme of the button
    def __change_theme(self):

        #get styling of button and store it in a tuple with keys for variable
        variables = (
            ("_text_color", self._text_color),
            ("_background_color", self._background_color), 
            ("_border_color", self._border_color), 
            ("_hover_color", self._hover_color), 
            ("_pressed_color", self._pressed_color), 
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
                    if QtGui.QGuiApplication.styleHints().colorScheme() == QtCore.Qt.ColorScheme.Dark:
                        new_colors[attribute] = color[1]

                    #otherwise use the light color
                    else:
                        new_colors[attribute] = color[0] 

            #otherwise it is a string and set the 
            #new color to that specified color
            else:
                new_colors[attribute] = color

        #set the stylesheet of button with new colors
        self._button.setStyleSheet(
                "QPushButton {"
                f"background-color: {new_colors["_background_color"]};"
                f"color: {new_colors["_text_color"]};"
                f"border: {self._border_width}px solid {new_colors["_border_color"]};"
                f"border-radius: {self._corner_radius}px"
                "}"

                "QPushButton:hover {"
                f"background-color: {new_colors["_hover_color"]}"
                "}"

                "QPushButton:pressed {"
                f"background-color {new_colors["_pressed_color"]}"
                "}"

                "QPushButton:disabled {" 
                f"color: {new_colors["_disabled_text_color"]};"
                f"background-color: {new_colors["_disabled_background_color"]}"
                "}"
            )

    #method to change theme when system theme changes 
    def changeEvent(self, event): 

        #if the system button palette changes and palette is not already changing continue
        if event.type() == QtCore.QEvent.Type.PaletteChange and not self._palette_changing: 
            self._palette_changing = True       #update palette changing flag to true   
            self.__change_theme()               #update button theme
            self._palette_changing = False      #update palette changing flag to false

        super().changeEvent(event)