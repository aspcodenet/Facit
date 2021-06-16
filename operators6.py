# tal1 = float(input("Mata in tal 1:"))
# tal2 = float(input("Mata in tal 2:"))

# resultat = tal1 ** tal2
# print(resultat)

# resultat = tal1 * tal2
# print(resultat)

# resultat = tal1 / tal2
# print(resultat)

# resultat = tal1 + tal2
# print(resultat)

# resultat = tal1 - tal2
# print(resultat)

# resultat = tal1 % tal2
# print(resultat)

# resultat = tal1 // tal2
# print(resultat)



while True:
    print("1. Ny")
    print("0. Avsluta")
    x = input("Mata in :")
    if x == 0:
        break

x = 0
while x < 10:
    print("Stefan är bäst")
    x = x + 1

print("Det var 10 det")

age=48
name = input("Vad heter du?")

if age > 47 and name == "Stefan":
    print("Du är ung!")
elif age > 47:
    print("Du är gammal")
else:
    print("Du är ung")

print("Done.")



x = 12


x = x + 1

if x != 12: # not 
    print("högstadiet")



chatMessage = input("Message:")

chatMessage = chatMessage.replace("tusan", "*****")
chatMessage = chatMessage.replace("hundan", "******")

# ctrl k+c
# ctrl k+u
print(chatMessage)




# C# float, double - samma som vi ser här = "approximationer"
# C# decimal = EXAKTA!

x = 1
if x + x + x == 3:
    print("Såklart")
else:
    print("Whatt? Hur kan det inte bli 0.3??")    

x = 0.1
if x + x + x == 0.3:
    print("Såklart")
else:
    print("Whatt? Hur kan det inte bli 0.3??")    