from PIL import Image
from pathlib import Path

def resize(indir, outdir):
    """ """
    indir = Path(indir)
    outdir = Path(outdir)

    outdir.mkdir(exist_ok=True, parents=True)

    for file in indir.iterdir():

        if file.name[0] == ".":
            continue

        img = Image.open(indir / file)
        w, h = img.size
        img = img.resize((w // 2, h // 2))

        img.save(outdir / file.name)

        
    