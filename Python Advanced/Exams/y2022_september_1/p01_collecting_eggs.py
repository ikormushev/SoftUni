from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
pieces_of_paper = deque([int(x) for x in input().split(", ")])

box_size = 50
boxes_filled = 0

while eggs and pieces_of_paper:
    egg = eggs.popleft()
    paper = pieces_of_paper.pop()

    if egg <= 0:
        pieces_of_paper.append(paper)
        continue
    elif egg == 13:
        paper_to_swap = pieces_of_paper.popleft()
        pieces_of_paper.appendleft(paper)
        pieces_of_paper.append(paper_to_swap)
        continue

    if egg + paper <= box_size:
        boxes_filled += 1

if boxes_filled:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print("Eggs left:", end=" ")
    print(*eggs, sep=", ")

if pieces_of_paper:
    print("Pieces of paper left:", end=" ")
    print(*pieces_of_paper, sep=", ")
