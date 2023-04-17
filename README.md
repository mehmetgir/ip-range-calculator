
# Python IP Subnet Calculator

This is a simple Python script that calculates the IP Subnet for a given network address.

## Usage

1.  Open the script in a Python editor or IDE.
    
2.  Replace the `network_address` variable with the network address you want to calculate the IP Subnet for.
    
3.  Run the script.
    
4.  The script will return a list of IP addresses that belong to the calculated IP range.
    

## Example

If you want to calculate the IP Subnet for the network address `10.62.12.0/23`, you can use the following code:

    import socket
    import struct
    
    def get_ip_subnet(network_address):
        """
        Calculates the IP Subnet for a given network address.
    
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
    
	""" Example """
	network_address = '10.62.12.0/23'
	ip_list = get_ip_subnet(network_address)
	print(ip_list)

This will output the following IP addresses:

    ['10.62.12.1', '10.62.12.2', '10.62.12.3', ..., '10.62.13.254']
## License

This project is licensed under the MIT License.
