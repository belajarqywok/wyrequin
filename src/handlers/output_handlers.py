from xlsxwriter import Workbook
from src.utilities import utilities

# for handling sniffing output
class output_handlers (utilities) :

    def __init__ (self, filename: str) -> None:

        # data iteration
        self.__iter = 1

        # get file extension
        get_ext: str = self.get_file_ext(filename = filename)
        
        # if output file is csv
        if get_ext == ".csv" :
            self.handler = csv_handler(
                filename = filename
            )

        # if output file is xlsx
        elif get_ext == ".xlsx" :
            self.handler = xlxs_handler(
                filename = filename
            )

    # append data to output file
    # (csv || xlsx || json)
    def append (self, time: str, source: str, destination: str,
        protocol: str, length: int, info: str) -> None:

        self.handler.append(

            no          = str(self.__iter),
            time        = time,
            source      = source,
            destination = destination,
            protocol    = protocol,
            length      = length,
            info        = info
        )

        # increment data iteration
        self.__iter += 1


# csv output handler
class csv_handler:

    def __init__ (self, filename: str) -> None:

        # file mode
        self.__mode = "w"

        # open file \w mode
        self.__file = open(filename, self.__mode)
        
        # field declaration
        self.__file.write(
            '"No.","Time","Source","Destination","Protocol","Length","Info"\n'
        )

    # append data to output file (csv)
    def append(self, **params: dict) -> None:

        # change write mode (w) to append mode (a)
        self.__mode = "a"

        self.__file.write(
            f'"{params.get("no")}","{params.get("time")}","{params.get("source")}",'+
            f'"{params.get("destination")}","{params.get("protocol")}","{params.get("length")}",'+
            f'"{params.get("info")}"\n'
        )
        
        

# xlsx output handler
class xlxs_handler:

    def __init__ (self, filename: str) -> None:
        
        # set workbook
        self.__workbook = Workbook(filename)

        # set worksheet
        self.__worksheet = self.__workbook.add_worksheet("main")


    def append(self, **params: dict) -> None:

        for index_param,(
            _,
            value_param
        ) in enumerate(params.items()) :

            self.__worksheet.write(

                int(params.get("no")),
                index_param, value_param
            )

        self.__workbook.close()
