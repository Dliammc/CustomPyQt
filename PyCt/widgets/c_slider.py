#default libraries
from typing import Union, Tuple, Optional, Any
from math import sqrt

#installed libraries
from PySide6 import QtWidgets, QtGui, QtCore

#local libraries
from ..appearance import ThemeManager, ModeManager

# The purpose of this program is to provide a class for styled 
# sliders using QSlider from PySide6 in connection to the 
# PyCt library
#
# Author: D. Liam Mc.
# Version: 0.0.2
# Date: June 12, 2025

class CSlider(QtWidgets.QWidget):
    def __init__(
                self,
                master: Any,
                width: int = 280,
                height: int = 4,
                button_width: int = 14,
                button_height: int = 14,
                orientation: str = "horizontal",
                minimum: int = 0,
                maximum: int = 100,
                step: int = 1,
                value: int = 50,
                tooltip: Optional[str] = None,
                border_width: Optional[int] = None,
                corner_radius: Optional[int] = None,
                button_border_width: Optional[int] = None,
                button_corner_radius: Optional[int] = None,
                background_color: Optional[Union[str, Tuple[str, str]]] = None,
                progress_color: Optional[Union[str, Tuple[str, str]]] = None,
                border_color: Optional[Union[str, Tuple[str, str]]] = None,
                button_background_color: Optional[Union[str, Tuple[str, str]]] = None,
                button_border_color: Optional[Union[str, Tuple[str, str]]] = None,
                button_hover_color: Optional[Union[str, Tuple[str, str]]] = None,
                button_pressed_color: Optional[Union[str, Tuple[str, str]]] = None,
                disabled_background_color: Optional[Union[str, Tuple[str, str]]] = None,
                disabled_button_background_color: Optional[Union[str, Tuple[str, str]]] = None

                 ):
        super().__init__()

        self._master = master
        self._width = width
        self._height = height
        self._button_width = button_width
        self._button_height = button_height
        self._orientation = orientation
        self._minimum = minimum
        self._maximum = maximum
        self._step = step
        self._value = value
        self._tooltip = tooltip

        #set appearance and styling parameters
        self._border_width = (
            ThemeManager.theme["CSlider"]["border_width"] if border_width is None else border_width
        )
        self._corner_radius = (
            ThemeManager.theme["CSlider"]["corner_radius"] if corner_radius is None else corner_radius
        )
        self._button_border_width = (
            ThemeManager.theme["CSlider"]["button_border_width"] if button_border_width is None else button_border_width
        )
        self._button_corner_radius = (
            ThemeManager.theme["CSlider"]["button_corner_radius"] if button_corner_radius is None else button_corner_radius
        )
        self._background_color = (
            ThemeManager.theme["CSlider"]["background_color"] if background_color is None else background_color
        )
        self._progress_color = (
            ThemeManager.theme["CSlider"]["progress_color"] if progress_color is None else progress_color
        )
        self._border_color = (
            ThemeManager.theme["CSlider"]["border_color"] if border_color is None else border_color
        )
        self._button_background_color = (
            ThemeManager.theme["CSlider"]["button_background_color"] if button_background_color is None else button_background_color
        )
        self._button_border_color = (
            ThemeManager.theme["CSlider"]["button_border_color"] if button_border_color is None else button_border_color
        )
        self._button_hover_color = (
            ThemeManager.theme["CSlider"]["button_hover_color"] if button_hover_color is None else button_hover_color
        )
        self._button_pressed_color = (
            ThemeManager.theme["CSlider"]["button_pressed_color"] if button_pressed_color is None else button_pressed_color
        )
        self._disabled_background_color = (
            ThemeManager.theme["CSlider"]["disabled_background_color"] if disabled_background_color is None else disabled_background_color
        )
        self._disabled_button_background_color = (
            ThemeManager.theme["CSlider"]["disabled_button_background_color"] if disabled_button_background_color is None else disabled_button_background_color
        )

        #flags
        self._palette_changing = False

        #class variables
        self._layout = QtWidgets.QVBoxLayout()
        self._slider = QtWidgets.QSlider()

        #set attributes of class
        self.setParent(self._master), 
        self.setMinimumSize(self._width, self._height)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.resize(self._width, self._height)

        #set content margins of layout
        self._layout.setContentsMargins(5,5,5,5)

        #set orientation of slider
        if self._orientation == "horizontal":
            self._slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        else:
            self._slider.setOrientation(QtCore.Qt.Orientation.Vertical)

        #set attributes of slider
        self._slider.setMinimum(self._minimum)
        self._slider.setMaximum(self._maximum)
        self._slider.setValue(self._value)
        self._slider.setSingleStep(self._step)
        self._slider.setToolTip(self._tooltip)

        self._slider.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)

        self._change_theme()

        self._layout.addWidget(self._slider)
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
    def button_width(self):
        return self._button_width
    
    @property
    def button_height(self):
        return self._button_height
    
    @property
    def orientation(self):
        return self._orientation
    
    @property
    def maximum(self):
        return self._maximum
    
    @property
    def minimum(self):
        return self._minimum
    
    @property
    def value(self):
        return self._value
    
    @property
    def step(self):
        return self._step
    
    @property
    def tooltip(self):
        return self._tooltip
    
    @property
    def border_width(self):
        return self._border_width
    
    @property
    def corner_radius(self):
        return self._corner_radius
    
    @property
    def button_border_width(self):
        return self._button_border_width
    
    @property
    def button_corner_radius(self):
        return self._button_corner_radius
    
    @property
    def background_color(self):
        return self._background_color
    
    @property
    def border_color(self):
        return self._border_color
    
    @property
    def progress_color(self):
        return self._progress_color
    
    @property
    def button_background_color(self):
        return self._button_background_color
    
    @property
    def button_border_color(self):
        return self._button_hover_color
    
    @property
    def button_hover_color(self):
        return self._hover_color
    
    @property
    def button_pressed_color(self):
        return self._button_pressed_color
    
    @property
    def disabled_background_color(self):
        return self._disabled_background_color
    
    @property
    def disabled_button_background_color(self):
        return self._disabled_button_background_color

    @master.setter
    def master(self, master: Any):
        self._master = master

        self.setParent(self._master)

    @width.setter
    def width(self, width: int = 140):
        self._width = width

        self.setMinimumSize(self._width + 10, self._height + 10)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.resize(self._width + 10, self._height + 10)

    @height.setter
    def height(self, height: int = 28):
        self._height = height

        self.setMinimumSize(self._width + 10, self._height + 10)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.resize(self._width + 10, self._height + 10)

    @height.setter
    @width.setter
    def size(self, width: int = 140, height: int = 28):
        self._width = width
        self._height = height

        self.setMinimumSize(self._width + 10, self._height + 10)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.resize(self._width + 10, self._height + 10)

    @button_width.setter
    def button_width(self, button_width: int = 14):
        self._button_width = button_width

        self._change_theme()

    @button_height.setter
    def button_height(self, button_height: int = 14):
        self._button_height = button_height

        self._change_theme()

    @button_width.setter
    @button_height.setter
    def button_size(self, button_width: int = 14, button_height: int = 14):
        self._button_width = button_width
        self._button_height = button_height

        self._change_theme()

    @orientation.setter
    def orientation(self, orientation: str = "horizontal"):
        self._orientation = orientation

        if self._orientation == "horizontal":
            self._slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        else:
            self._slider.setOrientation(QtCore.Qt.Orientation.Vertical)

    @maximum.setter
    def maximum(self, maximum: str = 100):
        self._maximum = maximum

        self._slider.setMaximum(self._maximum)

    @minimum.setter
    def minimum(self, minimum: str = 0):
        self._minimum = minimum

        self._slider.setMinimum(self._minimum)

    @value.setter
    def value(self, value: str = 50):
        self._value = value

        self._slider.setValue(self._value)

    @step.setter
    def step(self, step: str = 1):
        self._step = step

        self._slider.setSingleStep(self._step)

    @tooltip.setter
    def tooltip(self, tooltip: Optional[str] = None):
        self._tooltip = tooltip

        self._slider.setToolTip(self._tooltip)

    @border_width.setter
    def border_width(self, border_width: Optional[int] = None):
        self._border_width = ThemeManager.theme["CSlider"]["border_width"] if border_width is None else border_width

        self._change_theme()

    @corner_radius.setter
    def corner_radius(self, corner_radius: Optional[int] = None):
        self._corner_radius = ThemeManager.theme["CSlider"]["corner_radius"] if corner_radius is None else corner_radius

        self._change_theme()

    @button_border_width.setter
    def button_border_width(self, button_border_width: Optional[int] = None):
        self._button_border_width = ThemeManager.theme["CSlider"]["button_border_width"] if button_border_width is None else button_border_width

        self._change_theme()

    @button_corner_radius.setter
    def button_corner_radius(self, button_corner_radius: Optional[int] = None):
        self._button_corner_radius = ThemeManager.theme["CSlider"]["button_corner_radius"] if button_corner_radius is None else button_corner_radius

        self._change_theme()

    @background_color.setter
    def background_color(self, background_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._background_color = ThemeManager.theme["CSlider"]["background_color"] if background_color is None else background_color

        self._change_theme()

    @border_color.setter
    def border_color(self, border_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._border_color = ThemeManager.theme["CSlider"]["border_color"] if border_color is None else border_color

        self._change_theme()

    @progress_color.setter
    def progress_color(self, progress_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._progress_color = ThemeManager.theme["CSlider"]["progress_color"] if progress_color is None else progress_color

        self._change_theme()

    @button_background_color.setter
    def button_background_color(self, button_background_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._button_background_color = ThemeManager.theme["CSlider"]["button_background_color"] if button_background_color is None else button_background_color

        self._change_theme()

    @button_border_color.setter
    def button_border_color(self, button_border_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._button_border_color = ThemeManager.theme["CSlider"]["button_border_color"] if button_border_color is None else button_border_color

        self._change_theme()

    @button_hover_color.setter
    def button_hover_color(self, button_hover_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._button_hover_color = ThemeManager.theme["CSlider"]["button_hover_color"] if button_hover_color is None else button_hover_color

        self._change_theme()

    @button_pressed_color.setter
    def button_pressed_color(self, button_pressed_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._button_pressed_color = ThemeManager.theme["CSlider"]["button_pressed_color"] if button_pressed_color is None else button_pressed_color

        self._change_theme()
    

    @disabled_background_color.setter
    def disabled_background_color(self, disabled_background_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._disabled_background_color = ThemeManager.theme["CSlider"]["disabled_background_color"] if disabled_background_color is None else disabled_background_color

        self._change_theme()

    @disabled_button_background_color.setter
    def disabled_background_color(self, disabled_button_background_color: Optional[Union[str, Tuple[str, str]]] = None):
        self._disabled_button_background_color = ThemeManager.theme["CSlider"]["disabled_button_background_color"] if disabled_button_background_color is None else disabled_button_background_color

        self._change_theme()

    
    #method to update the theme of the button
    def _change_theme(self):

        #get styling of button and store it in a tuple with keys for variable
        variables = (
            ("_background_color", self._background_color), 
            ("_border_color", self._border_color), 
            ("_progress_color", self._progress_color),
            ("_button_background_color", self._button_background_color),
            ("_button_border_color", self._button_border_color),
            ("_button_hover_color", self._button_hover_color),
            ("_button_pressed_color", self._button_pressed_color),
            ("_disabled_background_color", self._disabled_background_color),
            ("_disabled_button_background_color", self._disabled_button_background_color)
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
        self._slider.setStyleSheet(
                "QSlider {"
                    "background: transparent;"
                    f"height: {self._button_height + 2}px;"
                    
               "}"

               "QSlider::groove:horizontal, QSlider::groove:vertical {"
                    f"background: {new_colors["_background_color"]};"
                    f"height: {self._height}px;"
                    f"border: {self._border_width}px solid {new_colors["_border_color"]};"
                    f"border-radius: {self._corner_radius}px;"
                    
                "}" 
                
                "QSlider::handle:horizontal, QSlider::handle:vertical {"
                    f"background: {new_colors["_button_background_color"]};"
                    f"border: {self._border_width}px solid {new_colors["_button_border_color"]};"
                    f"width: {self._button_width}px;"
                    f"height: {self._button_height}px;"
                    "margin: -5px 0;"
                    f"border-radius: {self._button_corner_radius}px;"
                    
                "}"

                "QSlider::handle:horizontal:hover, QSlider::handle:vertical:hover {"
                    f"background: {new_colors["_button_hover_color"]};"
                "}"

                "QSlider::handle:horizontal:pressed, QSlider::handle:vertical:pressed {"
                    f"background: {new_colors["_button_pressed_color"]};"              
                "}"

                "QSlider::add-page:horizontal, QSlider::add-page:vertical {"
                    f"background: {new_colors["_background_color"]};"
                    f"border-radius: {self._corner_radius}px;"
                "}"

                "QSlider::sub-page:horizontal, QSlider::sub-page:vertical {"
                    f"background: {new_colors["_progress_color"]};"
                    f"border-radius: {self._corner_radius}px;"
                "}"
            )

    #method to change theme when system theme changes 
    def changeEvent(self, event): 
        
        #if the system button palette changes and palette is not already changing continue
        if event.type() == QtCore.QEvent.Type.PaletteChange and not self._palette_changing: 
            self._palette_changing = True       #update palette changing flag to true   
            self._change_theme()               #update button theme
            self._palette_changing = False      #update palette changing flag to false

        super().changeEvent(event)
