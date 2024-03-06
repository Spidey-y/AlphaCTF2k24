#!/usr/bin/env python3


import random
from sys import exit
from os import environ
from inputimeout import inputimeout
import heapq


FLAG = environ.get("FLAG", "AlphaCTF{fake_flag_for_local_testing}")


class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __repr__(self):
        return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
        return self.f < other.f

    # defining greater than for purposes of heap queue
    def __gt__(self, other):
        return self.f > other.f


def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


def astar(grid, start, end, allow_diagonal_movement=True):
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)

    # Adding a stop condition
    outer_iterations = 0
    max_iterations = (len(grid[0]) * len(grid) // 2)

    # what squares do we search
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    if allow_diagonal_movement:
        adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),
                            (-1, -1), (-1, 1), (1, -1), (1, 1),)

    # Loop until you find the end
    while len(open_list) > 0:
        outer_iterations += 1

        if outer_iterations > max_iterations:
            # if we hit this point return the path such as it is
            # it will not contain the destination
            return None

        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            return return_path(current_node)

        # Generate children
        children = []

        for new_position in adjacent_squares:  # Adjacent squares

            # Get node position
            node_position = (
                current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid)-1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if grid[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) **
                       2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)

    return None


def generate_grid(x):
    sol = None
    while not sol and sol != [(0, 0)]:
        grid = [[0 for _ in range(x)] for _ in range(x)]
        for _ in range(int(0.2 * x * x)):
            i, j = random.randint(0, x-1), random.randint(0, x-1)
            grid[i][j] = 1
        start = (random.randint(0, x-1), random.randint(0, x-1))
        dest = start
        while abs(dest[0] - start[0]) + abs(dest[1] - start[1]) < 3:
            dest = (random.randint(0, x-1), random.randint(0, x-1))
        grid[start[0]][start[1]] = 0
        grid[dest[0]][dest[1]] = 0
        # check if solvable
        sol = astar(grid, start, dest, True)
    return grid, start, dest, sol


def is_other_optimal(sol, ans, grid, start, end):
    # this shit is used to check if the user found another optimal and im too lazy to get all the possibilities
    if ans[0] == sol[0] and ans[-1] == sol[-1] and all([grid[_[0]][_[1]] == 0 for _ in ans]):
        for i in zip(ans[1:-1], sol[1:-1]):
            x_diff = abs(i[0][0] - i[1][0])
            y_diff = abs(i[0][1] - i[1][1])
            if x_diff > 1 or y_diff > 1:
                return False
        for _ in range(len(ans)-1):
            row_diff = abs(ans[_][0] - ans[_+1][0])
            col_diff = abs(ans[_][1] - ans[_+1][1])
            if row_diff > 1 or col_diff > 1:
                return False
        return True
    return False


# "when i wrote this only me and god knew what does it do and why, now looking back at it only god knows" - a meme i found and now im relating to it
if __name__ == "__main__":
    for i in range(100):
        x = 5
        grid, start, end, sol = generate_grid(x)
        grid[start[0]][start[1]] = 'S'
        grid[end[0]][end[1]] = 'D'
        print(f"Find the optimal path from S to D in this grid of length {x}:")
        for row in grid:
            print(" ".join(str(c) for c in row))
        ans = []
        grid[start[0]][start[1]] = 0
        grid[end[0]][end[1]] = 0
        try:
            ans = inputimeout(
                prompt=">>> ", timeout=60)
        except:
            print("Time's up!")
            exit(0)
        if all([c in "[](),0123456789 " for c in ans]):
            ans = eval(ans)
            try:
                assert isinstance(ans, list)
            except:
                print("I expected a list of tuples!")
                exit()
        else:
            print("Invalid input!")
            exit()
        if len(ans) != len(sol):
            print("Nope, that's not the optimal path!")
            exit(0)
        if ans == sol or is_other_optimal(sol, ans, grid, start, end):
            continue
        else:
            print("Nope, that's not the optimal path!")
            exit(0)
    print(f"Congrats! Here's your flag: {FLAG}")
    exit(0)
