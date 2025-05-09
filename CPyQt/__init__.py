from .windows import CMainWindow as CMainWindow
from .windows import CTopLevel as CTopLevel

from .appearance import ThemeManager
from .appearance import ModeManager

from .widgets import CButton

def set_color_theme(theme: str):
    ThemeManager.load_theme(theme)

def set_appearance_mode(mode: str):
    ModeManager.set_mode(mode)

def get_color_theme():
    return ThemeManager.theme

def get_appearance_mode():
    return ModeManager.mode
