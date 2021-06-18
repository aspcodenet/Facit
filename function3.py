import PySimpleGUI as sg

def IsMyndig(age):
    if age >= 18:
        return True
    return False

layout = [
    #[sg.Text('Skriv in namn:'), sg.InputText(key='namn')],
    [sg.Text('Skriv in ålder:'),sg.InputText(key='theAge')],
    [sg.Text(' ' * 50,key='result')],
    [sg.Button('Tell me the truth',key='truthButton'), sg.Button('2'), sg.Exit()] 
]


window = sg.Window('Labbar').Layout(layout)
while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == 'truthButton':
        enteredAge = int(values["theAge"])
        myndig = IsMyndig(enteredAge)
        txt = "EJ myndig"
        if myndig == True:
            txt = "myndig"
        window['result'].update(f"Resultat: du är {txt}")
        #window['result'].update("Nu tryckte nån på knappen")







