from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(y) for y in input().split()])
intelligence_value = int(input())

current_barrel = 0

while True:
    if current_barrel == gun_barrel_size and bullets:
        current_barrel = 0
        print("Reloading!")

    if not bullets or not locks:
        break

    current_bullet = bullets.pop()
    current_barrel += 1
    intelligence_value -= bullet_price
    current_lock = locks.popleft()

    if current_bullet <= current_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")
