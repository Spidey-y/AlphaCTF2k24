from pwn import *
from collections import defaultdict
from typing import List
import math


def minimumFuelCost(roads: List[List[int]], capacity: int) -> int:
    # credits to https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/solutions/3176890/python3-1895-ms-faster-than-94-70-of-python3/
    adjacency_list = defaultdict(list)
    for a, b in roads:
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    total_fuel_cost = [0]

    def dfs(node, parent):
        people = 1
        for neighbor in adjacency_list[node]:
            if neighbor == parent:
                continue
            people += dfs(neighbor, node)
        if node != 0:
            total_fuel_cost[0] += math.ceil(people / capacity)
        return people
    dfs(0, None)
    return total_fuel_cost[0]


p = remote("localhost", 1102)
for _ in range(100):
    roads = eval(p.recvline().decode().split(": ")[1])
    capacity = int(p.recvline().decode().split(": ")[1])
    p.recv(numb=1024)
    p.sendline(str(minimumFuelCost(roads, capacity)))
    print(p.recvline().decode())
p.interactive()
