class csv_output_handler :
    def __init__(self, filename) :
        self.MODE = "w"

        self.file = open(filename, self.MODE)
        
        # field declaration
        self.file.write(
            '"No.","Time","Source","Destination","Protocol","Length","Info"\n'
        )

    def append(
        self,
        no: int, time: str, source: str, destination: str,
        protocol: str, length: int, info: str) :

        self.MODE = "a"

        self.file.write(
            f'"{no}","{time}","{source}","{destination}",' +
            f'"{protocol}","{length}","{info}"\n'
        )

