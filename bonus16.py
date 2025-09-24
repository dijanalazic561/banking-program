import FreeSimpleGUI as sg
label1 = sg.Text("Select file to compress ")
input1 = sg.Input()
choose_botton1 = sg.FilesBrowse("Choose")
label2=sg.Text("Select destination folder")
input2=sg.Input()
choose_botton2=sg.FolderBrowse("Choose")
compress_button=sg.Button("Compress")
window=sg.Window("File Compressor",
                 layout=[[label1,input1,choose_botton1],
                         [label2,input2,choose_botton2],
                         [compress_button]])
window.read()
window.close()
