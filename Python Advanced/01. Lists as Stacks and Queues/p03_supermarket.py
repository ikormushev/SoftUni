from collections import deque
supermarket_queue = deque([])

while True:
    command = input()
    if command == "End":
        print(f"{len(supermarket_queue)} people remaining.")
        break
    elif command == "Paid":
        while len(supermarket_queue) > 0:
            print(supermarket_queue.popleft())
    else:
        supermarket_queue.append(command)
