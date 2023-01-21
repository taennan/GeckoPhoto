from pathlib import Path

def rename(directory, name):
    """ """
    directory = Path(directory)

    i = 0
    for file in directory.iterdir():
        file.rename(f"{file.parent}/{name}-{i}{''.join(file.suffixes)}")
        i += 1