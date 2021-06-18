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
    print("6. Avsluta")


def GetFloatInput(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Mata in ett decimaltal tack!")            


def GetIntInput(prompt,min=0,max=100):
    while True:
        try:
            tal = int(input(prompt))
            if tal >= min and tal <= max:
                return tal
            print(f"Tal mellan {min} och {max}")                    
        except:
            print("Mata in ett heltal tack!")            

def CreateNewDog():
    print("SKAPA NY HUND")
    namn = input("Namn:")
    age = GetIntInput("Ålder:",0,100)
    ras = input("Ras:")
    vikt = GetFloatInput("Vikt i kg:")
    d = Dog(namn,age,vikt,ras)
    return d

def LoadFromFile():
    try:
        with open('kenneln.json','r') as f:
            ret = []
            data = json.load(f)
            for  dic in data:
                ret.append(Dog(**dic))                    
            return ret
    except:            
        print("Filen finns ej")
        return []

def SaveToFile(kennelLista):
    with open('kenneln.json', 'w') as json_file:
        json.dump([b.__dict__ for b in kennelLista], json_file)


def UpdateDog(kennelLista):
    print("Välj hundnummer som du vill uppdatera")
    n = 1
    for dog in kennel:
        print(f"{n}:{dog.name}")
        n = n + 1
    dogIndex = int(input("Nr:")) - 1
    dog = kennelLista[dogIndex]
    print("ÄNDRA  HUND")
    namn = input(f"Namn: {dog.name}")
    if namn == "":
        namn = dog.name
    age = int(input(f"Ålder {dog.age}:"))
    ras = input(f"Ras{dog.ras}:")
    if ras == "":
        ras = dog.name
    vikt = float(input(f"Vikt i kg{dog.vikt}:"))
    dog.name = namn
    dog.age = age
    dog.ras = ras
    dog.vikt = vikt

def Search(kennelLista):
    partOfName = input("Sök efter:")
    result = []
    for dog in kennelLista:
        if partOfName in dog.name:
          result.append(dog)    
    return result           


def DeleteDog(kennelLista):
    print("Välj hundnummer som du vill deleta")
    n = 1
    for dog in kennel:
        print(f"{n}:{dog.name}")
        n = n + 1
    dogIndex = int(input("Nr:")) - 1
    del kennelLista[dogIndex]

#Meningen med kennel = [] med Dogs
kennel = LoadFromFile()


#1 Save ok
#2 tagit bort serialize
#3 Sök
#4 Safe input - int osv

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
    if sel == "2":
        searchResults = Search(kennel)
        for dog in searchResults:
            print(f"{dog.name} {dog.ras}")
    if sel == "4":
        UpdateDog(kennel)
        SaveToFile(kennel)
    if sel == "5":
        DeleteDog(kennel)
        SaveToFile(kennel)
    if sel == "6":
        break


