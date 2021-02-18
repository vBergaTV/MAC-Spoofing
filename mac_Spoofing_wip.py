import subprocess

subprocess.call("ifconfig enp2s0 down", shell=True)
subprocess.call("ifconfig enp2s0 hw ether 00:2a:01:bb:22:cc", shell=True)
subprocess.call("ifconfig enp2s0 up", shell=True)
