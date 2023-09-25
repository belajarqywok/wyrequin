import re
from os.path import exists
from src.config import config
from src.utilities import utilities

# Set Environment 
class env_handler (config) :
    def __init__ (self, 
        path_location:    str,
        network_inteface: str,
        sniffing_output:  str
    ) -> None :

        self.__path_location:     str = path_location
        self.__network_interface: str = network_inteface
        self.__sniffing_output:   str = sniffing_output

        self.__utils: utilities     = utilities()

        super().__init__()


    def set_env (self) -> tuple :
        ### Path validation
        if not exists(self.__path_location) :
            return False, f"{self.__path_location} not found !."

        ### Extension validation
        elif not self.__utils.is_file_included(namefile = self.__sniffing_output) :
            file_extension: str = self.__utils.get_file_ext(
                namefile = self.__sniffing_output
            )

            return False, f"extension '{file_extension}' not included !."

        else :
            with open(self.environment, "w+") as filename :
                filename.write(
                    f"TSHARK_PATH={self.__path_location}\n" +
                    f"INTERFACE={self.__network_interface}\n" +
                    f"OUTPUT={self.__sniffing_output}"
                )

                return exists(self.environment), ""
