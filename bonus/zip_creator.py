import zipfile
import pathlib

def make_achive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir,"compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)



if __name__ == "__main__":
    make_achive(filepaths=["bonus1.py","bonus2.1.py"], dest_dir="dest")