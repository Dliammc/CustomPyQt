from platform import system, release
from typing import Union, Tuple, Optional, Any

from PySide6 import QtWidgets, QtGui, QtCore

from c_main_window import CMainWindow

class CTopLevel(QtWidgets.QWidget):
     def __init__(
                self,
                master: Optional[Any] = None,
                title: str = "CTopLevel",
                icon: Optional[str] = None,
                width: int = 300,
                height: int = 150,
                x: Optional[int] = None,
                y: Optional[int] = None,
                bg: Union[str, Tuple[str, str]] = None,
                opacity: float = 1.0,
                style: Optional[str] = None,
                theme: str = "system"
                ):
          super().__init__()

          self._master = master
          self._title = title
          self._icon = icon
          self._x = x
          self._y = y
          self._width = width
          self._height = height
          self._bg = bg
          self._opacity = opacity
          self._style = style
          self._theme = theme

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

          self.changeTheme()

     @property
     def master(self):
          return self._master
     
     @property
     def title(self):
          return self._title

     @property
     def icon(self):
          return self._icon
     
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
     def bg(self):
          return self._bg
     
     @property
     def opacity(self):
          return self._opacity
     
     @property
     def style(self):
          return self._style
     
     @property
     def theme(self):
          return self._theme
     
     @master.setter
     def master(self, master:Any = None):
          self._master = master

     @title.setter
     def title(self, title:str = "CMainWindow"):
          self._title = title

     @icon.setter
     def icon(self, icon:str = None):
          self._icon = icon

     @width.setter
     def width(self, width:int = 300):
          self._width = width

     @height.setter
     def height(self, height:int = 150):
          self._height = height

     @x.setter
     def x(self, x:int = None):
          self._x = x

     @y.setter
     def y(self, y:int = None):
          self._y = y

     @bg.setter
     def bg(self, bg:Union[str, Tuple[str, str]] = None):
          self._bg = bg

     @opacity.setter
     def opacity(self, opacity:float = 1.0):
          self._opacity = opacity

     @style.setter
     def style(self, style:str = "mica"):
          self._style = style

     @theme.setter
     def theme(self, theme:str = "system"):
          self._theme = theme

     def setWindowBackground(self, bg:Union[str, Tuple[str, str]] = None):
          self._bg = bg

          if self._bg != None:
               if isinstance(self._bg, tuple):
                    if self._master == None:
                         if self._theme.lower() == "light":
                              self.setStyleSheet("QWidget {background-color: " + f"{self._bg[0]}" + "}")
                         elif self._theme.lower() == "dark":
                              self.setStyleSheet("QWidget {background-color: " + f"{self._bg[1]}" + "}")
                         else:
                              if QtGui.QGuiApplication.styleHints().colorScheme() == QtCore.Qt.ColorScheme.Dark:
                                   self.setStyleSheet("QWidget {background-color: " + f"{self._bg[1]}" + "}")
                              else:
                                   self.setStyleSheet("QWidget {background-color: " + f"{self._bg[0]}" + "}") 
                    elif isinstance(self._master, CMainWindow):
                         print("yes")
                         if self._master._theme.lower() == "light":
                              self.setStyleSheet("QWidget {background-color: " + f"{self._bg[0]}" + "}")
                         elif self._master._theme.lower() == "dark":
                              self.setStyleSheet("QWidget {background-color: " + f"{self._bg[1]}" + "}")
                         else:
                              if QtGui.QGuiApplication.styleHints().colorScheme() == QtCore.Qt.ColorScheme.Dark:
                                   self.setStyleSheet("QWidget {background-color: " + f"{self._bg[1]}" + "}")
                              else:
                                   self.setStyleSheet("QWidget {background-color: " + f"{self._bg[0]}" + "}") 


               else:
                    self.setStyleSheet("QWidget {background-color: " + f"{self._bg}" + "}")

          else:
               if self._master == None:
                    if self._theme.lower() == "light":
                         self.setStyleSheet("QWidget {background-color: rgb(243,243,243)}")
                    elif self._theme.lower() == "dark":
                         self.setStyleSheet("QWidget {background-color: rgb(30,30,30)}")
                    else:
                         if QtGui.QGuiApplication.styleHints().colorScheme() == QtCore.Qt.ColorScheme.Dark:
                              self.setStyleSheet("QWidget {background-color: rgb(30,30,30)}")
                         else:
                              self.setStyleSheet("QWidget {background-color: rgb(243,243,243)}")

               elif isinstance(self._master, CMainWindow):
                    if self._master._theme.lower() == "light":
                         self.setStyleSheet("QWidget {background-color: rgb(243,243,243)}")
                    elif self._master._theme.lower() == "dark":
                         self.setStyleSheet("QWidget {background-color: rgb(30,30,30)}")
                    else:
                         if QtGui.QGuiApplication.styleHints().colorScheme() == QtCore.Qt.ColorScheme.Dark:
                              self.setStyleSheet("QWidget {background-color: rgb(30,30,30)}")
                         else:
                              self.setStyleSheet("QWidget {background-color: rgb(243,243,243)}") 

     def setWindowTheme(self, theme:str = "system"):
          self._theme = theme

          if self._theme != None:
               self.changeTheme()

     def setWindowIcon(self, icon:str = None):
          self._icon = icon

          if self._icon != None:
               self.setWindowIcon(QtGui.QIcon(self._icon))

     def changeTheme(self):
          if system() == "Windows" and release() == "11":
               try:
                    from win32mica import ApplyMica, MicaStyle, MicaTheme

                    if self._master == None:
                         print("yes")
                         if self._theme.lower() == "dark":
                              theme = MicaTheme.DARK
                         elif self._theme.lower() == "light":
                              theme = MicaTheme.LIGHT
                         else:
                              theme = MicaTheme.AUTO

                         self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

                         if self._style.lower() == "mica":
                              ApplyMica(self.winId(), theme, MicaStyle.DEFAULT)
                         elif self._style.lower() == "alt":
                              ApplyMica(self.winId(), theme, MicaStyle.ALT)

                    elif isinstance(self._master, CMainWindow):
                         print("yes")
                         if self._master._theme.lower() == "dark":
                              theme = MicaTheme.DARK
                         elif self._master._theme.lower() == "light":
                              theme = MicaTheme.LIGHT
                         else:
                              theme = MicaTheme.AUTO

                         self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

                         if self._master._style.lower() == "mica":
                              ApplyMica(self.winId(), theme, MicaStyle.DEFAULT)
                         elif self._master._style.lower() == "alt":
                              ApplyMica(self.winId(), theme, MicaStyle.ALT)
               except:
                    pass

          self.setWindowBackground(self._bg)

     def changeEvent(self, event): 
          if event.type() == QtCore.QEvent.Type.ThemeChange: 
               self.changeTheme()