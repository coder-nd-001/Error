import time

processes = int(input("Enter number of processes: "))

token = 0

def critical_section(process):
    print("Process", process, "entering Critical Section")
    time.sleep(1)
    print("Process", process, "leaving Critical Section")

for i in range(processes):

    print("\nToken with Process", token)

    request = int(input("Does Process want to enter CS? (1-Yes / 0-No): "))

    if request == 1:
        critical_section(token)

    token = (token + 1) % processes