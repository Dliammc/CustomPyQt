#default libraries
from platform import system, release
from typing import Union, Tuple, Optional
from os import path
from pathlib import Path

#local libraries
from ..appearance import ModeManager

#installed libraries
from PySide6 import QtWidgets, QtGui, QtCore

# The purpose of this program is to provide a class for styled 
# main windows using QWidget from PySide6 in connection to the 
# PyCt library
#
# Author: D. Liam Mc.
# Version: 6.1.0
# Date: October 23, 2025

class CMainWindow(QtWidgets.QWidget):
     def __init__(
               self,
               width: int = 500,
               height: int = 300,
               x: Optional[int] = None,
               y: Optional[int] = None,
               title: str = "CMainWindow",
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

          if not self._icon:
               main_directory = path.dirname(path.abspath(__file__))
               main_path = Path(main_directory).parent
               image_path = path.join(main_path, "windows", "images", "logo.png").replace("\\", "/")

               self.setWindowIcon(QtGui.QIcon(image_path))
          else:
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
          if (
               event.type() == QtCore.QEvent.Type.PaletteChange and not self._palette_changing
          ): 
               self._palette_changing = True
               for child in self.children():
                    try:
                         child._change_theme()
                    except:
                         pass
               self._change_theme()
               self._palette_changing = False
