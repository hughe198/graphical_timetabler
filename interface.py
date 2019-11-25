import PySimpleGUI as sg


def about():
    sg.Popup('Graphical Timetabler by Ellisonsoft', 'Welcome')


def subject_gui():
    layout = [
        [sg.Text('Class code'), sg.Text("Picture"), sg.Text("Name")]
    ]
    window2 = sg.Window('Subjects', layout, resizable = True, size = (1000,750))

    window2.read()


def table_gui():
    menu_def = [['&File', ['&Open Students File', '&Save Students File', '---', 'Properties', 'E&xit']],
                ['&Import', ['&Matched Classes']],
                ['&Run', ['&Match Classses', '&Generate Jpg',"&Preview"]],
                ['&About', ['About']]
                ]

    layout = [[sg.Menu(menu_def)],
              [
               sg.Button("Preview"),
               sg.Button("Export as Image"),
               sg.Button("Match Classes"),
              sg.Listbox(values=['Student 1', 'Student 2', 'Student 3'], size=(30, 6))
               ]
              ]
    window = sg.Window('Graphical Timetabler', layout, resizable = True, size = (1000,750)
                       )
    event, values = window.read()
    if event == "About":
        about()
    if event == "Match Classses":
        subject_gui()
#    if event =="Open Students File":


    event, values = window.read()

table_gui()

# load students into list box function made in importdata