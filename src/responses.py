class responses :
    ### Tshark path not found response
    def path_not_found_response (self, path_location: str) -> None :

        print(f"{path_location} NOT FOUND !!!")

    ### About this tool response
    def about_this_tool_response (self) -> None : print(
        "\n\wyrequin is a packet sniffer / packet capture tool\n\n" +
        "[ + ] VERSION\n" +
        "    wyrequin v1.0\n\n" +
        "[ + ] USAGE\n" +
        "    $ wyrequin [COMMAND] [COMMAND] .....\n\n" +
        "[ + ] COMMAND\n" +
        "------------------------------------\n\n" +
        "Set Tshark Path                     wyrequin set-env [ -p | --path ] {tshark.exe} [ -i | --interface ] {network interface}\n" +
        "Streaming Capture                   wyrequin stream [ -o | --output ] {csv | xlsx | cap | pcap | json}\n"
    )

    ### Envronment created response
    def envronment_created_response (self, env_status: bool, error_message: str = "Error Unknown") -> None :

        success: str = "environment created successfully"
        failed:  str = f"environment failed to create, because {error_message}"

        print(success if env_status else failed)

    ### Streaming capture response
    def streaming_capture_response (self,
        interface: str, localtime: str, timestamp: str,
        source_address: str, source_port: str, network_protocol: str,
        destination_address: str, destination_port: str, packet_length: str
    ) : 
        print(
            f"[ {interface} ] {localtime} / {timestamp} | " +
            f"IP {source_address}:{source_port} < --( {network_protocol} )-- > {destination_address}:{destination_port} "+
            f"| {packet_length} bytes"
        )
