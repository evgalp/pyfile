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

def rename_files(files, prefix, ext, out_path):
    """Input:
         -files - array of paths to files, list
         -prefix - rename prefix, raw string
         -ext - file extension with dot, string - as (".txt")
         -out_path - path to put renamed files in, raw string
       Changes file names to a format of "prefix_i.ext"
       Return --
    """
    i = 0
    for file_name in files:
        os.rename(file_name, os.path.join(out_path, prefix + str(i) + ext))
        i += 1

if __name__ == '__main__':

    input_dir = str(input("Input directory path: "))
    input_ext = str(input("Input extension: "))

    output_prefix = str(input("Output prefix: "))
    output_ext = str(input("Output extension: "))
    output_dir = str(input("Output directory path: "))

    files_list = get_files(input_dir, input_ext)
    rename_files(files_list, output_prefix, output_ext, output_dir)


    # E:\work_evg\tutorial\python\pyfile\dir_test
