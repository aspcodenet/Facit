# Be användaren mata in en summa på hur mycket pengar den har. Be sedan
# användaren att ange om den har rabatt.

# Om summan är mellan 15 och 25 och användaren inte har rabatt skriv – Du kan köpa en liten hamburgare.
# Om summan är mellan 15 och 25 och användaren har rabatt skriv – Du kan köpa en liten hamburgare och en pommes frites.
# Om summan är större än 25 och mindre än eller lika med 50 och användaren inte har rabatt skriv – Du kan köpa en stor hamburgare.
# Om summan är större än 25 och mindre än eller lika med 50 och användaren har rabatt skriv – Du kan köpa en stor hamburgare och pommes frites.
# Om summan är större än 60 eller om den är mellan 50 och 60 och användaren har rabatt skriv – Du kan köpa ett meal med dryck.


while True:
    summa = int(input("Hur mycket pengar har du:"))
    rabattInput = input("Har du rabatt J/N:")
    harRabatt = False
    if rabattInput.lower() == "j":
        harRabatt = True

    # if summa >= 15 and summa <= 25 and harRabatt == False:
    #     print("Du kan köpa en liten hamburgare.")
    # elif summa >= 15 and summa <= 25 and harRabatt == True:
    #     print("Du kan köpa en liten hamburgare och en pommes frites")

    if summa >= 15 and summa <= 25:
        if harRabatt == False:
            print("Du kan köpa en liten hamburgare.")
        else:
            print("Du kan köpa en l1iten hamburgare och en pommes frites")        
    elif summa > 25 and summa <= 50:
        if harRabatt == False:
            print("Du kan köpa en stor hamburgare.")
        else:
            print("Du kan köpa en stor hamburgare och en pommes frites")                
    elif summa > 60 or (summa >= 50 and summa <=60 and harRabatt == True):
        print("Du kan köpa ett meal med dryck.")

    if input("Vill du göra igen J/N").lower() == "n":
        break

print("Slut på programmet")    