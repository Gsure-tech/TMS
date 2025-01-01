import FreeSimpleGUI as sg


label_source = sg.Text("Select files to compress:")
input_box1 = sg.InputText()
choose_button1 = sg.FileBrowse("Choose", key="files")

label_destination = sg.Text("Select destination folder:")
input_box2 = sg.InputText()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")

window = sg.Window('File Zipper', layout=[[label_source, input_box1, choose_button1],
                                          [label_destination, input_box2, choose_button2],
                                          [compress_button]])

while True:
    event, values = window.read()
    print(event, values)

    filepaths = values["files"].split(";")
    folder = values["folder"]

window.read()
window.close()