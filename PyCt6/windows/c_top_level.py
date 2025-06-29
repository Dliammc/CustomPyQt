#default libraries
from platform import system, release
from typing import Union, Tuple, Optional, Any

#local libraries
from ..appearance import ModeManager

#installed libraries
from PySide6 import QtWidgets, QtGui, QtCore

# The purpose of this program is to provide a class for styled 
# main windows using QWidget from PySide6 in connection to the 
# PyCt library
#
# Author: D. Liam Mc.
# Version: 6.0.4
# Date: June 28, 2025

class CTopLevel(QtWidgets.QWidget):
     def __init__(
               self,
               width: int = 500,
               height: int = 300,
               x: Optional[int] = None,
               y: Optional[int] = None,
               title: str = "CTopLevel",
               icon: Optional[str] = None,
               background_color: Union[str, Tuple[str, str]] = None,
               opacity: float = 1.0,
               style: Optional[str] = None
     ):
          super().__init__()

          #initialize variables for class

          #default parameters and dimensions
          self._width = width
          self._height = height
          self._x = x
          self._y = y

          #set window title and icon
          self._title = title
          self._icon = icon

          #set window background color, opacity, and style
          self._background_color = background_color
          self._opacity = opacity
          self._style = style

          #flags
          self._palette_changing = False

          #set attributes for class
          self.activateWindow()
          self.setWindowTitle(self._title)
          self.setWindowOpacity(self._opacity)

          if self._icon != None:
               self.setWindowIcon(QtGui.QIcon(self._icon))

          if self._x != None and self._y == None:
              self.setGeometry(x, self.pos().y(), self._width, self._height)
          elif self._y != None and self._x == None:
              self.setGeometry(self.pos().x(), self._y, self._width, self._height)
          elif self._x != None and self._y != None:
               self.setGeometry(self._x, self._y, self._width, self._height)
          else:
               self.resize(self._width, self._height)

          self._change_theme()

     @property
     def width(self):
          return self._width
     
     @property
     def height(self):
          return self._height
     
     @property
     def x(self):
          return self._x

     @property
     def y(self):
          return self._y
     
     @property
     def title(self):
          return self._title

     @property
     def icon(self):
          return self._icon
     
     @property
     def background_color(self):
          return self._background_color
     
     @property
     def opacity(self):
          return self._opacity
     
     @property
     def style(self):
          return self._style

     @width.setter
     def width(self, width:int = 300):
          self._width = width

     @height.setter
     def height(self, height:int = 150):
          self._height = height

     @x.setter
     def x(self, x:Optional[int] = None):
          self._x = x

     @y.setter
     def y(self, y:Optional[int] = None):
          self._y = y

     @title.setter
     def title(self, title:str = "CMainWindow"):
          self._title = title

     @icon.setter
     def icon(self, icon:Optional[str] = None):
          self._icon = icon

     @background_color.setter
     def background_color(
          self, background_color:Union[str, Tuple[str, str]] = None
     ):
          self._background_color = background_color

     @opacity.setter
     def opacity(self, opacity:float = 1.0):
          self._opacity = opacity

     @style.setter
     def style(self, style:str = "mica"):
          self._style = style

     #method for setting window background color
     def setWindowBackground(
               self, background_color:Union[str, Tuple[str, str]] = None
          ):
          self._background_color = background_color

          if self._background_color != None:
               if isinstance(self._background_color, tuple):
                    if ModeManager.mode == "light":
                         self.setStyleSheet(
                              "QWidget {background-color: " + f"{self._background_color[0]}" + "}"
                         )
                    elif ModeManager.mode == "dark":
                         self.setStyleSheet(
                              "QWidget {background-color: " + f"{self._background_color[1]}" + "}"
                         )
                    else:
                         if (
                              QtGui.QGuiApplication.styleHints().colorScheme() == QtCore.Qt.ColorScheme.Dark
                         ):
                              self.setStyleSheet(
                                   "QWidget {background-color: " + f"{self._background_color[1]}" + "}"
                              )
                         else:
                             self.setStyleSheet(
                                  "QWidget {background-color: " + f"{self._background_color[0]}" + "}"
                              ) 

               else:
                    self.setStyleSheet(
                         "QWidget {background-color: " + f"{self._background_color}" + "}"
                    )

          else:
               if ModeManager.mode == "light":
                    self.setStyleSheet("QWidget {background-color: rgb(243,243,243)}")
               elif ModeManager.mode == "dark":
                    self.setStyleSheet("QWidget {background-color: rgb(30,30,30)}")
               else:
                    if (
                         QtGui.QGuiApplication.styleHints().colorScheme() == QtCore.Qt.ColorScheme.Dark
                    ):
                         self.setStyleSheet("QWidget {background-color: rgb(30,30,30)}")
                    else:
                         self.setStyleSheet("QWidget {background-color: rgb(243,243,243)}") 


     def setWindowTheme(self, theme:str = "system"):
          self._theme = theme

          if self._theme != None:
               self._change_theme()

     def setWindowIcon(self, icon:str = None):
          self._icon = icon

          if self._icon != None:
               self.setWindowIcon(QtGui.QIcon(self._icon))

     def _change_theme(self):
          if system() == "Windows" and release() == "11" and self._style != None:
               try:
                    from win32mica import ApplyMica, MicaStyle, MicaTheme

                    if ModeManager.mode == "dark":
                         theme = MicaTheme.DARK
                    elif ModeManager.mode == "light":
                         theme = MicaTheme.LIGHT
                    else:
                         theme = MicaTheme.AUTO

                    self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

                    if self._style.lower() == "mica":
                         ApplyMica(self.winId(), theme, MicaStyle.DEFAULT)
                    elif self._style.lower() == "alt":
                         ApplyMica(self.winId(), theme, MicaStyle.ALT)
               except:
                    pass

          self.setWindowBackground(self._background_color)

     def changeEvent(self, event): 
          if event.type() == QtCore.QEvent.Type.ThemeChange: 
               self._change_theme()