import os
import json
from typing import Union
import pathlib


class ThemeManager:
    theme: dict = {}
    _default_themes = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
    _currently_loaded_theme: Union[str, None] = None

    @classmethod
    def load_theme(cls, theme: str):
        main_directory = os.path.dirname(os.path.abspath(__file__))

        if theme in cls._default_themes:

            main_path = pathlib.Path(main_directory).parent
            with open(os.path.join(main_path, "widgets", "themes", f"{theme}.json")) as input_file:
                cls.theme = json.load(input_file)
                print(theme)
                print("yes")
        else:
            with open(theme, "r") as input_file:
                cls.theme = json.load(input_file)

        cls._currently_loaded_theme = theme

    @classmethod
    def save_theme(cls):
        if cls._currently_loaded_theme is not None:
            if cls._currently_loaded_theme not in cls._default_themes:
                with open(cls._currently_loaded_theme, "r") as input_file:
                    json.dump(cls.theme, input_file, indent=4)
            else:
                raise ValueError(f"cannot modify builtin theme '{cls._currently_loaded_theme}'")
        else:
            raise ValueError(f"cannot save theme, no theme is loaded")
            