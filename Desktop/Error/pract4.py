# # Step 1: Start Program

# # Step 2: Get number of nodes
# n = int(input("Enter number of nodes: "))

# clocks = []

# # Step 3: Get clock time of each node
# for i in range(n):
#     time = int(input(f"Enter time for Node {i+1}: "))
#     clocks.append(time)

# # Step 4: Display initial clocks
# print("\nInitial Clock Times:")
# for i in range(n):
#     print("Node", i+1, ":", clocks[i])

# # Step 5: Master calculates average time
# avg = sum(clocks) / n

# print("\nAverage Time:", avg)

# # Step 6: Calculate adjustment for each node
# print("\nClock Adjustments:")
# for i in range(n):
#     diff = avg - clocks[i]
#     print("Node", i+1, "needs adjustment of", diff)

# # Step 7: Synchronize clocks
# print("\nSynchronized Clock Times:")
# for i in range(n):
#     clocks[i] = avg
#     print("Node", i+1, ":", clocks[i])

# # Step 8: End Program


import random

# Simulated clock times
clocks = {
    "Node1": random.randint(10, 100),
    "Node2": random.randint(10, 100),
    "Node3": random.randint(10, 100),
    "Node4": random.randint(10, 100)
}

print("Initial Clock Times:")
for node, time in clocks.items():
    print(node, ":", time)

# Master collects clock values
total_time = sum(clocks.values())
num_nodes = len(clocks)

# Calculate average time
average_time = total_time / num_nodes

print("\nAverage Time:", average_time)

# Calculate adjustments
print("\nClock Adjustments:")
for node in clocks:
    offset = average_time - clocks[node]
    print(node, "needs adjustment of", offset)

# Synchronize clocks
for node in clocks:
    clocks[node] = average_time

print("\nSynchronized Clock Times:")
for node, time in clocks.items():
    print(node, ":", time)