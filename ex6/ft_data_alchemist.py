import random


def ft_data_alchemist():
    print("=== Game Data Alchemist ===\n")
    players = [
            "Alice", "bob", "Charlie", "dylan", "Emma",
            "Gregory", "jhon", "Kevin", "liam"
            ]
    print("Initial list of players:  ", players)
    list1 = [player.capitalize() for player in players]
    print("New list with all names capitalized:  ", list1)
    list2 = [player for player in players if player == player.capitalize()]
    print("New list of capitalized names only:  ", list2)
    dictt = {player: random.randint(0, 1000) for player in list1}
    print("\nScore dict:  ", dictt)
    avg = sum(dictt.values()) / len(dictt)
    print("Score average is {avg:.2f}")

    high_scores = {
            name: score for name, score in dictt.items()
            if score >= avg
            }
    print("High scores:  ", high_scores)


ft_data_alchemist()
