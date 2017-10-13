import os

def get_files(path, ext):
    """Input:
         -path - path to directory, raw string
         -ext - file extension with dot, string - as (".txt")
       Return - array of paths to files with given extension
    """

    file_paths_arr = []
    for file_name in os.listdir(path):
        if file_name.endswith(ext):
            file_paths_arr.append(os.path.join(path, file_name))

    return file_paths_arr

# print(get_files(r"E:\work_evg\tutorial\python\pyfile\dir_test", ".png"))

def rename_files(files, prefix, ext, out_path):
    """Input:
         -files - array of paths to files, list
         -prefix - rename prefix, string
         -ext - file extension with dot, string - as (".txt")
         -out_path - path to put renamed files in
       Changes file names to a format of "prefix_i.ext"
       Return --
    """
    i = 0
    for file_name in files:
        os.rename(file_name, os.path.join(out_path, prefix + str(i) + ext))
        i += 1

# rename_files(get_files(r"E:\work_evg\tutorial\python\pyfile\dir_test", ".png"), "a_", ".png", r"E:\work_evg\tutorial\python\pyfile\dir_test")
