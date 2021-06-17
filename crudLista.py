players = ["Mats Sundin", "Peter Forsberg", "Anders Eldebrink"]

while True:
    sel = input("1. Add Player  2. List all players 3. Count players 4. Exit")
    if sel == "1":
        players.append(input("Ange spelarens namn:"))
    if sel == "2":        
        for namn in players:
            print(namn)
    if sel == "3":        
        print(f"Antal {len(players)}")

