processes = [1, 2, 3, 4, 5]

coordinator = max(processes)

def bully_election(initiator):

    global coordinator

    print("Process", initiator, "starts election")

    higher = [p for p in processes if p > initiator]

    if not higher:
        coordinator = initiator
        print("Process", initiator, "becomes coordinator")

    else:
        print("Election message sent to:", higher)
        bully_election(max(higher))

initiator = int(input("Enter initiator process: "))

bully_election(initiator)

print("Coordinator is:", coordinator)