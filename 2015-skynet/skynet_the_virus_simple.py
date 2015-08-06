#!/usr/bin/env python3
# Written by Ivan Anishchuk (anishchuk.ia@gmail.com) in 2015
"""
A very simple solution for Skynet: The Virus.

I haven't cleaned it up because I started doing
more complex "ambush" solution and this became less interesting.
But maybe I'll return and fix it someday.
"""

# N: the total number of nodes in the level, including the gateways
# L: the number of links
# E: the number of exit gateways
N, L, E = [int(i) for i in input().split()]
links = {}
for i in range(L):
    # links between nodes
    node1, node2 = [int(node) for node in input().split()]
    links.setdefault(node1, [])
    links.setdefault(node2, [])
    links[node1].append(node2)
    links[node2].append(node1)
gateways = []
for i in range(E):
    node = int(input())  # the index of a gateway node
    gateways.append(node)
# game loop
while 1:
    # The index of the node on which the Skynet agent is positioned this turn
    agent_node = int(input())

    link = None
    for node in links[agent_node]:
        # Find if agent is too close to gw node and severe the shortest link 
        if node in gateways:
            link = (agent_node, node)
            links[agent_node].remove(node)
            links[node].remove(agent_node)
            break
    if link is None:
        # Agent is not close to gw node, let's severe anything
        # (Assuming the node must be linked to something)
        if links[agent_node]:
            node = links[agent_node][0]
            link = (agent_node, node)
            links[agent_node].remove(node)
            links[node].remove(agent_node)

    if link is not None:
        print(link[0], link[1])
        continue
