from os.path import exists
from src.config import config 
from src.responses import responses
from src.utilities import utilities

from src.handlers import (
    set_env_handler,
    streaming_capture_handler
)

# Command Lines Parser
class argument_parser :
    def __init__ (self, sys_args: list) -> None :
        self.__config: config = config()
        self.__utils: utilities = utilities()
        self.__responses: responses = responses()

        self.__sys_args: list = sys_args


    def __repr__ (self) -> None :
        try :
            # set path feature
            if (
                self.__sys_args[1] == "set-env"
            ) : self.__set_env_cmd()

            # Streaming Capture
            elif (
                self.__sys_args[1] == "stream"
            ) : self.__streaming_capture_cmd()

            else : self.__responses.about_this_tool_response()

        except IndexError : self.__responses.about_this_tool_response()

        return repr(None)


    # Set Environment Command Line Method
    def __set_env_cmd (self) -> None :
        try :
            ### Path Argument
            path_arg: bool = ( 
                (self.__sys_args[2] == "-p") |
                (self.__sys_args[2] == "--path")
            )

            tshark_location: str = self.__sys_args[3]

            ### Interface Argument
            interface_arg: bool = ( 
                (self.__sys_args[4] == "-i") |
                (self.__sys_args[4] == "--interface")
            )

            interface_name: str = self.__sys_args[5]

            ### Output Argument
            output_arg: bool = ( 
                (self.__sys_args[6] == "-o") |
                (self.__sys_args[6] == "--output")
            )

            output: str = self.__sys_args[7]
            
            ### Validation Arguments
            if (path_arg & interface_arg & output_arg) :

                status, message = set_env_handler.env_handler(
                    path_location    = tshark_location,
                    network_inteface = interface_name,
                    sniffing_output  = output
                ).set_env()
                
                ### Environment Status Response
                self.__responses.envronment_created_response(

                    env_status    = status,
                    error_message = message
                )

            ### If validation fails, then user will be shown about the use of this tool.
            else : self.__responses.about_this_tool_response()


        ### If there is an "IndexError" error it will be displayed about the use of this tool.
        except IndexError : self.__responses.about_this_tool_response()


    ### Streaming Capture Command Line Method
    def __streaming_capture_cmd (self) -> None :
        try :
            if exists(self.__config.environment) : repr(
                streaming_capture_handler.streaming_capture(
                    env_is_exist = True
                )
            )

            else :
                ### Tshark Path Argument
                tshark_path_arg: bool = ( 
                    (self.__sys_args[2] == "-p") |
                    (self.__sys_args[2] == "--path")
                )

                tshark_path: str = self.__sys_args[3]

                # Network Interface Argument
                interface_arg: bool = (
                    (self.__sys_args[4] == "-i") |
                    (self.__sys_args[4] == "--interface")
                )

                network_interface: str = self.__sys_args[5]

                # Output File Argument
                output_arg: bool = (
                    (self.__sys_args[6] == "-o") |
                    (self.__sys_args[6] == "--output")
                )

                output_file: str = self.__sys_args[7]

                # Validation Arguments
                if (
                    # Output File Validation
                    (output_arg & self.__utils.is_file_included(filename = output_file)) &

                    # Network Interface Validation
                    (interface_arg & isinstance(network_interface, str)) &

                    # Tshark Path Validation                    
                    (tshark_path_arg & exists(tshark_path))
                ) : 
                    try :
                        repr(
                            streaming_capture_handler.streaming_capture(
                                tshark_location   = tshark_path,
                                network_interface = network_interface,
                                output_capture    = output_file
                            )
                        )

                    except TypeError : pass

                else  : self.__responses.about_this_tool_response()

        except IndexError : self.__responses.about_this_tool_response()
