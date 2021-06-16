# Be användaren att mata in ett tal.   CHECK
# Kontrollera om talet är större än 10. Meddela
# användaren om talet är större än 10- Talet är större än 10. Om det är mindre än 10
# meddela användaren
# – Talet är mindre än 10

#tal = int(input("Mata in tal"))
tal = input("Mata in ett tal")
tal = int(tal)
#print(tal) 
if tal > 10:
    print("Talet större än 10")
if tal < 10:    
    print("Talet är mindre än 10")
