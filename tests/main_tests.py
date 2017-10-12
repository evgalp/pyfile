from nose.tools import *
from pyfile.main import *
import os

# print(str(os.getcwd())

def test_first():
    assert_equal("1", "1")

def test_file_exists():
    existing_file = "E:\\work_evg\\tutorial\\python\\pyfile\\tests\\exists.txt"
    not_existing_file = "notexists.txt"
    assert_equal(file_exists(existing_file), True)
    assert_equal(file_exists(not_existing_file), False)


    print(os.path.abspath(os.path.curdir))
    assert_equal(file_exists(existing_file), True)
    assert_equal(file_exists(not_existing_file), False)
