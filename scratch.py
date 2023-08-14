# def jumping_along_the_hummocks(n, c):
#   """
#   Finds the minimum number of jumps required to reach the last hummock from the first.

#   Args:
#     n: The number of hummocks.
#     c: The colors of the hummocks.

#   Returns:
#     The minimum number of jumps required.
#   """

#   # Create a graph where each node represents a hummock.
#   graph = {}
#   for i in range(n):
#     graph[i] = []

#   # Add edges to the graph for each pair of hummocks with the same color.
#   for i in range(n - 1):
#     if c[i] == c[i + 1]:
#       graph[i].append(i + 1)
#     else:
#       print("NOT IF", i + 1, i)

#   # Initialize the distance from the first hummock to all other hummocks to infinity.
#   distance = [float("inf")] * n
#   distance[0] = 0
#   print("GRAPH", graph, "DISTANCE", distance)

#   # Use Dijkstra's algorithm to find the shortest paths from the first hummock to all other hummocks.
#   for i in range(n): # 0 1 2 3 4
#     for j in graph[i]:
#       print((distance[j], distance[i] + 1))
#       distance[j] = min(distance[j], distance[i] + 1)

#   # Return the minimum distance from the first hummock to the last.
#   return distance[-1]


# # def main():
# #   # Read the number of hummocks from stdin.
# #   n = 5

# #   # Read the colors of the hummocks from stdin.
# #   c = [1, 2, 3, 4, 5]

# #   # Find the minimum number of jumps required to reach the last hummock.
# #   distance = jumping_along_the_hummocks(n, c)

# #   # Print the minimum number of jumps.
# #   print(distance)

# # main()
# def main():
#   # Read the number of hummocks from stdin.
#   n = int(input())

#   # Read the colors of the hummocks from stdin.
#   c = list(map(int, input().split()))

#   # Find the minimum number of jumps required to reach the last hummock.
#   distance = jumping_along_the_hummocks(n, c)

#   # Print the minimum number of jumps.
#   print(distance)


# if __name__ == "__main__":
#   main()

def jumping_along_the_hummocks(n, c):

    """
    Finds the minimum number of jumps required to reach the last hummock from the first.

    Args:
    n (type int): The number of hummocks.
    c (type list(int)): The colors of the hummocks.

    Returns:
    type int:  The minimum number of jumps required.
    """

    # get the color of the first hummock
    initial_color = c[0]

    # check how many times that color appears
    aparitions = c.count(initial_color)

    # to get the last aparition we reverse the list
    rever = c[::-1]
    print("REV", rever)

    # there are (aparition-1) jumps to get to the last hummock that has the initial color
    # then the remaining needed jumps are the position of that last hummock in the reversed list

    answer = aparitions - 1 + rever.index(initial_color)

    # finally return the desired number
    return answer


def main():
    # Read the number of hummocks from stdin.
    n = int(input("Insert number of hummocks"))

    # Read the colors of the hummocks from stdin.
    c = []
    for i in range(n):
        s = input(f"Insert the hummock color number {i+1}")
        c.append(int(s))

    # Find the minimum number of jumps required to reach the last hummock.
    distance = jumping_along_the_hummocks(n, c)

    # Print the minimum number of jumps.
    print(f"The minimum number of jumps is {distance}")

if __name__ == "__main__":
    main()