import os
from pathlib import Path
from dotenv import load_dotenv

# Configuration
class config :
    def __init__ (self) -> None :

        # Environment File
        self.environment: str = ".qpcap_env"

        # Output Extension Included
        self.output_ext_included: list = [".csv", ".xlsx", ".cap", ".pcap", ".json"]

        # Read Extension Included
        self.read_ext_included: list = [".cap", ".pcap"]

        # Load Environment File
        self.__dotenv: Path = Path(self.environment)
        load_dotenv(dotenv_path = self.__dotenv)

        # Network Interface
        self.network_interface: str = os.getenv("INTERFACE")
    
        # Tshark Path / Location
        self.tshark_location: str   = os.getenv("TSHARK_PATH")

    