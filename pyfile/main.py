import os
import sys

def file_exists(in_file):
    """Input: file name, string
    Return: True if file exists, False otherwise
    """
    to_check = open(in_file)
    if to_check:
        return True
    else:
        return False
