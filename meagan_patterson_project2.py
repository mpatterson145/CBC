#! /usr/bin/python3

'''
!!!!
NOTE THE FORMATTING OF THE HEADER AND THE OUTPUTS FROM EACH PROBLEM!!!
!!!!
'''

'''
Meagan Patterson
CSIA 450
Spring 2020
Project 2
'''

# LIBRARIES HERE
# import socket
# import scipy

#1.
# Calculate the number of potential 
# connections and the network density in a
# fixed-size network of 800 nodes with 
# 2000 actual connections.

# total nodes in the network
n = 800
# actual connections
actual_connections = 2000
# the formula for potential connections
potential_connections = int((n*(n-1))/2)
# the formula for network density
network_density = (actual_connections/potential_connections)
# print the results
print("#1.")
print("Potential Connections:", potential_connections)
print("Network Density:", round(network_density,2))
print(" ")

#2.	
# Create an updated SNMP Community String
# starting with "public_" and adding a 
# location of "CBC_WIRELESS"

# this is the default SNMP Community String
snmp_community_string = "public_"
# update it to include the organization location
location = "CBC_WIRELESS"
snmp_community_string += location
# print the results
print("#2.")
print("Updated SNMP Community String:", snmp_community_string)
print(" ")

#3. 
# Print the LENGTH of this updated SNMP Community String.
print("#3.")
print("Length:", len(snmp_community_string))
print(" ")

#4. 
# Create a list of OSI model layers 
# and return the "Presentation" layer by
# indexing the list.

#OSI Model
osimodel = ['application', 'presentation', 'session', 'transport', 'network', 'data link', 'physical']

print("#4.")
print("Layer *2* in the OSI Model:", osimodel[1]) 
print(" ")

#5. 
# Create two set data structures, one for
# the OSI model and one for the TCP/IP 
# model

# create two sets
osimodel = set(['application', 'presentation', 'session', 'transport', 'network', 'data link', 'physical'])
tcpipmodel = set(['application', 'transport', 'internet', 'network access'])

print("#5.")
print ("OSI Model Set:", osimodel) 
print("TCP/IP Model Set:", tcpipmodel )
print(" ")

#6. 
# Print the intersection set of the OSI 
# and TCP/IP sets

intersection_ports = osimodel & tcpipmodel
print("#6.")
print("Intersection Set of OSI & TCP/IP:", intersection_ports)
print(" ")

#7. 
# Create a function that returns a random IPv4 octet.
# This is just the random library for Python.
from random import randint

# This is the function
def getRandom():
    min_random_value = 0
    max_random_value = 255
    return randint(min_random_value, max_random_value)

# This gets the value
random_value = getRandom()

print("#7.")
print("IPv4 Octet:", random_value)
print(" ")

#8. 
# Create a dictionary object that contains
# the following protocols and ports: 
# Telnet:23,SMTP:25, HTTP:80, HTTPS:443, 
# where the protocol is the key.

# Create the dictionary.
Protocol_Port_dictionary = {'Telnet':23, 'SMTP':25, "HTTP":80, 
                  "HTTPS":443}

print("#8.")
print("Protocol and Port Dictionary:", Protocol_Port_dictionary)
print(" ")

#9. 
# List your localhost's IPv4 IP address, 
# version, and is_private flag.

ip_str = '192.168.1.14'

# use the ipaddress module
import ipaddress
my_ip = ipaddress.ip_address(ip_str)


print("#9.")
print('IP address:', my_ip)
print('IP version:', my_ip.version)
print('IP address is private:', my_ip.is_private)
print(" ")

#10. 
#List the following about your network.
#   a. Network is private?
#   b. Network is broadcast?
#   c. Network is compressed?
#   d. Network with netmask?
#   e. Network with hostmask?
#   f. Network address count?

network_str = '192.168.1.14/24'
my_net = ipaddress.ip_network(network_str, False)

print("#10.")
print('Network is private:', my_net.is_private)
print('Network is broadcast:', my_net.broadcast_address)
print('Network is compressed:', my_net.compressed)
print('Network with netmask:', my_net.with_netmask)
print('Network with hostmask:', my_net.with_hostmask)
print('Network address count:', my_net.num_addresses)
print(" ")

#11. 
# The network_IPv4.py file has some 
# sample iteration code for listing all 
# the "usable" hosts.
# Why is "usable" in quotes?
print("#11.")
print("?????")
print(" ")

#12. 
# Change the port number to 8500 and 
# run TCPServer.py and TCPClient.py, 
# sending a network message that contains
# your name.
print("#12.")
print("?????")
print(" ")

#13. 
# Why is port 8500 used and not port 80?
print("#13.")
print("?????")
print(" ")

#14. 
# Use the 'math' module to calculate the
# number of bits needed to represent the 
# following number: 128.

import math

my_number = 128

print("#14.")
print("Number of bits needed to respresent 128:", math.log2(my_number))
print(" ")

#15. 
# Use the 'random' module to select a 
# random set of 10 PRIVATE Class A IPv4 
# addresses.
print("#15.")
print("?????")
print(" ")