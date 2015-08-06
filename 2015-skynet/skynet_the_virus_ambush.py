#!/usr/bin/env python3
# Written by Ivan Anishchuk (anishchuk.ia@gmail.com) in 2015
"""
A more complex solution for Skynet: The Virus.

It does the "ambush" thing on the fourth test.
I haven't cleaned it up either but it works.
Maybe I'll return and fix it someday.
"""

def walk(old_node, new_node):
    """
    Link walker.

    Needed to determine which way to severe.
    """
    check = [old_node]
    while len(links[new_node]) == 2:
        n = new_node
        new_node = [node for node in links[n] if node != old_node][0]
        old_node = n
        check.append(old_node)
        if new_node in check:
            break
    return new_node

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
        # Find if agent is too close to gw node and severe the shortest link.
        if node in gateways:
            link = (agent_node, node)
            break
    if link is None:
        # The first ambush: block path.
        # Works if there are only two ways from the current node.
        if len(links[agent_node]) == 2:
            node1, node2 = links[agent_node]
            new_node = walk(agent_node, node1)
            if len(links[new_node]) > 2:
                link = (agent_node, node1)
            if link is not None:
                new_node = walk(agent_node, node2)
                if len(links[new_node]) > 2:
                    link = (agent_node, node2)

    if link is None:
        # The second ambush: block path to the largest star.
        # Not sure if it works at all, but should be better than random.
        gw = max(links, key=lambda k: len(links[k]))
        for node1 in links[gw]:
            for node2 in links[gw]:
                if (
                    node1 in links[node2]
                    and len(links[node1]) == 3
                    and len(links[node2]) == 4
                ):
                    link = (node1, node2)
                    break
            if link is not None:
                break

    if link is None:
        # Agent is not close to gw node, let's severe anything.
        # Probably not needed anymore because the second ambush,
        # keeping it just in case.
        if links[agent_node]:
            node = links[agent_node][0]
            link = (agent_node, node)

    if link is not None:
        links[link[0]].remove(link[1])
        links[link[1]].remove(link[0])
        print(link[0], link[1])
        continue
