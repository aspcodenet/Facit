# Dynamisk bankapplikation
# kontonummer - saldo

accounts = {} # dictionary
#allaBarn = ["Fanny", "Josefine"]
#allAccounts = [] # SEB 20 000 000

while True:
    print("1. Add account")
    print("2. Withdraw amount")
    print("3. Deposit amount")
    print("4. Lista alla")
    sel = input()
    if sel == "1":
        kontonummer = input("Vilket kontonummer")
        if kontonummer in accounts:
            print("Nähädu det kontot finns ju redan")
        else:
            accounts[kontonummer] = 0
    if sel == "2":
        kontonummer = input("Vilket kontonummer vill du ta ut ifrån")
        if  kontonummer not in accounts:
            print("Ange ett konto som finns tack")
            continue # Börja om i loopen
        amount = int(input("Hur mycket vill du ta ut?"))
        if amount > accounts[kontonummer]:
            print("Så mycket har du inte")
            print(f"Du har ju bara : {accounts[kontonummer]}")
        else:
            accounts[kontonummer] = accounts[kontonummer] - amount
            print(f"Nytt saldo: {accounts[kontonummer]}")
    if sel == "3":
        kontonummer = input("Vilket kontonummer vill du stoppa in pengar på")
        if  kontonummer not in accounts:
            print("Ange ett konto som finns tack")
            continue # Börja om i loopen
        amount = int(input("Hur mycket vill du sätta in"))
        accounts[kontonummer] = accounts[kontonummer] + amount
    if sel == "4":
        for knr in accounts.keys():
            print(f"Konto:{knr} : {accounts[knr]}")

