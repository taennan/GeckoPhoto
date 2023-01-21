from PySimpleGUI import *
from resize import resize
from rename import rename

layout = [
    [Text("Input directory:")],
    [Input(default_text="/Users/taennanrickman/Desktop/PhotoRename/input", key='-INDIR-')],
    [Text("Output directory:")],
    [Input(default_text="/Users/taennanrickman/Desktop/PhotoRename/output-2", key='-OUTDIR-')],
    [Text()],
    [Text("Rename to:")],
    [Input(default_text="CZ 911", key='-NAME-')],
    [Text()],
    [Text(key="-INFO-")],
    [Button("Process", key="-PROCESS-")],
]

window = Window('Gecko Photo', layout)

while True:
    event, values = window.read()
    
    if event == WINDOW_CLOSED or event == 'Quit':
        break

    indir, outdir, name = (
        values["-INDIR-"],
        values["-OUTDIR-"],
        values["-NAME-"],
    )

    if event == "-PROCESS-":

        try:
            resize(indir, outdir)
            rename(outdir, name)
        except:
            window['-INFO-'].update(f"Couldn't process photos")
        else:
            window['-INFO-'].update(f"Successfully processed photos")

window.close()