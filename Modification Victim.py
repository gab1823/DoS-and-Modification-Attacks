#!/usr/bin/python
from scapy.all import *

# Target address
dip=sys.argv[1]

# Payloads
payload1=Raw("A"*8)
payload2=Raw("B"*8)

# IPv6 header
IP=IPv6(dst=dip)

# Calculating Checksum
payload=str(Raw("A"*8 + "B"*8))
echoReq=ICMPv6EchoRequest(data=payload)
csum=in6_chksum(58,IP/echoReq,str(echoReq))

# ICMPv6 header
icmpv6=ICMPv6EchoRequest(cksum=csum, data=payload1)

# Fragment headers
frag1=IPv6ExtHdrFragment(offset=0, m=1, id=12345, nh=58)
frag2=IPv6ExtHdrFragment(offset=2, m=0, id=12345, nh=58)

# Packets
packet1=IP/frag1/icmpv6
packet2=IP/frag2/payload2

# Sending packets
send(packet1)	
send(packet2)
