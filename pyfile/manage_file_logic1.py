import os

def get_files(dirpath, ext):
    """Input:
         -path to directory, raw string
         -file extension with dot, string - like (".txt")
       Return - array of files with given extension
    """
    # files = [file_name for file_name in os.listdir(dirpath)
    #      if os.path.isfile(os.path.join(dirpath, file_name)) and file_name.endswith(ext)]
    # return files

    files = os.path.join

print(get_files(r"E:\work_evg\tutorial\python\pyfile\dir_test", ".png"))

def rename_files(files, prefix):
    i = 0
    for file_name in files:
        os.rename(file_name, str(i))

rename_files(get_files(r"E:\work_evg\tutorial\python\pyfile\dir_test", ".png"), "a")
