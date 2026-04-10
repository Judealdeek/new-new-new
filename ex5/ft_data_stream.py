import random


def gen_event():
    players = ["Alice", "Bob", "Dylan", "Charlie"]
    actions = [
               "jump", "run", "walk", "sprint", "crawl",
               "slip", "trip", "laugh", "cry", "shout",
               "whisper", "sing", "dance", "cheer", "fight",
               "attack", "defend", "dodge", "block", "escape",
               "find", "lose", "pick", "drop", "open", "close",
               "break", "fix", "level", "gain", "heal", "cast",
               "use", "activate", "disarm", "win", "challenge",
               "explore", "enter", "leave"
               ]

    while (True):
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def comsume_event(events):
    while events:
        item = random.choice(events)
        events.remove(item)
        yield item


def main():
    print("=== Game Datea Stream Processor ===")
    g = gen_event()
    i = 0
    for i in range(1000):
        print(f"Event {i}:  Player {next(g)[0]} did action {next(g)[1]}")

    print("Built list of 10 events:  ", end="")
    events = []
    for i in range(9):
        events.append(next(g))
    print(events)
    c = comsume_event(events)
    while (events):
        print("Got event from list:  ", next(c))
        print("Remains in list:  ", events)


main()
