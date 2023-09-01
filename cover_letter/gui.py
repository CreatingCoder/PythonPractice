import PySimpleGUI as gui
from docxtpl import DocxTemplate
from pathlib import Path


doc_path = Path(__file__).parent / 'template.docx'
doc = DocxTemplate(doc_path)


gui.theme('LightGray2')

letter_vals = [

    [gui.Image('img.png', expand_x=True, expand_y=True, pad=(20,20))],
    [gui.Text('Name'), gui.Input(key='NAME',do_not_clear = True)],
    [gui.Text('Address 1'), gui.Input(key='ADR1',do_not_clear = True)],
    #[gui.Text('Address 2'), gui.Input(key='ADR2',do_not_clear = True)],
    [gui.Text('State'), gui.Input(key='STATE',do_not_clear = True)],
    [gui.Text('City'), gui.Input(key='CITY',do_not_clear = True)],
    [gui.Text('Zip'), gui.Input(key='ZIP',do_not_clear = True)],
    [gui.Text('Phone'), gui.Input(key='PHONE',do_not_clear = True)],
    [gui.Text('Email'), gui.Input(key='EMAIL',do_not_clear = True)],
    [gui.Text('Date'), gui.Input(key='DATE',do_not_clear = True)],
    [gui.Text('Job Announcement'), gui.Input(key='ANNOUNCEMENT_NUM',do_not_clear = True)],
    [gui.Text("Recipient's Name"), gui.Input(key='RECIP_NAME',do_not_clear = True)],
    [gui.Text('Job Position'), gui.Input(key='JOB_POS',do_not_clear = True)],
    [gui.Text('Presently, I am responsible for..'), gui.Input(key='RESPONS',do_not_clear = True)],
    [gui.Text('Current Position'), gui.Input(key='CURR_POS',do_not_clear = True)],
    [gui.Text('Years of Experience'), gui.Input(key='YEARS_EXP',do_not_clear = True)],
    [gui.Text('I have accomplished'), gui.Input(key='ACCOMP',do_not_clear = True)],


    [gui.Button('Create Letter'), gui.Exit()],
]

window = gui.Window('Federal Job Cover Letter Generator', letter_vals, element_justification='right') #, background_color='#DAE0E6')

while True:
    event, values = window.read()

    if event == gui.WINDOW_CLOSED or event == 'Exit':
        break

    elif event == 'Create Letter':
        doc.render(values)
        doc.save(Path(__file__).parent / 'Cover Letter.docx')
        gui.popup('Letter Created!')

window.close()
