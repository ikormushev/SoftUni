def stock_availability(flavours, action, *args):
    if action == "delivery":
        flavours += args
    elif action == "sell":
        if not args:
            flavours.pop(0)
        else:
            if isinstance(args[0], int):
                number = args[0]
                for _ in range(number):
                    flavours.pop(0)
            else:
                for box in args:
                    if box in flavours:
                        for _ in range(flavours.count(box)):
                            flavours.remove(box)

    return flavours


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))

print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))

print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))

print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))

print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))

print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))

print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))