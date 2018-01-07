import logic
from logic import *

def cli_rename_files():
    input_dir = str(input("Input directory path: "))
    input_ext = str(input("Input extension: "))

    output_prefix = str(input("Output prefix: "))
    output_ext = str(input("Output extension: "))
    output_dir = str(input("Output directory path: "))

    files_list = get_files(input_dir, input_ext)
    rename_files(files_list, output_prefix, output_ext, output_dir)



if __name__ == '__main__':
    # cli_rename_files()
    in_paths = get_files(r"E:\work_evg\tutorial\python\pyfile\dir_test", ".png")
    chunk(in_paths, 10)

    # x = os.path.split(r"E:\work_evg\tutorial\python\pyfile\dir_test\kurwa.png")
    # print(x)
    # print(x[0])
    # print(x[1])





    # E:\work_evg\tutorial\python\pyfile\dir_test
