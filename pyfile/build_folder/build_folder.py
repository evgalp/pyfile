import os
import shutil
import sys

def folder_is_empty(src):
    total = len([name for name in os.listdir(src)])
    if total == 0:
        return True
    else:
        return False

def copy_all_files(src, dst):
    files = os.listdir(src)
    total = len([name for name in os.listdir(src)])
    count = 1
    print('\nWorking in directory {0}'.format(src))
    for f in files:
        print('Copying file {0} of {1}...'.format(count, total))
        shutil.copy(os.path.join(src, f), dst)
        count += 1

def build_path(out_path, *args):

    args = sys.argv[1:]

    if os.path.isdir(out_path):
        print(args[1:])
        return True
    else:
        return False

inpath = sys.argv[1]
outpath = sys.argv[2]

copy_all_files(inpath, outpath)
# print(folder_is_empty(inpath))
# print(folder_is_empty(outpath))



# print(build_path(out_path_test))

# def ran_args(*args):
#     print(args[1:])
#
# ran_args(0,1,2)

# test_src = "E:\work_evg\tutorial\python\pyfile\test_files\test_dst"

# print (r"E:\aaa")
# print(os.path.join(sys.argv[1]))

# move_all_files()
