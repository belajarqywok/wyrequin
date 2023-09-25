build :
	echo build

tests :
	tox

remove_env :
	rm .qpcap_env

create_env_test: 
	python qpcap.py set-env -p F:/Wireshark/tshark.exe -i Wi-Fi -o xxx.cs

stream_test :
	python qpcap.py stream -p F:/Wireshark/tshark.exe -i Wi-Fi -o xxx.csv

notebook :
	python3 -m notebook