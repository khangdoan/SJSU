#!/bin/sh

#Clear all rules
iptables -F

#Allow PING for everyone
iptables -A FORWARD -p icmp -j ACCEPT

# allow HHTP/HHTPS for WIFI lan
iptables -A FORWARD -p tcp --dport 80 -j ACCEPT
iptables -A FORWARD -p tcp --dport 443 -j ACCEPT

#block HTTP/HTTPS from sjsu.edu and redirect to webproxy
# sjsu.edu -> 130.65.255.101
iptables -t nat -A OUTPUT -p tcp --dport 80  -d 130.65.255.101 -j DNAT --to-destination <web proxy's ip>
iptables -t nat -A OUTPUT -p tcp --dport 443  -d 130.65.255.101 -j DNAT --to-destination <web proxy's ip>

/etc/init.d/iptables save
/etc/init.d/iptables reload
