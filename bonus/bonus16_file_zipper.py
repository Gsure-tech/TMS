import FreeSimpleGUI as sg

label_source = sg.Text("Select files to compress:")
label_destination = sg.Text("Select destination folder:")
input_box1 = sg.InputText()
input_box2 = sg.InputText()
choose_button1 = sg.Button("Choose")
choose_button2 = sg.Button("Choose")

window = sg.Window('File Zipper', layout=[[label_source, input_box1, choose_button1], [label_destination, input_box2, choose_button2]])
window.read()
window.close()