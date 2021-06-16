#Gör likadant fast med TRE nummer

number1 = input("Mata in ett tal")
number1 = int(number1)

number2 = input("Mata in ett till tal")
number2 = int(number2)


number3 = input("Mata in ett tredje tal")
number3 = int(number3)


largest = 0 # på nåt sätt ska det största in i denna

if number1 > number2 and number1 > number3:
    largest = number1

if number2 > number1 and number2 > number3:
    largest = number2

if number3 > number1 and number3 > number2:
    largest = number3


# if number1 > number2:
#     if number1 > number3:
#         largest = number1
#     else:
#         largest = number3
# else:    
#     if number2 > number3:
#         largest = number2
#     else:
#         largest = number3

print(f"Det största talet är {largest}")
