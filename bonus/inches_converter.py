import FreeSimpleGUI as sg
from converters14 import convert


sg.theme("Black")
label_feet = sg.Text("Enter feet")
input_box_feet = sg.InputText(key="feet")
label_inches = sg.Text("Enter inches")
input_box_inches = sg.InputText(key="inches")
convert_button = sg.Button("Convert")
exit_button = sg.Button("Exit")
label_result = sg.Text("",key="output")

window = sg.Window("Converter", layout=[[label_feet,input_box_feet],
                                        [label_inches,input_box_inches],
                                        [convert_button, exit_button, label_result]])


while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")

window.close()
