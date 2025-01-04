import FreeSimpleGUI as sg


sg.theme("Black")
label1= sg.Text("Select archive")
input1 = sg.InputText()
choose_button1 = sg.FileBrowse("Choose", key="files")

label2 = sg.Text("Select dest dir:")
input2 = sg.InputText()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window('Archive Extractor',
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]])


# while True:
#     event, values = window.read()
#     print(event, values)
#
#     filepaths = values["files"].split(";")
#     folder = values["folder"]
#     make_achive(filepaths, folder)
#     window["output"].update(value="Compression completed!")

window.read()
window.close()