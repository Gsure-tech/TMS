import functions
import FreeSimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")

window = sg.Window('My To-Do App', layout=[""])
window.read()
window.close()