import random
players = ["Martin", "Craig", "Sue",
           "Claire", "Dave", "Alice",
           "Luciana", "Harry", "Jack",
           "Rose", "Lexi", "Maria",
           "Thomas", "James", "William",
           "Ada", "Grace", "Jean",
           "Marissa", "Alan"]
print("Welcome to Team Allocator!")
while True:
    random.shuffle(players)
    team1 = players[:len(players)//2]
    print("Team 1 captain: " + random.choice(team1))
    print("Team 1:")
    for player in team1:
        print(player)
    team2 = players[len(players)//2:]
    print("\nTeam 2 captain: " + random.choice(team2))
    print("Team 2:")
    for player in team2:
        print(player)
    repsonse = input("Pick teams again? Type y or n: ")
    if repsonse == "n":
        break
    if repsonse == "y":
        random.shuffle(players)
    team1 = players[:len(players)//2]
    print("Team 1 captain: " + random.choice(team1))
    print("Team 1:")
    for player in team1:
        print(player)
    team2 = players[len(players)//2:]
    print("\nTeam 2 captain: " + random.choice(team2))
    print("Team 2:")
    for player in team2:
        print(player)
    repsonse = input("Pick teams again? Type y or n: ")

    
