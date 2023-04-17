import socket
import struct

"""This code defines a function get_ip_range(network_address) that 
takes a network address in the form of a string, net, and returns 
a list of IP addresses within that network. """

def get_ip_range(network_address):
    """
    Calculates the IP range for a given network address.

    Args:
        network_address (str): The network address in CIDR notation (e.g., '10.62.12.0/23').

    Returns:
        A list of IP addresses that belong to the calculated IP range.
    """
    ip, cidr = network_address.split('/')
    cidr = int(cidr)
    host_bits = 32 - cidr
    i = struct.unpack('>I', socket.inet_aton(ip))[0]  # Note the endianness
    start = (i >> host_bits) << host_bits
    end = start | ((1 << host_bits) - 1)
    return [socket.inet_ntoa(struct.pack('>I', i)) for i in range(start, end+1)]
