#default libraries
from typing import Union, Tuple, Optional, Any, Callable

#installed libraries
from PySide6 import QtWidgets, QtGui, QtCore

#local libraries
from ..appearance import ThemeManager, ModeManager

# The purpose of this program is to provide a class for styled 
# frames using QFrame from PySide6 in connection to the 
# PyCt library
#
# Author: D. Liam Mc.
# Version: 0.0.2
# Date: May 15, 2025

class CFrame(QtWidgets.QFrame):
    def __init__(self,
                master: Any,
                width: Optional[int] = None,
                height: Optional[int] = None,
                border_width: Optional[int] = None,
                corner_radius: Optional[int] = None,
                border_color: Optional[Union[str, Tuple[str, str]]] = None,
                background_color: Optional[Union[str, Tuple[str, str]]] = None,
                layout_type: str = "vertical"
    ):
        super().__init__()

        #set default parameters and dimensions
        self._master = master
        self._width = width
        self._height = height
        self._layout_type = layout_type 

        #set appearance and styling parameters
        self._border_width = ThemeManager.theme["CFrame"]["border_width"] if border_width is None else border_width
        self._corner_radius = ThemeManager.theme["CFrame"]["corner_radius"] if corner_radius is None else corner_radius
        self._border_color = ThemeManager.theme["CFrame"]["border_color"] if border_color is None else border_color
        self._background_color = ThemeManager.theme["CFrame"]["background_color"] if background_color is None else background_color

        #flags
        self._palette_changing = False

        #create layout variable for frame depending on what layout type the user wants
        if layout_type == "horizontal":
            self._layout = QtWidgets.QHBoxLayout()
        else:
            self._layout = QtWidgets.QVBoxLayout()

        #set default attributes for class
        self.setParent(self._master)

        if not self._width is None:
            self.setMinimumWidth(self._width)
        if not self._height is None: 
            self.setMinimumHeight(self._height)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        
        self.setLayout(self._layout)

        #update theme of frame
        self._change_theme()

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
    def layout_type(self):
        return self._layout_type
    
    @property
    def border_width(self):
        return self._border_width
    
    @property
    def corner_radius(self):
        return self._corner_radius
    
    @property
    def border_color(self):
        return self._border_color
    
    @property
    def background_color(self):
        return self._background_color
    
    @master.setter
    def master(self, master: Any):
        self._master = master

        self.setParent(self._master)

    @width.setter
    def width(self, width: int = 200):
        self._width = width

        self.setMinimumSize(self._width, self._height)

    @height.setter
    def height(self, height: int = 200):
        self._height = height

        self.setMinimumSize(self._width, self._height)

    @width.setter
    @height.setter
    def size(self, width: int = 200, height: int = 200):
        self._width = width
        self._height = height

        self.setMinimumSize(self._width, self._height)

    @layout_type.setter
    def layout_type(self, layout_type: str = "vertical"):
        self._layout_type = layout_type

    @border_width.setter
    def border_width(self, border_width: Optional[Union[str, Tuple[str, str]]] = None):
        self._border_width = border_width

        self._change_theme()

    @corner_radius.setter
    def corner_radius(self, corner_radius: Optional[Union[str, Tuple[str, str]]] = None):
        self._corner_radius = corner_radius

        self._change_theme()

    @border_color.setter
    def border_color(self, border_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._border_color = border_color

        self._change_theme()

    @background_color.setter
    def background_color(self, background_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._background_color = background_color

        self._change_theme()

    def _change_theme(self):

        #get styling of frame and store it in a tuple with keys for variable
        variables = (("_border_color", self._border_color),
                     ("_background_color", self._background_color))
        
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

        #set the stylesheet of frame with new colors
        self.setStyleSheet(
            "QFrame {"
                f"background-color: {new_colors["_background_color"]};"
                f"border: {self._border_width}px solid {new_colors["_border_color"]};"
                f"border-radius: {self._corner_radius}px"
            "}"
        )

    #method for adding widgets to layout of frame
    def addWidget(self, widget: Any):
        self._layout.addWidget(widget)

    #method to change theme when system theme changes 
    def changeEvent(self, event): 

        #if the system frame palette changes and palette is not already changing continue
        if event.type() == QtCore.QEvent.Type.PaletteChange and not self._palette_changing: 
            self._palette_changing = True       #update palette changing flag to true   
            self._change_theme()               #update frame theme
            self._palette_changing = False      #update palette changing flag to false

        super().changeEvent(event)
