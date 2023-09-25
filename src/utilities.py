import re
from src.config import config 

### Utilities 
class utilities:
    def __init__ (self) -> None:
        self.__config = config()

    ### Get file extension
    def get_file_ext (self, filename: str) -> str:
        pattern: str = ".[a-zA-Z0-9]*"

        return re.findall(
            pattern = pattern,
            string  = filename
        )[-1]

    ### Is file included
    def is_file_included (self, filename: str) -> bool:
        file_ext: str = self.get_file_ext(filename = filename)
        
        if file_ext in self.__config.output_ext_included : return True 

        else : return False 
