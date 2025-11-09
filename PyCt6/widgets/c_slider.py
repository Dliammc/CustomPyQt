#default libraries
from typing import Union, Tuple, Optional, Any
from math import sqrt

#installed libraries
from PySide6 import QtWidgets, QtGui, QtCore

#local libraries
from ..appearance import ThemeManager, ModeManager

# The purpose of this program is to provide a class for styled 
# sliders using QSlider from PySide6 in connection to the 
# PyCt6 library
#
# Author: D. Liam Mc.
# Version: 6.1.0
# Date: November 8, 2025

class CSlider(QtWidgets.QWidget):
    def __init__(
            self,
            master: Any,
            width: Optional[int] = None,
            height: Optional[int] = None,
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

        #initialize variables for class

        #default parameters and dimensions
        self._master = master

        if width is None:
            if orientation == "horizontal":
                width = 280
            else:
                width = 4
        if height is None:
            if orientation == "horizontal":
                height = 4
            else:
                height = 280

        self._width = width
        self._height = height
        self._button_width = button_width
        self._button_height = button_height

        #set orientation, min, max, step, value and tooltip parameters
        self._orientation = orientation
        self._minimum = minimum
        self._maximum = maximum
        self._step = step
        self._value = value
        self._tooltip = tooltip

        #set appearance and styling parameters
        self._border_width = (
            ThemeManager.theme["CSlider"]["border_width"] 
            if border_width is None else border_width
        )
        self._corner_radius = (
            ThemeManager.theme["CSlider"]["corner_radius"] 
            if corner_radius is None else corner_radius
        )
        self._button_border_width = (
            ThemeManager.theme["CSlider"]["button_border_width"] 
            if button_border_width is None else button_border_width
        )
        self._button_corner_radius = (
            ThemeManager.theme["CSlider"]["button_corner_radius"] 
            if button_corner_radius is None else button_corner_radius
        )
        self._background_color = (
            ThemeManager.theme["CSlider"]["background_color"] 
            if background_color is None else background_color
        )
        self._progress_color = (
            ThemeManager.theme["CSlider"]["progress_color"] 
            if progress_color is None else progress_color
        )
        self._border_color = (
            ThemeManager.theme["CSlider"]["border_color"] 
            if border_color is None else border_color
        )
        self._button_background_color = (
            ThemeManager.theme["CSlider"]["button_background_color"] 
            if button_background_color is None else button_background_color
        )
        self._button_border_color = (
            ThemeManager.theme["CSlider"]["button_border_color"] 
            if button_border_color is None else button_border_color
        )
        self._button_hover_color = (
            ThemeManager.theme["CSlider"]["button_hover_color"] 
            if button_hover_color is None else button_hover_color
        )
        self._button_pressed_color = (
            ThemeManager.theme["CSlider"]["button_pressed_color"] 
            if button_pressed_color is None else button_pressed_color
        )
        self._disabled_background_color = (
            ThemeManager.theme["CSlider"]["disabled_background_color"] 
            if disabled_background_color is None else disabled_background_color
        )
        self._disabled_button_background_color = (
            ThemeManager.theme["CSlider"]["disabled_button_background_color"] 
            if disabled_button_background_color is None else disabled_button_background_color
        )

        #flags
        self._palette_changing = False

        #class variables
        self._layout = QtWidgets.QVBoxLayout()
        self._slider = QtWidgets.QSlider()
        self._margin_left = 0
        self._margin_right = 0

        #set attributes of class
        self.setParent(self._master), 
        self.setMinimumSize(self._width + 12, self._height + 12)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        self.resize(self._width + 12, self._height + 12)

        #set content margins of layout
        self._layout.setContentsMargins(5,5,5,5)

        #set orientation of slider
        if self._orientation == "horizontal":
            self._margin_left = -5
            self._slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        else:
            self._margin_right = -5
            self._slider.setOrientation(QtCore.Qt.Orientation.Vertical)

        #set attributes of slider
        self._slider.setMinimum(self._minimum)
        self._slider.setMaximum(self._maximum)
        self._slider.setValue(self._value)
        self._slider.setSingleStep(self._step)
        self._slider.setToolTip(self._tooltip)

        self._slider.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding
        )

        self._layout.addWidget(self._slider)
        self.setLayout(self._layout)

    def slider(self):
        return self._slider
    
    #method to update the theme of the slider
    def _change_theme(self):

        #get styling of slider and store it in a tuple with keys for variable
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

        #set the stylesheet of slider with new colors
        self._slider.setStyleSheet(
                "QSlider {"
                    "background: transparent;"
                    f"height: {self._button_height + 2}px;"
                    f"width: {self._button_width + 2}px;"
                    
               "}"

               "QSlider::groove:horizontal, QSlider::groove:vertical {"
                    f"background: {new_colors['_background_color']};"
                    f"height: {self._height}px;"
                    f"width: {self._width}px;"
                    f"border: {self._border_width}px solid {new_colors['_border_color']};"
                    f"border-radius: {self._corner_radius}px;"
                    
                "}" 

                "QSlider::groove:horizontal:disabled, QSlider::groove:vertical:disabled {"
                    f"background: {new_colors['_disabled_background_color']};"
                "}"
                
                "QSlider::handle:horizontal, QSlider::handle:vertical {"
                    f"background: {new_colors['_button_background_color']};"
                    f"border: {self._border_width}px solid {new_colors['_button_border_color']};"
                    f"width: {self._button_width}px;"
                    f"height: {self._button_height}px;"
                    f"margin: {self._margin_left} {self._margin_right};"
                    f"border-radius: {self._button_corner_radius}px;"
                "}"

                "QSlider::handle:horizontal:disabled, QSlider::handle:vertical:disabled {"
                    f"background: {new_colors['_disabled_button_background_color']};"
                "}"

                "QSlider::handle:horizontal:hover, QSlider::handle:vertical:hover {"
                    f"background: {new_colors['_button_hover_color']};"
                "}"

                "QSlider::handle:horizontal:pressed, QSlider::handle:vertical:pressed {"
                    f"background: {new_colors['_button_pressed_color']};"              
                "}"

                "QSlider::add-page:horizontal, QSlider::add-page:vertical {"
                    f"background: {new_colors['_background_color']};"
                    f"border-radius: {self._corner_radius}px;"
                "}"

                "QSlider::add-page:horizontal:disabled, QSlider::add-page:vertical:disabled {"
                    f"background: {new_colors['_disabled_background_color']};"
                "}"

                "QSlider::sub-page:horizontal, QSlider::sub-page:vertical {"
                    f"background: {new_colors['_progress_color']};"
                    f"border-radius: {self._corner_radius}px;"
                "}"

                "QSlider::sub-page:horizontal:disabled, QSlider::sub-page:vertical:disabled {"
                    f"background: {new_colors['_disabled_background_color']};"
                "}"
            )

    #method to change theme when system theme changes 
    def changeEvent(self, event): 
        
        #if the system slider palette changes and palette is not already changing continue
        if (
            event.type() == QtCore.QEvent.Type.PaletteChange and not self._palette_changing
        ): 
            self._palette_changing = True       #update palette changing flag to true   
            self._change_theme()               #update slider theme
            self._palette_changing = False      #update palette changing flag to false

        super().changeEvent(event)
