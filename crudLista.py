players = []

# f = open("players.txt","r") 
# for line in f:
#     players.append(line)
def RewritePlayersFile(players):
    with open("players.txt","w") as f:
        for player in players:
            f.write(player + "\n")


with open("players.txt","r") as f:
    for line in f:
        players.append(line.replace("\n",""))

while True:
    sel = input("1. Add Player  2. List all players 3. Count players 4. Exit")
    if sel == "1":
        newPlayer = input("Ange spelarens namn:")
        players.append(newPlayer)
        # with open("players.txt","a") as f:
        #     f.write(newPlayer + "\n")
        RewritePlayersFile(players)
    if sel == "2":        
        for namn in players:
            print(namn)
    if sel == "3":        
        print(f"Antal {len(players)}")

