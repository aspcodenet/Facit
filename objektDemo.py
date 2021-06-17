class Person: # RITNING
    def __init__(self, name, age, team):
        self.name = name
        self.age = age
        self.team = team
        self.dogs = []

def FindInList(listOfPlayers, partOfName):
    for player in listOfPlayers:
        if partOfName in player.name:
            return player 
    return None

lista = []

while True:
    sel = input()
    if sel == "1":
        print("NY")            
        namn = input("Namn:")
        team = input("Team:")
        age = int(input("age:"))
        p = Person(namn, age, team)
        lista.append(p)
    if sel == "3":
        namn = input("Visa alla som innehåller namn:")
        person = FindInList(lista, namn)
        if person  is None:
            print("Finns ingen träff")
        else:
            print(f" {person.name}  {person.age}")
    if sel == "2":
        print("LISTAR ALLA")            
        for person in lista:
            print(f" {person.name}  {person.age}")




# p = Person("Kalle", 23)
# print(p.name)
# print(p.age)
# p.age = 99
# print(p.age)

# p2 = Person("Lisa", 24)
# print(p2.name)
# print(p2.age)
# p2.age = 45
# print(p2.age)

