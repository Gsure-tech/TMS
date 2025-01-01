import FreeSimpleGUI as sg

label_feet = sg.Text("Enter feet")
input_box_feet = sg.InputText(key="feet")
label_inches = sg.Text("Enter inches")
input_box_inches = sg.InputText(key="inches")
convert_button = sg.Button("Convert")
label_result = sg.Text(key="result")
