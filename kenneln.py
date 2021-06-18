import json

class Dog: # RITNING
    def __init__(self, name, age, vikt, ras):
        self.name = name
        self.ras = ras  #ras
        self.age = age
        self.vikt = vikt


def PrintMenu():
    print("1. Lista alla")
    print("2. Sök")
    print("3. Skapa ny")
    print("4. Uppdatera")
    print("5. Ta bort")

def CreateNewDog():
    print("SKAPA NY HUND")
    namn = input("Namn:")
    age = int(input("Ålder:"))
    ras = input("Ras:")
    vikt = float(input("Vikt i kg:"))
    d = Dog(namn,age,vikt,ras)
    return d

def LoadFromFile():
    try:
        with open('kenneln.json','r') as f:
            data = json.load(f)
            return data
    except:            
        print("Filen finns ej")
        return []

def SaveToFile(kennelLista):
    with open('kenneln.json', 'w') as json_file:
        json.dump(kennelLista, json_file)


kennel = LoadFromFile()


while True:
    PrintMenu()
    sel = input("Välj action>")
    if sel == "1":
        for dog in kennel:
            print(f"{dog.name} {dog.ras}")
    if sel == "3":
        dog = CreateNewDog()
        kennel.append(dog)
        SaveToFile(kennel)

