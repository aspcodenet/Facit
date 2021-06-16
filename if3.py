#Be användaren mata in två tal.number1 och number2.
#Lagra det STÖRSTA talet av dom två i en tredje variabel, largest

#Skriv ut: 
#Det största talet är <>
number1 = input("Mata in ett tal")
number1 = int(number1)

number2 = input("Mata in ett till tal")
number2 = int(number2)

largest = 0 # på nåt sätt ska det största in i denna
if number1 > number2:
    largest = number1
else:    
    largest = number2

print(f"Det största talet är {largest}")



