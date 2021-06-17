def happy_new_year(wishes = True):
   print("Two...")
   print("Three...")
   print("One...")
   if not wishes:
       return
   print("Happy New Year!")


happy_new_year(True)
happy_new_year(False)



def introduction(first_name, last_name="Kent"):
   #print("Hello, my name is", first_name, last_name)
   print(f"Hello, my name is {first_name} {last_name}")


n = "Luke"
e = "Skywalker"
introduction(n, e)
introduction(n)
introduction(last_name="Clark", first_name="Kent")



def AskForIntValue(language):
    if language == "en":
        print("Enter value:")    
    if language == "sv":
        print("Mata in tal:")

    a = int(input())
    return a

def GetInputLanguage():
    while True:
        lang = input("Ange språk en/sv:")
        if lang == "en" or lang == "sv":
            return lang
        print("Felaktig input")




lang = GetInputLanguage()
a = AskForIntValue(lang)
# ...... 100 000
b = AskForIntValue(lang)
# ...... 100 000
c = AskForIntValue(lang)






# #.... 100 000
# print("Enter value: ")
# b = int(input())
# #.... 100 000
# print("Enter value: ")
# c = int(input())



