import sys


def ft_inventory_system():
    print("=== Inventory System Analysis ===")
    dictt = {}
    args = sys.argv
    for arg in args[1:]:
        lst = arg.split(":")
        if lst[0] in dictt:
            print(f"Redundant item '{lst[0]}' - discarding")
            continue
        if len(lst) == 1:
            print(f"Error - invalid parameter '{lst[0]}'")
            continue
        try:
            value = int(lst[1])
            dictt[lst[0]] = value
        except ValueError as e:
            print(f"Quantity error for '{lst[0]}':  {e}:  '{value}'")
    print("Got inventory:  ", dictt)
    print("Item list:  ", dict.keys(dictt))
    summ = sum(dict.values(dictt))
    print(f"Total quantity of the {len(dictt)} items:  {summ}")
    for key in dict.keys(dictt):
        print(f"Item {key} represents {(dictt[key] / summ * 100):.1f}%")
    maxx = max(dictt.values())
    for key in dictt.keys():
        if dictt[key] == maxx:
            print(f"Item most abundant:  {key} with quantity {dictt[key]}")
            break
    minn = min(dictt.values())
    for key in dictt.keys():
        if dictt[key] == minn:
            print(f"Item least abundant:  {key} with quantity {dictt[key]}")
            break
    dictt['magic_item'] = 1

    print("Updated inventory:  ", dictt)


ft_inventory_system()
