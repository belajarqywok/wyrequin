import pyshark
from src.config import config
from src.responses import responses
from src.handlers.output_handlers import output_handlers

# Streaming Capture
class streaming_capture (config) :
    def __init__ (self,
        env_is_exist: bool = False, 
        **streaming_params: dict 
    ) -> None :
        super().__init__()

        self.env_is_exist: bool = env_is_exist 
        self.streaming_params: dict = streaming_params

        self.__responses: responses = responses()

    def __repr__ (self) :
        if self.env_is_exist :
            interface: str = self.network_interface
            capture = pyshark.LiveCapture(
                interface = interface, 
                tshark_path = self.tshark_location
            )

        else :
            interface: str = self.streaming_params["network_interface"]
            capture = pyshark.LiveCapture(
                interface = interface, 
                tshark_path = self.streaming_params["tshark_location"]
            )

        # csv handler
        csv_handler = output_handlers(
            filename = self.streaming_params.get("output_capture")
        )

        for packet in capture.sniff_continuously() :
            try :
                # Sniffing time
                localtime: str = f"{packet.sniff_time}"
                timestamp: str = f"{packet.sniff_timestamp}"

                # packet info
                frame_info:       str = f"{packet.frame_info}"
                packet_length:    str = f"{packet.length}" 
                network_protocol: str = f"{packet.transport_layer}"


                # Get source address and port
                source_address:   str = f"{packet.ip.src}"
                source_port:      str = f"{packet[network_protocol].srcport}"

                # Get destination address and port
                destination_address: str = f"{packet.ip.dst}"
                destination_port:    str = f"{packet[network_protocol].dstport}"

                # csv handler
                csv_handler.append(
                    time        = timestamp,
                    source      = f"{source_address}:{source_port}",
                    destination = f"{destination_address}:{destination_port}",
                    protocol    = network_protocol,
                    length      = int(packet_length),
                    info        = frame_info
                )

                # Capture response
                # Log format :
                #   [ Wi-Fi ] date / timestamp | IP xx:xx < --(TCP)-- > xx:xx [ xx.com ] | 000 bytes

                self.__responses.streaming_capture_response(

                    # network interface
                    interface = interface,

                    # localtime (UTC)
                    localtime = localtime,

                    # timestamp
                    timestamp = timestamp,

                    # source address and port
                    # example : xxx.xxx.xxx.xxx:xxx
                    source_address = source_address,
                    source_port = source_port,

                    # destination address and port
                    # example : xxx.xxx.xxx.xxx:xxx
                    destination_address = destination_address,
                    destination_port = destination_port,

                    # network transport protocol (TCP / UDP)
                    network_protocol = network_protocol,

                    # packet length (byte)
                    packet_length = packet_length
                )

            except ( 
                KeyboardInterrupt,
                AttributeError,
                TypeError,
                EOFError,
                KeyError
            ) : pass
            