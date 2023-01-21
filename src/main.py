from PySimpleGUI import *
from pathlib import Path
from resize import resize
from rename import rename

INITIAL_DIR = Path("/Users/taennanrickman/Programming/Projects/Python/GeckoPhoto")
INITIAL_INPUT_DIR = INITIAL_DIR / "photos/input"
INITIAL_OUTPUT_DIR = INITIAL_DIR / "photos/output"

input_input = Input(default_text=INITIAL_INPUT_DIR, enable_events=True, key='-INDIR-')
# NOTE: These browser widgets probably magically change the input values via their 'target' params
input_browser = FolderBrowse("Search", initial_folder=INITIAL_INPUT_DIR, key="-INPUT-BROWSER-")

output_input = Input(default_text=INITIAL_OUTPUT_DIR, enable_events=True, key='-OUTDIR-')
output_browser = FolderBrowse("Search", initial_folder=INITIAL_OUTPUT_DIR, key="-OUTPUT-BROWSER-")

name_input = Input(enable_events=True, key='-BASENAME-')

info_text = Text(pad=((0,0), (10, 10)), key="-INFO-")

process_button = Button("Process", disabled=True, disabled_button_color="#777777" , key="-PROCESS-")

layout = [
    [Text("Input directory:")],
    [input_input, input_browser],
    [Text("Output directory:")],
    [output_input, output_browser],
    [Text()],
    [Text("Rename as:")],
    [name_input],
    [info_text],
    [process_button],
]

window = Window('Gecko Photo', layout)

while True:
    event, values = window.read()

    if event == WINDOW_CLOSED or event == 'Quit':
        break

    indir = Path(values[input_input.key])
    outdir = Path(values[output_input.key])
    name = values[name_input.key].strip()

    if not indir.exists() or name == "":
        process_button.update(disabled=True)
        continue
    process_button.update(disabled=False)

    if event == process_button.key:

        if name == "":
            info_text.update("Please enter a base name to rename photos to")
            continue

        try:
            resize(indir, outdir)
            rename(outdir, name)
        except:
            info_text.update("Couldn't rename photos")
        else:
            info_text.update("Successfully renamed photos")
    

window.close()