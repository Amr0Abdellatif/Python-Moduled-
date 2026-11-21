#!/usr/bin/env python3


import random

achievment_set: list[str] = ["Crafting Genius", "World Savior",
                             "Master Explorer", "Collecter Supreme",
                             "Untouchable", "Boss Slayer",
                             "Stratigist", "Speed Runner", "Unstopable",
                             "Survivor", "Treasure Hunter", "First Steps",
                             "Sharp Mind", "Habibies Catsher", "Berghein Material",
                             "Probelmatic", "Super Man", "Philosopher",
                             "Standup Comedian", "The Politician"]


# dictionary book!!
players: dict =             {"Amro": [],
                            "Sudhir": [],
                            "Johny": [],
                            "Fernando": []}


def gen_player_achievements():
    achievment_count = len(achievment_set)
    all_sets: list = len(players) * [None]
    i :int = 0


    for name in players:
        rand_num = random.randrange(1, achievment_count + 1)
        players[name] = random.sample(achievment_set, rand_num)
        all_sets[i] = set(players[name])
        print(name, ": ", all_sets[i])
        i += 1


    print("\n\n\n",set.intersection(*all_sets) if all_sets else set())
    print("\n\n\n",set.difference(*all_sets) if all_sets else set())


gen_player_achievements()
