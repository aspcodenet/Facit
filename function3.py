import PySimpleGUI as sg


layout = [
    [sg.Text('Skriv in namn:'), sg.InputText(key='namn')],
    [sg.Text('Skriv in ålder:'),sg.InputText(key='theAge')],
    [sg.Text(' ' * 50,key='result')],
    [sg.Button('Tell me the truth',key='button1'), sg.Button('2'), sg.Exit()] 
]


window = sg.Window('Labbar').Layout(layout)
while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break






