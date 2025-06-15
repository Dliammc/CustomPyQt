class ModeManager:
    mode: str = None
    
    @classmethod
    def set_mode(cls, mode: str):
        if mode.lower() == "system":
            cls.mode = mode.lower()
        elif mode.lower() == "dark":
            cls.mode = mode.lower()
        else:
            cls.mode = mode.lower()
            