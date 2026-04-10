import random


def ft_gen_player_achievements():
    achievements = ["Crafting Genius", "Strategist",
                    "World Savior", "Speed Runner",
                    "Survivor", "Master Explorer",
                    "Treasure Hunter", "Unstoppable",
                    "First Steps", "Collector Supreme",
                    "Untouchable", "Sharp Mind", "Boss Slayer"
                    ]
    n = random.randint(4, 8)
    my = set(random.sample(achievements, n))
    print(my)


ft_gen_player_achievements()
