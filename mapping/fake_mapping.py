#!/usr/bin/env python3
"""
Script:	mapping.py
Date:	2021-01-30	

Platform: macOS/Windows/Linux

Description:

"""
__author__ = 'thedzy'
__copyright__ = 'Copyright 2021, thedzy'
__license__ = 'GPL'
__version__ = '1.0'
__maintainer__ = 'thedzy'
__email__ = 'thedzy@hotmail.com'
__status__ = 'Development'

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import socket
import requests
import argparse
import numpy
import struct


def main():
    print('traceroute')

    lat_start, lon_start = get_coordinates()
    lat_array, lon_array = [lat_start], [lon_start]

    dest_ip = socket.gethostbyname(options.dest_address)

    port = 33434
    max_hops = 30
    icmp = socket.getprotobyname('icmp')
    udp = socket.getprotobyname('udp')
    ttl = 1
    while True:
        recv_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        send_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, udp)
        send_socket.setsockopt(socket.SOL_IP, socket.IP_TTL, ttl)

        # Build the GNU timeval struct (seconds, microseconds)
        timeout = struct.pack("ll", 2, 0)

        # Set the receive timeout so we behave more like regular traceroute
        recv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeout)

        recv_socket.bind(("", port))
        send_socket.sendto(b'', (dest_ip.encode(), port))
        curr_addr = None
        curr_name = None
        finished = False
        tries = 2
        while not finished and tries > 0:
            try:
                _, curr_addr = recv_socket.recvfrom(512)
                finished = True
                curr_addr = curr_addr[0]
                try:
                    curr_name = socket.gethostbyaddr(curr_addr)[0]
                except socket.error:
                    curr_name = curr_addr
            except socket.error as err:
                tries = tries - 1
                # sys.stdout.write("* ")

        send_socket.close()
        recv_socket.close()

        if not finished:
            pass

        if curr_addr is not None:
            curr_host = "%s (%s)" % (curr_name, curr_addr)
        else:
            curr_host = ""

        lat_end, lon_end = get_coordinates(curr_addr)

        if lat_end is not None and lon_end is not None and curr_addr is not None:
            print(curr_addr, '> ', lat_end, lon_end)
            lat_array.append(lat_end)
            lon_array.append(lon_end)

        ttl += 1
        if curr_addr == dest_ip or ttl > max_hops:
            break


    # https://matplotlib.org/basemap/api/basemap_api.html
    line_width = 3

    print('draw')
    # plot a pretty enough map

    fig = plt.figure(figsize=(12, 12), edgecolor='white')
    # map = Basemap(projection='ortho', lat_0=sum(lat_array)/len(lat_array), lon_0=sum(lon_array)/len(lon_array), resolution='l')
    map = Basemap(projection='mill', lat_0=sum(lat_array)/len(lat_array), lon_0=sum(lon_array)/len(lon_array))

    map.drawcoastlines(linewidth=0.25)
    #map.drawcountries(linewidth=0.3, linestyle='solid', color='#888888')
    map.fillcontinents(color='green', lake_color=(0.53, 0.71, 0.84))
    map.shadedrelief(scale=0.1)
    map.drawmapboundary(fill_color='blue')

    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(numpy.arange(0, 360, 30))
    map.drawparallels(numpy.arange(-90, 90, 30))


    print(lon_array)
    print(lat_array)

    for index in range(len(lat_array)-1):
        print(lat_array[index], lon_array[index], '->', lat_array[index+1], lon_array[index+1])
        if lat_array[index] > lat_array[index+1] + 5 and lat_array[index] > lat_array[index+1] - 5:
            map.plot(lon_array[index], lat_array[index],
                     marker='${}$'.format(index),
                     markersize=line_width * 5,
                     markeredgewidth=0,
                     markerfacecolor='black',
                     latlon=True)
        #map.plot(lon_array[index+1], lat_array[index+1], marker=7, markersize=line_width * 5, markeredgewidth=0, markerfacecolor='red',
        #         latlon=True)

        map.drawgreatcircle(lon_array[index], lat_array[index], lon_array[index+1], lat_array[index+1], color='r', linewidth=line_width,
                                    linestyle='solid')

    map.plot(lon_array[index+1], lat_array[index+1],
             marker=7,
             markersize=line_width * 5,
             markeredgewidth=0,
             markerfacecolor='black',
             latlon=True)

    plt.tight_layout()
    plt.show()


def get_coordinates(ip=''):
    url = 'http://ip-api.com/json/{}'

    request = requests.get(url.format(ip))
    # print(request.text)
    try:
        response = request.json()
        return response['lat'], response['lon']
    except:
        return None, None


if __name__ == '__main__':
    def parser_formatter(format_class, **kwargs):
        """
        Use a raw parser to use line breaks, etc
        :param format_class: (class) formatting class
        :param kwargs: (dict) kwargs for class
        :return: (class) formatting class
        """
        try:
            return lambda prog: format_class(prog, **kwargs)
        except TypeError:
            return format_class


    # Create parser
    parser = argparse.ArgumentParser(description='Description of the program',
                                     formatter_class=parser_formatter(
                                         argparse.RawTextHelpFormatter,
                                         indent_increment=4, max_help_position=12, width=160))

    # Destination
    parser.add_argument('dest_address', metavar='DESTINATION',
                        help='ip/adress of site')

    options = parser.parse_args()

    main()
