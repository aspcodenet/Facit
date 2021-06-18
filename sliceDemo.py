original = [0, 10, 20, 30, 40, 50, 60] 
print(original)

# [0, 10, 20, 30, 40, 50, 60]

### KVITTO
### 

#Start stop parametrar från position 2 till position 5
for x in range(0,10):
    print(x) #0 
#SKapa en ny lista med elementen 2-5 frpn listan l 
#nya = [  original[2], original[3],original[4]  ]



nyaLista = original[2:5]
for n in nyaLista:
    print(n)
# [20, 30, 40]

#Strunta i start = då avser från början 
nyaLista = original[:3]
for n in nyaLista:
    print(n)
# [0, 10, 20]

ejPaPlan = original[11:]   # strunta i slut = allt till slutet
# [30, 40, 50, 60]

nyaLista = original[:]   # Kopiera en lista faktiskt!
# [0, 10, 20, 30, 40, 50, 60]

	
#Out of range? = inga fel!
print(original[2:10])
# [20, 30, 40, 50, 60]
print(original[5:2])
# []

print(original[5:-5])






