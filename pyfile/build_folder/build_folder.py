import os
import shutil
import sys

def directory_is_empty(src):
    total = len([name for name in os.listdir(src)])
    if total == 0:
        return True
    else:
        return False

def copy_all_files(src, dst):
    files = os.listdir(src)
    total = len([name for name in os.listdir(src)])
    count = 1
    print('\nWorking in directory:\n {0}'.format(src))

    for f in files:
        print('Copying file {0} of {1}...'.format(count, total))
        shutil.copy(os.path.join(src, f), dst)
        count += 1

    print("Done")

def build_mix(in_path):
    os.makedirs(os.path.join(in_path, 'mix'), exist_ok=True)
    print('mix folder created')

    mix_path = os.path.join(in_path, 'mix')
    print('Mix folder path is {0}'.format(mix_path))
    directories = os.listdir(in_path)
    directories.remove('mix')

    for directory in directories:
        directory_path = os.path.join(in_path, directory)
        copy_all_files(directory_path, mix_path)


inpath = sys.argv[1]

build_mix(inpath)


#
# inpath = sys.argv[1]
# outpath = sys.argv[2]
#
# copy_all_files(inpath, outpath)
