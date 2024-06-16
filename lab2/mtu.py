import argparse
import ipaddress
import platform
import socket
import subprocess
import sys 

HEADER_SIZE = 28
MIN_MTU = 0
MAX_MTU = 10000

def ping(mtu, hostname):
    os = platform.system().lower()
    command = f"ping -M do -s {mtu} -c 1 {host}"
    if os == "darwin":
        command = f"ping -D -s {mtu} -c 1 {hostname}"
    elif os == "windows":
        command = f"ping -M do -s {mtu} -n 1 {hostname}"
    try:
        out = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    except Exception:
        return False
    return out.wait() == 0

def find_mtu(hostname):
    left = MIN_MTU
    right = MAX_MTU - HEADER_SIZE
    while right > left + 1:
        mid = (left + right) // 2
        if ping(mid, hostname):
            left = mid
        else:
            right = mid
    return left

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, required=True, help="hostname")
    args = parser.parse_args()
    hostname = args.host
    try:
        ipaddress.IPv4Address(socket.gethostbyname(host))
    except Exception:
        raise Exception("Invalid host")
    print(f"Minimal MTU for {hostname} (with header size) is: {find_mtu(hostname) + HEADER_SIZE}")