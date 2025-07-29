import os
from enum import Enum
from datetime import datetime
from pathlib import Path


class gp_log_colors(Enum):
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"


class gp_log_level(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class gp_logger:

    def __init__(self) -> None:
        self.file_log_enabled = False
        self.file_path: Path = None
        self.line_length = 256
        self.log_colors = {
            gp_log_level.DEBUG: gp_log_colors.BLUE,
            gp_log_level.INFO: gp_log_colors.RESET,
            gp_log_level.WARNING: gp_log_colors.YELLOW,
            gp_log_level.ERROR: gp_log_colors.RED
        }
        self.debug_enabled = False

        return
    

    def enable_file_log(self, file_path: str, file_name: str) -> None:
        #check file path, if correct
        new_path = Path(file_path)

        try:
            new_path.mkdir(parents = True, exist_ok = True)
            self.file_path = new_path / file_name
            self.file_log_enabled = True
        
        except Exception as e:
            self.log(gp_log_level.ERROR, f'Couldn\'t create filepath. Error {e}')


        return
    

    def disable_file_log(self) -> None:
        self.file_path = None
        self.file_log_enabled = False

        return
    

    def log(self, log_level: gp_log_level, message: str) -> None:

        if log_level == gp_log_level.DEBUG and not self.debug_enabled:

            return
        
        formatted_message = message.replace('\n', "\n".ljust(42))
        timestamp = f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S.")}{datetime.now().microsecond // 1000:03d}'
        log_text = f'{(timestamp + "      " + log_level.value).ljust(41)}{formatted_message}'
        print(f'{self.log_colors[log_level].value}{log_text}{gp_log_colors.RESET.value}')

        if self.file_log_enabled:

            with self.file_path.open('a', encoding="utf-8") as f:
                f.write(log_text + '\n')

        return
    

    def set_color(self, log_level, color: str) -> bool:

        return True
    
    
    


