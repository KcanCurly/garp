from scapy.all import send, get_if_hwaddr
from scapy.layers.l2 import ARP, Ether
import argparse
import time
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Send gratuitous ARP packets at specified intervals")
    parser.add_argument("-i", "--ip", help="IP address to announce (Required)", required=True)
    parser.add_argument("-n", "--interface", help="Network interface to use (default: eth0)", default="eth0")
    parser.add_argument("-I", "--interval", help="Interval between packets in seconds (Default: 10)", default=10.0)
    args = parser.parse_args()

    m = get_if_hwaddr(args.interface)

    # Send unsolicited ARP (Gratuitous ARP)
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(
        op=2,           # ARP reply (even though unsolicited)
        psrc=args.ip,  # IP we're announcing
        hwsrc=m,  # Our MAC
        pdst=args.ip,  # Same as psrc
        hwdst="ff:ff:ff:ff:ff:ff"  # Broadcast
    )

    try:
        while True:
            send(packet, args.interface, verbose=False)
            time.sleep(args.interval)
    except Exception:
        print("Exiting...")
        sys.exit(1)