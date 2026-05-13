# arr = [10, 20, 30, 40, 50, 60]

# processors = 3
# size = len(arr) // processors

# total = 0

# for i in range(processors):
#     start = i * size
#     end = start + size

#     part = arr[start:end]
#     local_sum = sum(part)

#     print("Processor", i)
#     print("Elements:", part)
#     print("Intermediate Sum:", local_sum)

#     total += local_sum

# print("\nTotal Sum =", total)


print("MPI Environment Initialized")

p = int(input("Enter number of processors: "))

arr = [10, 20, 30, 40, 50, 60]

size = len(arr) // p

total_sum = 0

for rank in range(p):

    start = rank * size

    if rank == p - 1:
        end = len(arr)
    else:
        end = start + size

    part = arr[start:end]

    local_sum = sum(part)

    print("\nProcessor ID:", rank)
    print("Elements:", part)
    print("Local Sum:", local_sum)

    total_sum += local_sum

print("\nFinal Sum =", total_sum)

