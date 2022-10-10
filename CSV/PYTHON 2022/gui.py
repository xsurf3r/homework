import PySimpleGUI as sg

#Funkcijas

sg.theme('Reddit')

layout = [[sg.Text('Nospied!'),sg.Button('Šķēres')],
[sg.Text('',key='-LEMUMS-')],
[sg.Text('Vārds'),sg.InputText()],
[sg.Button('Neaizvērt')],
[sg.Button('Aizvērt')]]

window = sg.Window('Spēle',layout)
  
while True:
    event, values = window.read()
    if event == 'Šķēres':
        window['-LEMUMS-'].update('Izvēle: šķēres')
    if event == 'Aizvērt':
        break

window.close()
