processes = [1, 2, 3, 4, 5]

def ring_election(initiator):

    ids = []

    index = processes.index(initiator)

    print("Election started by", initiator)

    while True:

        ids.append(processes[index])

        index = (index + 1) % len(processes)

        if processes[index] == initiator:
            break

    leader = max(ids)

    print("Processes in election:", ids)
    print("Leader elected:", leader)

initiator = int(input("Enter initiator process: "))

ring_election(initiator)