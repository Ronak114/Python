import os

def arrange_file(files, ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)
    i=1
    for file in files_with_ext:
        os.rename(file, f"photo-{i}{ext}")
        i += 1


if __name__=="__main__":
    files = os.listdir()
    arrange_file(files, ".png")