#!/usr/bin/env python3


import random
from sys import exit
from os import environ
from inputimeout import inputimeout, TimeoutOccurred
from collections import defaultdict
from typing import List
import math


FLAG = environ.get("FLAG", "AlphaCTF{fake_flag_for_local_testing}")


def generate_roads(length):
    roads = []
    for i in range(1, length):
        node = random.randint(0, i - 1)
        roads.append([i, node])
    return roads


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


if __name__ == "__main__":
    for i in range(100):
        roads = generate_roads(random.randint(3, 100))
        capacity = random.randint(1, 20)
        try:
            ans = int(inputimeout(
                prompt=f"roads: {roads}\ncapacity: {capacity}\nWhat's the minimum amount of fuel?\n>>> ", timeout=5))
        except TimeoutOccurred:
            print("Time's up!")
            exit(0)
        except ValueError:
            print("Invalid input!")
            exit(0)
        if ans != minimumFuelCost(roads, capacity):
            print("Wrong answer!")
            exit(0)
        print("Correct!")

    print(f"Congrats! Here's your flag: {FLAG}")
    exit(0)
