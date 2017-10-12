import os
import sys

def file_exists(in_file):
    """Input: file name, string
    Return: True if path exists and is a file, False otherwise
    """
    return os.path.exists(in_file) and os.path.isfile(in_file)

def copy_file(in_path, out_path):
    """Input: input file name, string; output file name, string;
    Copies file content from in_path to out_path
    Return: True if file was copied, False otherwise
    """

    if file_exists(in_path):
        in_file = open(in_path, 'r')
        in_data = in_file.read()

        out_file = open(out_path, 'w')
        out_file.write(in_data)

        out_file.close()
        in_file.close()

        return True
    else:
        return False

if __name__ == '__main__':
    copy_file()
