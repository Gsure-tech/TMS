import zipfile

def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)



if __name__ == "__main__":
    extract_archive("/Users/gsure-tech/Documents/PythonProjects/todo_app/bonus/compressed.zip",
                    dest_dir="/Users/gsure-tech/Documents/PythonProjects/todo_app/bonus/files")

