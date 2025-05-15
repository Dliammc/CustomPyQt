from .windows import CMainWindow
from .windows import CTopLevel

from .appearance import ThemeManager
from .appearance import ModeManager

from .widgets import CButton
from .widgets import CLineEdit
from .widgets import CTextEdit
from .widgets import CFrame

def set_color_theme(theme: str):
    ThemeManager.load_theme(theme)

def set_appearance_mode(mode: str):
    ModeManager.set_mode(mode)

def update_appearance_mode(mode: str, obj):
    ModeManager.set_mode(mode)

    obj._change_theme()

def get_color_theme():
    return ThemeManager.theme

def get_appearance_mode():
    return ModeManager.mode
